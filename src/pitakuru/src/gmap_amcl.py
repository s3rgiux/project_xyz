#!/usr/bin/env python
# coding: utf-8
import json
import serial
import os
import rospy
import subprocess
from pitakuru.msg import State, TriggerAction
from std_msgs.msg import Int16,Float32,String
from sensor_msgs.msg import Joy
from pitakuru.msg import TriggerAction
from time import sleep

import signal

class SwitchInput(object):
    def __init__(self):
        rospy.init_node('gmap_amcl')
        self.sub = rospy.Subscriber('/j0/joy', Joy, self.callback,queue_size=1)
        #self.ser = serial.Serial(rospy.get_param('/switch/port_name'), rospy.get_param('/switch/baudrate'), timeout=rospy.get_param('/switch/timeout'))
        self.ser = serial.Serial('/dev/serial/by-id/usb-Arduino_LLC_Arduino_Micro-if00', 115200, timeout=0.1)
        self.pub_sys = rospy.Publisher('/syscommand', String, queue_size=1)
        self.button_states = dict()
        self.current_bumper = 1
        self.volts=0

        #self.sub = rospy.Subscriber('state', State, self.callback)
        
        #rospy.on_shutdown(self.shutdown)
        self.alert = 0
        self.mode = 2
        self.collision = False
        self.status_on = False
        self.count_status = 0
        self.gpid=0
        self.gmap_running=True

    def read_button(self, joy):
        (circle, triangle, square, cross,l1,r1,pad) = (False, False, False, False,False,False,False)
        button = joy.buttons
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
            
        return (circle, triangle, square, cross,l1,r1,pad)

    def callback(self, joy):
        # (r, u, l, d) = self.read_axes(joy)
        #trigger_action = TriggerAction()
        #(circle, triangle, square, cross) = self.read_button(joy)
        (circle, triangle, square, cross, l1, r1,pad) = self.read_button(joy)
        if pad:
            if self.gmap_running == False:
                self.gmap_running=True
                #subprocess.call(["roslaunch", "pitakuru", "gmapping.launch"])
                subprocess.Popen(["roslaunch", "pitakuru", "gmapping.launch"])
                self.gmap_running=False
                sleep(0.2)
        elif l1:
            print("l1")
            #subprocess.call(["roslaunch", "pitakuru", "pitakuru_full_yolo_mbf.launch"])
            #subprocess.call(["rostopic","pub","1","/syscommand","std_msgs/String",""data: 'reset'""])
            #os.system('rostopic pub -1 /syscommand std_msgs/String "data: reset"')
            if(self.gmap_running):
                msg=String()
                msg.data="reset"
                self.pub_sys.publish(msg)
                print("succeded")
                sleep(0.2)
            # else:
            #     self.gmap_running=True
            #     #subprocess.call(["roslaunch", "pitakuru", "gmapping.launch"])
            #     subprocess.Popen(["roslaunch", "pitakuru", "gmapping.launch"])
            #     self.gmap_running=False
            #     sleep(0.2)
            #subprocess.call(["/home/xavier/pow_off.sh"])
            #rospy.logerr("matando desde on")
        elif r1:
            print("r1")
            if(self.gmap_running):
                self.gmap_running=False
                os.system('rosrun map_server map_saver -f "/home/xavier/catkin_ws/src/pitakuru/maps/map"')
                sleep(0.5)
                subprocess.call(["rosnode","kill","/slam_gmapping"])
        else:
            return
        #self.pub.publish(trigger_action)


   

   

    def getButton(self,name):
        return self.button_states[name]

    

if __name__ == "__main__":
    switch_input = SwitchInput()
    #switch_input.request_current_state()
    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        #switch_input.update()
        R.sleep()
