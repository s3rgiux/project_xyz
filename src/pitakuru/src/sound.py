#!/usr/bin/env python
# coding: utf-8
import subprocess

import rospy
from pitakuru.msg import State
from std_msgs.msg import Int16


class SoundNode():
    sound_files = {
        "active": rospy.get_param("/active", "./src/pitakuru/assets/AGV_active_3s.wav"),
        "warning": rospy.get_param("/warning", "./src/pitakuru/assets/AGV_warning_3s.wav"),
        "error": rospy.get_param("/error", "./src/pitakuru/assets/AGV_error_5s.wav"),
    }

    def __init__(self):
        rospy.init_node('SoundNode')
        #self.sub = rospy.Subscriber('state', State, self.execute_cb)
	self.sub_alerts = rospy.Subscriber('/alerts', Int16, self.alerts_cb,queue_size=1)
        #self.action.start()
    
    def get_file(self, sound):
        return self.sound_files[sound.type]
	
    def alerts_cb(self,data):
#// 6 collision 5 danger 4 warning 3 karugamo 2 idle 1 manual
        if(data.data==1):
            subprocess.call(["aplay", "/home/xavier/catkin_ws/src/pitakuru/assets/manual-japanese.mp3"])
        elif(data.data==2):
            subprocess.call(["aplay", "/home/xavier/catkin_ws/src/pitakuru/assets/idle-japanese.mp3"])
        #elif(data.data==3):
        #    subprocess.call(["aplay", "/home/xavier/catkin_ws/src/pitakuru/assets/karugamo-japanese.mp3"])
        elif(data.data==4):
            subprocess.call(["aplay", "/home/xavier/catkin_ws/src/pitakuru/assets/AGV_warning_3s.wav"])
        elif(data.data==5):
            subprocess.call(["aplay", "/home/xavier/catkin_ws/src/pitakuru/assets/AGV_warning_3s.wav"])
        elif(data.data==6):
            subprocess.call(["aplay", "/home/xavier/catkin_ws/src/pitakuru/assets/collision.wav"])
        elif(data.data==8):
            subprocess.call(["aplay", "/home/xavier/catkin_ws/src/pitakuru/assets/karugamo-japanese.mp3"])


    #def execute_cb(self, sound):
        #print("DDDDDDDFFFFFFFF")
        #print(sound)
        #filename = self.get_file(sound)
        #subprocess.call(["aplay", filename])
        #self.action.set_succeeded(SoundResult())


if __name__ == '__main__':
    sound_node = SoundNode()
    # 制御周期
    ROS_RATE = 10
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        R.sleep()
