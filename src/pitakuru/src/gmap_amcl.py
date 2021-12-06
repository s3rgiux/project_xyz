#!/usr/bin/env python
# coding: utf-8

import os
import rospy
import subprocess
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from time import sleep
import tf
import geometry_msgs.msg
import time
from nav_msgs.msg import Odometry

class GmapAmcl(object):
    def __init__(self):
        self.init_pose = geometry_msgs.msg.PoseWithCovarianceStamped()
        self.xini = 0.0
        self.yini = 0.0
        self.zrini = 0.0
        self.wrini = 0.0
        self.read_vars()
        rospy.init_node('gmap_amcl')
        self.sub = rospy.Subscriber('/j0/joy', Joy, self.joy_callback,queue_size=1)
        rospy.Subscriber('/amcl_pose', geometry_msgs.msg.PoseWithCovarianceStamped, self.pose_callback, queue_size=1)
        rospy.Subscriber('/odom', Odometry, self.odom_callback, queue_size=1)
        self.pub_sys = rospy.Publisher('/syscommand', String, queue_size=1)
        self.button_states = dict()

        self.listener = tf.TransformListener()
        self.pub_init_pose = rospy.Publisher('/initialpose', geometry_msgs.msg.PoseWithCovarianceStamped)
        self.nuevain = geometry_msgs.msg.PoseWithCovarianceStamped()
        self.actual_tf = geometry_msgs.msg.PoseWithCovarianceStamped()
        self.saved_pose = geometry_msgs.msg.PoseWithCovarianceStamped()
        self.pose_amcl = geometry_msgs.msg.PoseWithCovarianceStamped()
        self.pose_amcl.pose.pose.position.x = self.xini
        self.pose_amcl.pose.pose.position.y = self.yini
        self.pose_amcl.pose.pose.orientation.z = self.zrini
        self.pose_amcl.pose.pose.orientation.w = self.wrini

        self.use_ps4_controller = False        

        self.gmap_running = False
        self.amcl_running = True
        self.last_time = time.time()
        sleep(6)
        self.pub_init_pose.publish(self.init_pose)
        self.odom_pose = Odometry()
        
    def odom_callback(self,odometry_msg):
        self.odom_pose = odometry_msg

    def pose_callback(self, data):
        self.pose_amcl = data
    def write_vars(self):
        with open('/home/xavier/catkin_ws/src/pitakuru/config/initpose.txt','w') as f:
            f.write("x="+str(self.pose_amcl.pose.pose.position.x)+"\n")
            f.write("y="+str(self.pose_amcl.pose.pose.position.y)+"\n")
            f.write("rz="+str(self.pose_amcl.pose.pose.orientation.z)+"\n")
            f.write("rww="+str(self.pose_amcl.pose.pose.orientation.w)+"\n")
            f.close()
        with open('/home/xavier/catkin_ws/src/pitakuru/config/initodom.txt','w') as f:
            f.write("x="+str(self.odom_pose.pose.pose.position.x)+"\n")
            f.write("y="+str(self.odom_pose.pose.pose.position.y)+"\n")
            f.write("rz="+str(self.odom_pose.pose.pose.orientation.z)+"\n")
            f.write("rww="+str(self.odom_pose.pose.pose.orientation.w)+"\n")
            f.close()


    def read_vars(self):
        ffile = open('/home/xavier/catkin_ws/src/pitakuru/config/initpose.txt','r').read()
        variable = "x"
        ini = ffile.find(variable)+(len(variable)+1)
        rest = ffile[ini:]
        search_enter = rest.find('\n')
        self.xini = float(rest[:search_enter])

        variable = "y"
        ini = ffile.find(variable)+(len(variable)+1)
        rest = ffile[ini:]
        search_enter = rest.find('\n')
        self.yini = float(rest[:search_enter])

        variable = "rz"
        ini = ffile.find(variable)+(len(variable)+1)
        rest = ffile[ini:]
        search_enter = rest.find('\n')
        self.zrini = float(rest[:search_enter])

        variable = "rww"
        ini = ffile.find(variable)+(len(variable)+1)
        rest = ffile[ini:]
        search_enter = rest.find('\n')
        self.wrini = float(rest[:search_enter])

        self.init_pose.header.frame_id = "map"
        self.init_pose.pose.pose.position.x = self.xini
        self.init_pose.pose.pose.position.y = self.yini
        self.init_pose.pose.pose.orientation.z = self.zrini
        self.init_pose.pose.pose.orientation.w = self.wrini
        print ("xini:",self.xini)
        print ("yini:",self.yini)
        print ("zini:",self.zrini)
        print ("wini:",self.wrini)
    def read_button(self, joy):

        (circle, triangle, square, cross,l1,r1,pad) = (False, False, False, False,False,False,False)
        button = joy.buttons
        if self.use_ps4_controller:
            if len(button) < 4:
                return (circle, triangle, square, cross,l1,r1,pad)
            if button[1]:
                cross = True
            if button[2]:
                circle = True
            if button[3]:
                triangle = True
            if button[0]:
                square = True
            if button[4]:
                l1 = True
            if button[5]:
                r1 = True
            if button[13]:
                pad = True
        else:
            if len(button) < 4:
                return (circle, triangle, square, cross,l1,r1,pad)
            if button[2]:
                cross = True
            if button[3]:
                circle = True
            if button[1]:
                triangle = True
            if button[0]:
                square = True
            if button[4]:
                l1 = True
            if button[5]:
                r1 = True
            if button[9]:
                pad = True #joystick button r3


        return (circle, triangle, square, cross,l1,r1,pad)

    def update_tf(self):
        
        if(self.gmap_running):
            self.listener.waitForTransform("/map", "/base_link", rospy.Time(), rospy.Duration(25.0))
            try:
                now = rospy.Time.now()
                self.listener.waitForTransform("/map", "/base_link", now, rospy.Duration(25.0))
                (trans,rot) = self.listener.lookupTransform("/map", "/base_link", now)
                self.actual_tf.header.frame_id = "map"
                self.actual_tf.pose.pose.position.x = trans[0]
                self.actual_tf.pose.pose.position.y = trans[1]
                self.actual_tf.pose.pose.position.z = trans[2]
                self.actual_tf.pose.pose.orientation.x = rot[0]
                self.actual_tf.pose.pose.orientation.y = rot[1]
                self.actual_tf.pose.pose.orientation.z = rot[2]
                self.actual_tf.pose.pose.orientation.w = rot[3]
            except (tf.LookupException, tf.ConnectivityException):
                print("fallo")
        else:
            if(time.time() - self.last_time > 1.0):
                self.write_vars()

    def joy_callback(self, joy):

        (circle, triangle, square, cross, l1, r1,pad) = self.read_button(joy)
        
        if l1:
            print("l1")

            if(self.gmap_running):
                msg=String()
                msg.data="reset"
                self.pub_sys.publish(msg)
                print("reseted")
                sleep(0.2)
            else:
                if self.amcl_running:
                    subprocess.call(["rosnode","kill","/amcl"])
                    print("killed amcl")
                    self.amcl_running=False
                    sleep(0.2)
                    subprocess.call(["rosnode","kill","/map_server"])
                    sleep(0.15)
                self.gmap_running=True
                print("launching gmapping")
                subprocess.Popen(["roslaunch", "pitakuru", "gmapping.launch"])
                print("launched gmapping")
                sleep(0.2)

        elif r1:
            print("r1")
            if(self.gmap_running):
                self.gmap_running=False
                os.system('rosrun map_server map_saver -f "/home/xavier/catkin_ws/src/pitakuru/maps/map"')
                print("saved map")
                self.saved_pose=self.actual_tf
                print(self.saved_pose)
                sleep(0.5)
                subprocess.call(["rosnode","kill","/slam_gmapping"])
                print("killed slam")
                if self.amcl_running==False:
                    self.amcl_running=True
                    subprocess.Popen(["roslaunch","pitakuru","amcl.launch"])
                    print("started amcl")
                    sleep(15.0)
                    self.pub_init_pose.publish(self.saved_pose)                    
        else:
            return
            



    def getButton(self,name):
        return self.button_states[name]

if __name__ == "__main__":
    obj_gmap_amcl = GmapAmcl()
    ROS_RATE = 10
    R = rospy.Rate(ROS_RATE)
    while not rospy.is_shutdown():
        obj_gmap_amcl.update_tf()
        R.sleep()
