#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import sys,time
print(sys.path)
print(sys.version)
from math import sqrt, cos, sin
import rospy
#import tf2_ros
import tf,tf2_ros
import numpy as np
from time import sleep
from geometry_msgs.msg import Twist, Pose, TransformStamped,Quaternion
from sensor_msgs.msg import Imu, JointState
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import *
from geometry_msgs.msg import Point, Vector3, PoseWithCovarianceStamped

import commands as cmd
#import msvcrt
#import keyboard
import pyproacmd
from pyproacmd import Utils
import struct
import time

from pypro.msg import StateWheels

from sensor_msgs.msg import Joy


import rosparam
#params = rosparam.get_param("/km_dolly_wheels")
#if params['connect_mode']=='ble':
#    from pykeigan import blecontroller
#    SLEEP_TIME = 0.01
#else:
#    from pykeigan import usbcontroller
#    SLEEP_TIME = 0.1
import atexit

D_RIGHT= 0.104#0.109 #0.1045#0.098#    #m, right wheel radius
D_LEFT= 0.104 #0.109 #0.1045#0.098#     #m, left wheel radius
ACC = 20
#TREAD=0.4 #0.447  #m, length between wheels
TREAD=0.45  #m, length between wheels
perimeter= 0.657   #m distance traveled
LINEAR_RATIO = 0.50 # Tuning parameter of dolly linear speed
ANGULAR_RATIO = 20.0 #Tuning parameter of dolly angular speed
GYRO_OFFSET = np.array([-0.02053863,0.0176115,0.03733194])
baud = 1000000

SLEEP_TIME = 0.001 #0.015#0.05
#200mm diameter
def calc_input(omega_r,omega_l):
    """
    Parameters
    ----------
    omega_r, omega_l : float
        angular velocities of the wheels
    Returns
    ----------
    v : float
        Linear velocity of the dolly
    yawrate : float
        Yaw anguler velocity of the dolly
    """
    vr = D_RIGHT*omega_r
    vl = D_LEFT*omega_l
    v = (vr + vl) / 2.0
    yawrate= (vr - vl) / (TREAD / 2.0)*1.06
    u = np.array([v, yawrate])
    return u

def MotionModel(x,u,dt):
    """
    Parameters
    ----------
    x : array
        Dolly pose at the last timestamp. Location and orientation (loc_x,loc_y,theta) of the dolly.
    u : array
        Dolly velocity. Linear and yaw angular velocity of the dolly.
    dt : float
        The difference between the current and last timestamp.
    Returns
    ----------
    x : array
        Estimated dolly pose at the current timestamp. Location and orientation (loc_x,loc_y,theta) of the dolly.
    """
    loc_x = x[0]#x[0]
    loc_y = x[1]#x[1]
    theta = x[2]#x[2]
    v = u[0]
    omega = u[1] / 2.0
    loc_x = loc_x - np.sin(theta + np.pi / 2) * v * dt#loc_x - np.cos(theta + np.pi / 2) * v * dt
    loc_y = loc_y + np.cos(theta + np.pi / 2) * v * dt#loc_y + np.sin(theta + np.pi / 2) * v * dt
    theta = theta + omega * dt#theta + omega * dt
    theta = PItoPI(theta)
    x = np.array([loc_x, loc_y, theta])
    return x
    

def PItoPI(angle):
    while angle >= np.pi:
        angle = angle - 2 * np.pi
    while angle <= -np.pi:
        angle = angle + 2 * np.pi
    return angle

class KeyCtrlr:
    
    def __init__(self, proacmd, id_L=1, id_R=2):
        self.pc = proacmd
        self.id_L = id_L
        self.id_R = id_R
        self.velm=0
        self.posm=0
        #self.current_motor_left=0
        self.current_motor=0
        

    def runvel_handler(self,vel):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-vel)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))

    def forward_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))
    
    def backward_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-1200)))

    def left_rotate_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))
    
    def right_rotate_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-1200)))

    def enable_handler(self):
        result = self.pc.send_receive(cmd.Enable(self.id_R))

    def disable_handler(self):
        result = self.pc.send_receive(cmd.Disable(self.id_R))
    
    def read_foc_handler(self):
        result = self.pc.send_receive(cmd.ReadFOC(self.id_R))
        if result is not None and result.resp.body[1] < 700 and result.resp.body[1] > -700:
            self.velm=result.resp.body[1]
            if result.resp.body[2] < 30 and result.resp.body[2] > -30:
                self.current_motor=result.resp.body[2]
        #print('VR#{0}'.format(velm))
        #self.posm=result.resp.body[0]
    
    def move_to_handler(self, pos):
        result = self.pc.send_receive(cmd.MoveTo(self.id_R, pos))

    def close(self):
        self.pc.sclose()

class KeyCtrll:
    
    def __init__(self, proacmd, id_L=1, id_R=2):
        self.pc = proacmd
        self.id_L = id_L
        self.id_R = id_R
        self.velm=0
        self.posm=0
        self.current_motor=0
        
    
    def runvel_handler(self,vel):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(vel)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))

    def forward_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))
    
    def backward_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(-1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-1200)))

    def left_rotate_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(-1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))
    
    def right_rotate_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-1200)))

    def enable_handler(self):
        result = self.pc.send_receive(cmd.Enable(self.id_L))
        #result = self.pc.send_receive(cmd.Disable(self.id_R))

    def disable_handler(self):
        result = self.pc.send_receive(cmd.Disable(self.id_L))
        #result = self.pc.send_receive(cmd.Disable(self.id_R))
    
    def read_foc_handler(self):
        result = self.pc.send_receive(cmd.ReadFOC(self.id_L))
        if result is not None and result.resp.body[1] < 700 and result.resp.body[1] > -700:
            self.velm=result.resp.body[1]
            if result.resp.body[2] < 30 and result.resp.body[2] > -30:
                self.current_motor=result.resp.body[2]
        #self.posm=result.resp.body[0]
        #result = self.pc.send_receive(cmd.ReadFOC(self.id_R))
    
    def move_to_handler(self, pos):
        result = self.pc.send_receive(cmd.MoveTo(self.id_L, pos))

    def close(self):
        self.pc.sclose()



class PitWheels:
    def __init__(self):
        self.left_pub = rospy.Publisher('left_wheel', Float32, queue_size=1)
        self.right_pub = rospy.Publisher('right_wheel', Float32, queue_size=1)
        self.dbg_pub = rospy.Publisher('test', Float32, queue_size=1)
        self.wheels_pub = rospy.Publisher('wheels_wheels', Vector3, queue_size=1)
        self.current_pub = rospy.Publisher('amperage', Vector3, queue_size=1)
        self.state_wheels_pub = rospy.Publisher('stateWheels',StateWheels, queue_size=1)
        '''
        left wheel: front:x,left:-z,top:-y left-handed cordinate
        '''
        #self.left_w_dev = usbcontroller.USBController(params['left_w_addr'])
        pc = pyproacmd.ProaCmd('/dev/serial/by-id/usb-STMicroelectronics_STM32_STLink_0668FF343537424257252450-if02', baud)
        pc2 = pyproacmd.ProaCmd('/dev/serial/by-id/usb-STMicroelectronics_STM32_STLink_066FFF555449836687205519-if02', baud)
        self.left_w_rpm= Float32()
        self.right_w_rpm= Float32()
        self.left_w_dev = KeyCtrlr(pc)
        self.right_w_dev = KeyCtrll(pc2)
        self.left_w_dev.enable_handler()
        sleep(0.5)
        self.right_w_dev.enable_handler()
        sleep(0.5)
        self.left_w_dev.enable_handler()
        sleep(0.5)
        self.right_w_dev.enable_handler()
        #self.left_w_dev.read_foc_handler()
        #self.right_w_dev.read_foc_handler()
        print("Left Wheel Connected")
        rospy.loginfo("Connected to Left Wheel")
        '''
        right wheel: front:-x,left:z,top:-y left-handed cordinate
        '''
        #self.right_w_dev = usbcontroller.USBController(params['right_w_addr'])
        print("Right Wheel Connected")
        rospy.loginfo("Connected to Right Wheel")
        rospy.on_shutdown(self.shutdown)
   
        self.odo = Odometry()
        self.odo.header.frame_id='odom'
        self.odo.child_frame_id='base_link' #quick fix
        self.odocount = 0
        self.pub_odo = rospy.Publisher('/odom', Odometry,queue_size=10)
        self.x = np.array([0.0, 0.0, 0.0])
        self.current_time = time.time()
        self.last_time = time.time()

        self.tf_broadcaster = tf2_ros.TransformBroadcaster()

        self.odom_trans = TransformStamped()
        self.odom_trans.header.stamp = rospy.Time.now()
        self.odom_trans.header.frame_id = "odom"
        self.odom_trans.child_frame_id = "base_link"

        self.right_velocity = 0
        self.left_velocity = 0
        self.calc_right_vel =0
        self.calc_left_vel =0
        self.motors_enabled=False
        self.disable_motors()

        self.xPosLas = 0
        self.yPosLas =0 
        self.angLas =0
        self.ang2Las=0
        self.brinco=False
        self.max_speed = rospy.get_param("/pitakuru_wheels/max_speed")
        self.joint_pub = rospy.Publisher('joint_states', JointState, queue_size=10)
        self.can_correct=False
        self.l_curr=0
        self.r_curr=0
        self.xini=0
        self.yini=0
        self.zrini=0
        self.wrini=0

        rospy.Subscriber('/cmd_vel', Twist, self.teleop_callback, queue_size=1)
        rospy.Subscriber('/poseupdate', PoseWithCovarianceStamped, self.correct_callback, queue_size=1)
        rospy.Subscriber('/euler2', Float64, self.angle_callback, queue_size=1)

        self.read_vars()

        
    #def write_odom_file(self):
        

    def read_vars(self):
        ffile=open('/home/xavier/catkin_ws/src/pitakuru/config/initodom.txt','r').read()
        variable="x"
        ini=ffile.find(variable)+(len(variable)+1)
        rest=ffile[ini:]
        search_enter=rest.find('\n')
        self.xini=float(rest[:search_enter])

        variable="y"
        ini=ffile.find(variable)+(len(variable)+1)
        rest=ffile[ini:]
        search_enter=rest.find('\n')
        self.yini=float(rest[:search_enter])

        variable="rz"
        ini=ffile.find(variable)+(len(variable)+1)
        rest=ffile[ini:]
        search_enter=rest.find('\n')
        self.zrini=float(rest[:search_enter])

        variable="rww"
        ini=ffile.find(variable)+(len(variable)+1)
        rest=ffile[ini:]
        search_enter=rest.find('\n')
        self.wrini=float(rest[:search_enter])
        #print(" value")
        
        self.odo.pose.pose.position.x=self.xini
        self.odo.pose.pose.position.y=self.yini
        self.odo.pose.pose.orientation.z=self.zrini
        self.odo.pose.pose.orientation.w=self.wrini
        angs= tf.transformations.euler_from_quaternion([0,0,self.zrini,self.wrini])
        self.x[0]=self.xini
        self.x[1]=self.yini
        self.x[2]=angs[2]
        print "xini:",self.xini
        print "yini:",self.yini
        print "zini:",self.zrini
        print "wini:",self.wrini
        print(angs)



    

    def reset_odom(self):
        self.x[0]=0
        self.x[1]=0
        self.x[2]=0
        self.odo.pose.pose.position.x = self.x[0]
        self.odo.pose.pose.position.y = self.x[1]
        q = tf.transformations.quaternion_from_euler(0, 0, self.x[2])
        self.odo.pose.pose.orientation = Quaternion(*q)
        self.odo.twist.twist.linear.x = 0
        self.odo.twist.twist.linear.y = 0
        self.odo.twist.twist.angular.z = 0
        self.odom_trans.header.stamp = rospy.Time.now()
        self.odom_trans.transform.translation.x = self.x[0]
        self.odom_trans.transform.translation.y = self.x[1]
        self.odom_trans.transform.translation.z = 0
        self.odom_trans.transform.rotation = Quaternion(*q)
        print("reseting_odom")
    def enable_motors(self):
        self.left_w_dev.enable_handler()
        sleep(0.01)
        self.right_w_dev.enable_handler()
    
    def disable_motors(self):
        self.left_w_dev.disable_handler()
        sleep(0.01)
        self.right_w_dev.disable_handler()

    def pubodo2(self):
        try:
            self.left_w_dev.read_foc_handler()
            self.right_w_dev.read_foc_handler()
            self.left_w_rpm.data=self.left_w_dev.velm
            self.right_w_rpm=self.right_w_dev.velm
            self.left_pub.publish(self.left_w_rpm)
            self.right_pub.publish(self.right_w_rpm)
            #left_velocity = (self.left_w_dev.velm/21)*1# float v_=round(msg.linear.x / (5.68))*31;//rad/s and gear ratio: 5.5  and the wheel Radius 31 milimeter
            #left_position = self.left_w_dev.posm #lvalues['position']

            #rvalues = self.left_w_dev.read_foc_handler #self.right_w_dev.read_motor_measurement()
            
            
            #rospy.sleep(0.01)
            #right_velocity = (self.right_w_dev.velm/21)*1#self.right_w_dev.velm#rvalues['velocity']
            
        except:
            import traceback
            traceback.print_exc()


    def pubodo(self):
        try:
            self.odocount += 1
            
            #lvalues = self.left_w_dev.read_foc_handler#self.left_w_dev.read_motor_measurement()
            self.left_w_dev.read_foc_handler()
            self.right_w_dev.read_foc_handler()
            #rospy.sleep(0.01)
            left_velocity = (self.left_w_dev.velm/21)*1# float v_=round(msg.linear.x / (5.68))*31;//rad/s and gear ratio: 5.5  and the wheel Radius 31 milimeter
            self.calc_left_vel=0.6*left_velocity+0.4*self.calc_left_vel
            #print('LV#{0}'.format(left_velocity))
            #left_position = self.left_w_dev.posm #lvalues['position']
            #rvalues = self.left_w_dev.read_foc_handler #self.right_w_dev.read_motor_measurement()
            #rospy.sleep(0.01)
            right_velocity = (self.right_w_dev.velm/21)*1#self.right_w_dev.velm#rvalues['velocity']
            self.calc_right_vel=0.6*right_velocity+0.4*self.calc_right_vel
            self.left_w_rpm.data = self.left_w_dev.velm
            #self.right_w_rpm=self.right_w_dev.velm
            #rospy.logerr("hello pypro")
            self.left_pub.publish(self.left_w_rpm)
            self.right_pub.publish(self.right_w_rpm)
            
            ampere = Vector3()
            alfa=0.94
            self.l_curr=self.l_curr*alfa+(1-alfa)*abs(self.left_w_dev.current_motor)
            self.r_curr=self.r_curr*alfa+(1-alfa)*abs(self.right_w_dev.current_motor)
            ampere.x=self.r_curr
            ampere.y=self.l_curr
            ampere.z=self.current_time
            self.current_pub.publish(ampere)

            # vec2 = Vector3()
            # vec2.x = right_velocity
            # vec2.y = left_velocity
            # vec2.z = self.current_time
            # self.wheels_pub.publish(vec2)
            state_wheels = StateWheels()
            state_wheels.left_vel = self.calc_left_vel#left_velocity
            state_wheels.right_vel = self.calc_right_vel#right_velocity
            state_wheels.left_current = self.l_curr #abs(self.left_w_dev.current_motor)
            state_wheels.right_current = self.r_curr#abs(self.right_w_dev.current_motor)
            state_wheels.time_stamp = rospy.Time.now()
            self.state_wheels_pub.publish(state_wheels)
            #rospy.logerr("hello pypro2")
            
            #float v_=round(msg.linear.x / (5.68))*31;//rad/s and gear ratio: 5.5  and the wheel Radius 31 milimeter
            #print('RV#{0}'.format(right_velocity))
            #right_position = self.right_w_dev.posm#rvalues['position']
            #float v_=round(msg.linear.x / (5.68))*31;//rad/s and gear ratio: 5.5  and the wheel Radius 31 milimeter
            #u = calc_input(-right_velocity, left_velocity)#right wheel rotates backwards
            u = calc_input(-self.calc_right_vel, self.calc_left_vel)#right wheel rotates backwards

            # if self.can_correct:
            # ######################################################################
            #     self.x[0]=self.x[0]*0.6+0.4*self.xPosLas
            #     self.x[1]=self.x[1]*0.6+0.4*self.yPosLas
            #     self.can_correct=False
            #     if not self.brinco:
            #         #self.x[2]=self.x[2]*0.95+0.05*self.angLas
            #         self.x[2]=self.x[2]*0.9+0.1*self.angLas
            #     else:
            #         self.x[2]=self.angLas
            ######################################################################
            old_theta = self.x[2]
            self.current_time = time.time()
            dt = self.current_time-self.last_time
            self.x = MotionModel(self.x,u,dt)
            self.last_time = time.time()
            self.odo.header.seq = self.odocount
            self.odo.header.stamp = rospy.Time.now()
            self.odo.pose.pose.position.x = self.x[0]
            self.odo.pose.pose.position.y = self.x[1]

            q = tf.transformations.quaternion_from_euler(0, 0, self.x[2])
            self.odo.pose.pose.orientation = Quaternion(*q)
            self.odo.twist.twist.linear.x = -u[0]#-np.sin(self.x[2] + np.pi / 2) * u[0] #-u[0]/dt #-np.sin(self.x[2] + np.pi / 2) * u[0] 
            self.odo.twist.twist.linear.y = 0 #np.cos(self.x[2] + np.pi / 2) * u[0] #0 #np.cos(self.x[2] + np.pi / 2) * u[0] 
            #self.odo.twist.twist.linear.x = u[0]
            self.odo.twist.twist.angular.z = u[1]/2.0 #u[1]/2.0

            self.pub_odo.publish(self.odo)

            self.odom_trans.header.stamp = rospy.Time.now()
            self.odom_trans.transform.translation.x = self.x[0] #-self.x[1]
            self.odom_trans.transform.translation.y = self.x[1] #self.x[0]
            self.odom_trans.transform.translation.z = 0
            self.odom_trans.transform.rotation = Quaternion(*q)
            
            self.tf_broadcaster.sendTransform(self.odom_trans)

            # joint_state = JointState()
            # joint_state.header = Header()
            # joint_state.header.stamp = rospy.Time.now()
            # joint_state.name = ['left_wheel_joint', 'right_wheel_joint']
            # #joint_state.position = [-left_position%3.14, -right_position%3.14]
            # joint_state.velocity = []
            # joint_state.effort = []
            # self.joint_pub.publish(joint_state)
            #self.run_ctrl_cmd()
        except:
            import traceback
            traceback.print_exc()

    def teleop_callback(self, data):
	#linear_speed = data.linear.x
        #angular_speed = data.angular.z
        if(data.linear.y==-1 and self.motors_enabled==True):
            self.motors_enabled=False
            self.disable_motors()
        elif(data.linear.y==1 and self.motors_enabled==False):
            self.motors_enabled=True
            self.enable_motors()
        linear_speed = ((data.linear.x*21)/0.1045)*10
        angular_speed = ((data.angular.z*21)/0.1045)*2
        #rospy.logerr("a speed: {}".format(angular_speed))
        new_right_velocity = linear_speed - angular_speed#linear_speed + angular_speed 
        new_left_velocity = linear_speed + angular_speed#linear_speed - angular_speed
        #if self.right_velocity != new_right_velocity or self.left_velocity != new_left_velocity:
        self.right_velocity = new_right_velocity
        self.left_velocity = new_left_velocity
        self.run_ctrl_cmd()
        #linear_speed = LINEAR_RATIO * data.linear.x
        #angular_speed = ANGULAR_RATIO * data.angular.z
        #new_right_velocity = linear_speed / D_RIGHT + angular_speed / (TREAD/D_RIGHT/2)
        #new_left_velocity = linear_speed / D_LEFT - angular_speed / (TREAD/D_LEFT/2)
        #if self.right_velocity != new_right_velocity or self.left_velocity != new_left_velocity:
        #    self.right_velocity = new_right_velocity
        #    self.left_velocity = new_left_velocity
        #    self.run_ctrl_cmd()
    
    def correct_callback(self, data):
        
	#rospy.logerr("got correct callback")
        self.yPosLas =data.pose.pose.position.y
        self.xPosLas =data.pose.pose.position.x
        self.can_correct=True
        self.dbg_pub.publish(self.yPosLas-self.x[1])
        #print(self.xPosLas)
        #print(self.yPosLas-self.x[1])
        #self.angLas =data.pose.pose.orientation.z
        #self.ang2Las=data.pose.pose.orientation.w


    def angle_callback(self, data): 
	#rospy.logerr("angle {}".format(data.data))  
        if data.data<-173 or data.data>173:
            self.brinco=True
        else:
            self.brinco=False
        self.angLas =data.data*3.1416/180
        #self.angLas =data.pose.pose.orientation.z
        #self.ang2Las=data.pose.pose.orientation.w    

    def run_ctrl_cmd(self):
        lim=self.max_speed
        if self.left_velocity<lim and self.left_velocity>-lim:
            self.left_w_dev.runvel_handler(int(self.left_velocity))
            #rospy.sleep(0.017)
        elif  self.left_velocity>lim:
            self.left_w_dev.runvel_handler(int(lim))
        elif  self.left_velocity<-lim:
            self.left_w_dev.runvel_handler(int(-lim))
        if self.right_velocity<lim and self.right_velocity>-lim:
            self.right_w_dev.runvel_handler(int(self.right_velocity))  
            #rospy.sleep(0.017)
        elif  self.right_velocity>lim:
            self.right_w_dev.runvel_handler(int(lim))
        elif  self.right_velocity<-lim:
            self.right_w_dev.runvel_handler(int(-lim))
        #self.left_w_dev.runvel_handler(int(self.left_velocity))
        #rospy.sleep(0.02)
        #self.right_w_dev.runvel_handler(int(self.right_velocity))
        #rospy.sleep(0.02)
        #self.left_pub.publish(self.left_velocity)
        #self.right_pub.publish(self.right_velocity)
        #if self.left_velocity!=0:
        #if self.left_velocity==0:
            #self.left_w_dev.set_speed(-np.abs(self.left_velocity))
        #    if self.left_velocity > 0:
        #        self.left_w_dev.run_reverse()
        #    elif self.left_velocity < 0:
        #        self.left_w_dev.run_forward()
        #else:
        #    self.left_w_dev.runvel_handler(0)
        #if self.right_velocity != 0:
        #if self.right_velocity==0:
        #    self.right_w_dev.set_speed(-np.abs(self.right_velocity))
        #    if self.right_velocity > 0:
        #        self.right_w_dev.run_forward()
        #    elif self.right_velocity < 0:
        #        self.right_w_dev.run_reverse()
        #else:
        #    self.right_w_dev.runvel_handler(0)

    def shutdown(self):
        #rospy.sleep(1)
        self.left_w_dev.disable_handler()
        self.right_w_dev.disable_handler()
        self.left_w_dev.close()
        sleep(0.1)        
        self.right_w_dev.close()
        sleep(0.1)
        #self.right_w_dev.finish_auto_serial_reading()  # ??????????????????????????????????????????
        #self.left_w_dev.finish_auto_serial_reading()  # ??????????????????????????????????????????
        #self.right_w_dev.set_led(1, 100, 100, 100)
        #self.left_w_dev.set_led(1, 100, 100, 100)
        #rospy.sleep(1)
        # atexit.register()#??????????????????????????????

def pit_wheels_main():
    rospy.init_node('pit_wheels', anonymous = True)
    pit_wheels = PitWheels()
    # for k in range(10):
    #     try:
    #         pit_wheels = PitWheels()
    #     except:
    #         print "Initializing ERROR"
    #         sleep(1)
    #     else:
    #         break

    while not rospy.is_shutdown():
        pit_wheels.pubodo()
        sleep(SLEEP_TIME)
        
   

if __name__=='__main__':
    try:
        pit_wheels_main()
    except rospy.ROSInterruptException:
        print("finish")
        #pit_wheels.shutdown()

