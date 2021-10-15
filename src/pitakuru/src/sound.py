#!/usr/bin/env python
# coding: utf-8
import subprocess
import rospy
from pitakuru.msg import State
from std_msgs.msg import Int16
import os
import signal

class SoundNode():

    def __init__(self):
        rospy.init_node('SoundNode')
	self.sub_alerts = rospy.Subscriber('/alerts', Int16, self.alerts_cb,queue_size=1)
        self.entered = False
        self.cancel = False
        self.gpid = 0
	
    def alerts_cb(self,data):
#// 6 collision 5 danger 4 warning 3 karugamo 2 idle 1 manual
#//8 peop follow 6 collision 5 danger 4 warning 3 nothing 2 idle 1 manual

        if(data.data == 1):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/manual-japanese.mp3"
            self.entered=True
        elif(data.data == 2):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/idle-japanese.mp3"
            self.entered=True
        elif(data.data == 4):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/AGV_warning_3s.wav"
            self.entered=True
        elif(data.data == 5):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/AGV_warning_3s.wav"
            self.entered=True
        elif(data.data == 6):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/collision-japanese.mp3"
            self.entered=True
        elif(data.data == 8):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/karugamo-japanese.mp3"
            self.entered=True
        elif(data.data == 101):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/speed-1-japanese.mp3"
            self.entered=True
        elif(data.data == 102):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/speed-2-japanese.mp3"
            self.entered=True
        elif(data.data == 103):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/speed-3-japanese.mp3"
            self.entered=True
        elif(data.data == 104):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/speed-4-japanese.mp3"
            self.entered=True
        elif(data.data == 105):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/speed-5-japanese.mp3"
            self.entered=True
        elif(data.data == 106):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/karugamo-waypoint-japanese.mp3"
            self.entered=True
        elif(data.data == 107):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/danger-mode-japanese2.mp3"
            self.entered=True
        elif(data.data == 108):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/low-battery-japanese.mp3"
            self.entered=True
        elif(data.data == 109):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/karugamo-lost-japanese2.mp3"
            self.entered=True
        elif(data.data == 110):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/karugamo-searching.mp3"
            self.entered=True
        elif(data.data == 111):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/autopilot-japanese.mp3"
            self.entered=True
        elif(data.data == 112):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/arrived-1st-japanese.mp3"
            self.entered=True
        elif(data.data == 113):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/arrived-2nd-japanese.mp3"
            self.entered=True
        elif(data.data == 114):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/AGV_warning_3s.wav"
            self.entered=True
        elif(data.data == 115):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/AGV_warning_3s.wav"
            self.entered=True
        elif(data.data == 116):
            self.route="/home/xavier/catkin_ws/src/pitakuru/assets/AGV_warning_3s.wav"
            self.entered=True
        elif(data.data == 117):
            self.route = "/home/xavier/catkin_ws/src/pitakuru/assets/AGV_warning_3s.wav"
            self.entered = True
        elif(data.data == 118):
            self.route = "/home/xavier/catkin_ws/src/pitakuru/assets/careful.mp3"
            self.entered = True

        if(self.entered):
            try: 
                if(self.gpid is not 0):
                    os.kill(self.gpid, signal.SIGTERM) # Kill pprevious sound
            except:
                print('cant get pid') 
            self.entered = False
            try:
                p = subprocess.Popen(["play", self.route])
                self.gpid = p.pid
            except:
                print('cant play')

if __name__ == '__main__':
    sound_node = SoundNode()
    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        R.sleep()
