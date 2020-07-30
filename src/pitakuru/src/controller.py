#!/usr/bin/env python
# coding: utf-8
import rospy

from sensor_msgs.msg import Joy
from pitakuru.msg import TriggerAction


# "Two-Wheel Drive" 
class PS4Controller: 
    def __init__(self):
        rospy.init_node('PS4Controller', log_level=rospy.INFO)
        self.sub = rospy.Subscriber('/j0/joy', Joy, self.callback)
        self.pub = rospy.Publisher('trigger_action', TriggerAction, queue_size=1)
    
    def read_button(self, joy):
        (circle, triangle, square, cross) = (False, False, False, False)
        button = joy.buttons
        if len(button) < 4:
            return (circle, triangle, square, cross)
        if button[1]:
            circle = True
        elif button[2]:
            triangle = True
        elif button[3]:
            square = True
        elif button[0]:
            cross = True
        return (circle, triangle, square, cross)

    def callback(self, joy):
        # (r, u, l, d) = self.read_axes(joy)
        trigger_action = TriggerAction()
        (circle, triangle, square, cross) = self.read_button(joy)
        # マニュアルモード
        if circle:
            trigger_action.trigger = TriggerAction.TRIGGER_REMOTE_MANUAL_BUTTON_ON
        # 待機モード
        elif triangle:
            trigger_action.trigger = TriggerAction.TRIGGER_REMOTE_IDLE_BUTTON_ON
        # カルガモモード
        elif square:
            trigger_action.trigger = TriggerAction.TRIGGER_REMOTE_KARUGAMO_BUTTON_ON
        else:
            return
        self.pub.publish(trigger_action)

if __name__ == '__main__':
    ps4_ctrl = PS4Controller()
    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        R.sleep()
