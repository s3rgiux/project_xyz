#!/usr/bin/env python
# coding: utf-8

import math
import time

import rospy
from sensor_msgs.msg import Joy
from pitakuru.msg import DriveWheel, State



class ManualMovement(object):
    def __init__(self):
        rospy.init_node('ManualMovement')
        self.joy_sub = rospy.Subscriber('movement/manual/joy', Joy, callback=self.receive_joy)
        self.pub = rospy.Publisher('drive_wheel_desired', DriveWheel, queue_size=1)

    def receive_joy(self, joy):
        axes = joy.axes
        (ud, lr) = (axes[7], axes[6])
        max_ud = rospy.get_param('/manual/max_ud')
        max_lr = rospy.get_param('/manual/max_lr')
        if ud != 0.0:
            msg = DriveWheel(ud*max_ud, ud*max_ud)
            self.pub.publish(msg)
        elif lr != 0.0:
            msg = DriveWheel(-lr*max_lr, lr*max_lr)
            self.pub.publish(msg)
        else:
            msg = DriveWheel(0.0, 0.0)
            self.pub.publish(msg)


if __name__ == '__main__':
    manual = ManualMovement()

    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        R.sleep()