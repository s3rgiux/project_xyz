#!/usr/bin/env python
# coding: utf-8
import json
import serial
import os
import rospy
import subprocess
from pitakuru.msg import TriggerAction
from time import sleep

class SwitchInputOn(object):
    def __init__(self):
        rospy.init_node('PitakuruState')
        self.ser = serial.Serial('/dev/serial/by-id/usb-Arduino_LLC_Arduino_Micro-if00', 115200, timeout=0.1)
        self.button_states = dict()
        self.current_bumper = 1 
        self.volts = 0
        self.pub = rospy.Publisher('trigger_action', TriggerAction, queue_size=2)
        rospy.on_shutdown(self.shutdown)
        self.alert = 0
        self.status_on = False
        self.counter_to_power_on = 0

    def request_current_state(self):
        self.ser.write(b'7')

    def shutdown(self):
        rospy.logwarn("shutting down switch node")
        self.ser.write(b'0')
        self.ser.close()
    
    def update(self):
        current_states_str = self.ser.readline()
        if not current_states_str:
            return

        current_states = json.loads(current_states_str)
        #if Black button pressed
        if(current_states['A1'] < 200 and self.status_on == False):
            self.counter_to_power_on = self.counter_to_power_on+1
            if(self.counter_to_power_on>0):
                self.status_on = True
                self.counter_to_power_on = 0
                rospy.logerr("starting")
                subprocess.call(["roslaunch", "pitakuru", "pitakuru_full_yolo_mbf.launch"])
                rospy.logerr("matando desde on")

if __name__ == "__main__":
    switch_input = SwitchInputOn()
    sleep(0.01)
    switch_input.request_current_state()
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    while not rospy.is_shutdown():
        switch_input.update()
        R.sleep()
