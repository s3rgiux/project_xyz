#!/usr/bin/env python
# coding: utf-8

import rospy
from fiducial_msgs.msg import FiducialTransformArray
from sensor_msgs.msg import Joy
from pitakuru.msg import State, DriveWheel


class Movement(object):
    current_state = State.STATE_IDLE

    def __init__(self):
        rospy.init_node('Movement')
        state_sub = rospy.Subscriber('state', State, callback=self.state_callback)
        joy_sub = rospy.Subscriber('/j0/joy', Joy, callback=self.joy_callback)
        fiducials_sub = rospy.Subscriber('fiducial_transforms', FiducialTransformArray, callback=self.fiducial_callback)

        self.manual_joy_pub = rospy.Publisher('/movement/manual/joy', Joy, queue_size=5)
        self.karugamo_joy_pub = rospy.Publisher('/movement/karugamo/joy', Joy, queue_size=5)
        self.karugamo_fiducials_pub = rospy.Publisher('/movement/karugamo/fiducial_transforms', FiducialTransformArray, queue_size=5)
        self.drive_wheel_pub = rospy.Publisher('drive_wheel_desired', DriveWheel, queue_size=1)
    
    def joy_callback(self, joy):
        if self.current_state == State.STATE_ACTIVE_KARUGAMO:
            self.karugamo_joy_pub.publish(joy)
        elif self.current_state == State.STATE_ACTIVE_MANUAL:
            self.manual_joy_pub.publish(joy)

    def fiducial_callback(self, fiducial):
        if self.current_state == State.STATE_ACTIVE_KARUGAMO:
            self.karugamo_fiducials_pub.publish(fiducial)

    def state_callback(self, state):
        self.current_state = state.state
        msg = DriveWheel(0.0, 0.0)
        self.drive_wheel_pub.publish(msg)


if __name__ == '__main__':
    movement = Movement()

    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        R.sleep()
