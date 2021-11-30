#!/usr/bin/env python
# coding: utf-8

import math
import time

import rospy
from fiducial_msgs.msg import FiducialTransformArray
from sensor_msgs.msg import Joy
from pitakuru.msg import DriveWheel, State
from std_msgs.msg import String,Float32


class KarugamoMovement(object):
    eI = 0.0
    theta_old = 0.0
    last_received = None

    is_current_mode = False

    left_joy_interrupt = 0.0
    right_joy_interrupt = 0.0

    max_speed_rpm = rospy.get_param('/karugamo/max_speed_rpm')
    speed_p = rospy.get_param('/karugamo/speed_p')
    steer_p = rospy.get_param('/karugamo/steer_p')
    steer_i = rospy.get_param('/karugamo/steer_i')
    steer_d = rospy.get_param('/karugamo/steer_d')
    interrupt_rpm = rospy.get_param('/karugamo/joy_interrupt_rpm')
    WAIT_TIME = rospy.get_param('pitakuru/wait_time')

    def __init__(self):
        rospy.init_node('KarugamoMovement')
        self.state_sub = rospy.Subscriber('state', State, callback=self.receive_state)
        self.fiducial_sub = rospy.Subscriber('movement/karugamo/fiducial_transforms', FiducialTransformArray, callback=self.receive_target)
        self.joy_sub = rospy.Subscriber('movement/karugamo/joy', Joy, callback=self.receive_joy)
        self.ang_pub = rospy.Publisher("peopAng",Float32, queue_size=1)
        self.dist_pub = rospy.Publisher("peopDist",Float32, queue_size=1)
        self.pub = rospy.Publisher('drive_wheel_desired', DriveWheel, queue_size=1)
        self.last_received = rospy.get_time()
        self.angulo= Float32()
        self.distancia= Float32()
	self.changed=False
        self.dist = -1
        self.theta = -500

    def receive_state(self, state):
        self.is_current_mode = (state.state == State.STATE_ACTIVE_KARUGAMO)

    def receive_target(self, fiducials):
        transforms = fiducials.transforms
        if len(transforms) == 0:
            return
        transform = transforms[0]
        trans = transform.transform.translation
        self.dist = math.sqrt(trans.x**2 + trans.z**2)
        self.theta = -math.atan2(trans.z, trans.x)
        if self.theta > math.pi:
            self.theta -= 2 * math.pi
        if self.theta < -math.pi:
            self.theta += 2 * math.pi
        self.angulo.data=(self.theta*180/math.pi)+90
        self.distancia.data=self.dist
        left_rpm, right_rpm = self.pid(self.dist, self.theta)
        #drive_wheel = DriveWheel(left_rpm=left_rpm, right_rpm=right_rpm)
	self.pub_res()
        #self.pub.publish(drive_wheel)

    def pub_res(self):
        
        self.ang_pub.publish(self.angulo)
        self.dist_pub.publish(self.distancia)

    def thresh_theta(self, theta):
        if theta > math.pi:
            return theta - 2*math.pi
        return theta
    
    def pid(self, distance, angle):
        theta = self.thresh_theta(angle)

        now = rospy.get_time()
        interval = 0.1

        v = min(self.speed_p * distance, self.max_speed_rpm)
        self.eI = self.eI + interval * theta; # Integral

        delta_v = self.steer_p * theta + self.steer_i * self.eI + self.steer_d * (theta - self.theta_old) / interval
        self.theta_old = theta

        left_rpm = v + delta_v + self.left_joy_interrupt # ジョイコンの割り込み
        right_rpm = v - delta_v + self.right_joy_interrupt # ジョイコンの割り込み
        self.last_received = rospy.get_time()
        return (left_rpm, right_rpm)

    def receive_joy(self, joy):
        axes = joy.axes
        # 左右の割り込みのみ対応
        lr = axes[6] # 左:-1, 右:1, 入力なしの場合は0
        self.left_joy_interrupt = -lr*self.interrupt_rpm
        self.right_joy_interrupt = lr*self.interrupt_rpm
    
    def wait(self):
        # 最終コマンド受取時間からどれだけ経ったか
        now = rospy.get_time()
        dt = now - self.last_received
        # 一定時間コマンドを受信しなかった場合
        if (dt > self.WAIT_TIME) and self.is_current_mode:
            self.last_received = rospy.get_time()
            self.angulo.data=-500
            self.distancia.data=-1
	    self.pub_res()
            drive_wheel = DriveWheel(left_rpm=0.0, right_rpm=0.0)
            self.pub.publish(drive_wheel)


if __name__ == '__main__':
    karugamo = KarugamoMovement()

    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        karugamo.wait()
        R.sleep()
