#!/usr/bin/env python
# coding: utf-8
import json
import serial
import os
import rospy
import subprocess
from pitakuru.msg import State, TriggerAction
from std_msgs.msg import Int16,Float32
from sensor_msgs.msg import Joy
from pitakuru.msg import TriggerAction

class SwitchInput(object):
    def __init__(self):
        rospy.init_node('gmap_amcl')
        self.sub = rospy.Subscriber('/j0/joy', Joy, self.callback)
        #self.ser = serial.Serial(rospy.get_param('/switch/port_name'), rospy.get_param('/switch/baudrate'), timeout=rospy.get_param('/switch/timeout'))
        self.ser = serial.Serial('/dev/serial/by-id/usb-Arduino_LLC_Arduino_Micro-if00', 115200, timeout=0.1)
        self.button_states = dict()
        self.current_bumper = 1 
        self.volts=0

        #self.sub = rospy.Subscriber('state', State, self.callback)
        
        rospy.on_shutdown(self.shutdown)
        self.alert = 0
        self.mode = 2
        self.collision = False
        self.status_on = False
        self.count_status = 0
        self.gpid=0
#//6 collision 5 danger 4 warning 3 karugamo 2 idle 1 manual
#//8 peop follow 6 collision 5 danger 4 warning 3 nothing 2 idle 1 manual with sound
#//78 peop follow 6 collision 75 danger 74 warning 73 nothing 72 idle 71 manual no sound


    def read_button(self, joy):
        (circle, triangle, square, cross,l1,r1) = (False, False, False, False)
        button = joy.buttons
        if len(button) < 4:
            return (circle, triangle, square, cross)
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
            
        return (circle, triangle, square, cross,l1,r1)

    def callback(self, joy):
        # (r, u, l, d) = self.read_axes(joy)
        #trigger_action = TriggerAction()
        #(circle, triangle, square, cross) = self.read_button(joy)
        (circle, triangle, square, cross, l1, r1) = self.read_button(joy)
        if l1:
            print("l1")
            subprocess.call(["roslaunch", "pitakuru", "pitakuru_full_yolo_mbf.launch"])
            #subprocess.call(["/home/xavier/pow_off.sh"])
            rospy.logerr("matando desde on")
        elif r1:
            print("r1")
        else:
            return
        self.pub.publish(trigger_action)

    def alerts_cb(self,data):
        self.mode=data.data
       

    def request_current_state(self):
        self.ser.write(b'7')

    #def callback(self, state):
        #self.set_LED_color(state)

    def shutdown(self):
        rospy.logwarn("shutting down switch node")
        #self.set_LED_color()
        
    
    
    
                subprocess.call(["roslaunch", "pitakuru", "pitakuru_full_yolo_mbf.launch"])
                #subprocess.call(["/home/xavier/pow_off.sh"])
                rospy.logerr("matando desde on")
                #os.system('sudo systemctl poweroff')
        #else:
        #    self.count_status=0
        if(self.button_states["karugamo"] == 1 and self.status_on):
        # if(self.button_states["karugamo"] == 1):
            self.count_status=self.count_status+1
            if(self.count_status>2):
                #os.system("shutdown /s /t 1")
                #request_current_state()
                self.shutdown()
                os.system('systemctl poweroff')
                self.status_on=False

        trigger_action = TriggerAction()
        rospy.logerr(self.button_states)
        if self.button_states["break"] == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_COLLISION
        if self.button_states["release"] == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_BREAK_RELEASE_BUTTON_ON
        if self.button_states["karugamo"] == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_KARUGAMO_BUTTON_ON
        if self.button_states["idle"] == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_IDLE_BUTTON_ON
        if not trigger_action.trigger:
            trigger_action.trigger = TriggerAction.TRIGGER_IDLE_BUTTON_ON#TRIGGER_BREAK_RELEASE_BUTTON_ON
        self.pub.publish(trigger_action)

    def getButton(self,name):
        return self.button_states[name]

    #def set_LED_color(self, state=State):
        #if state.state == State.STATE_ACTIVE_KARUGAMO and self.alert != 1:
            # rgb = 110 (yellow)
            ##self.ser.write(b'6')
        #elif state.state == State.STATE_IDLE and self.alert != 1:
            # rgb = 010 (green)
            ##self.ser.write(b'2')
        #elif state.state == State.STATE_ACTIVE_MANUAL and self.alert != 1:
            # rgb = 001 (blue)
            ##self.ser.write(b'1')
        #elif state.state == State.STATE_ERROR_OBSTACLE or self.mode == 5:
            # rgb = 101 (violet)
            ##self.ser.write(b'5')
        #elif state.state == State.STATE_ERROR_COLLISION:
            # rgb = 100 (red)
            ##self.ser.write(b'4')
        #else:
            # rgb = 000 (off)
            ##self.ser.write(b'0')


if __name__ == "__main__":
    switch_input = SwitchInput()
    switch_input.request_current_state()
    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        switch_input.update()
        R.sleep()
