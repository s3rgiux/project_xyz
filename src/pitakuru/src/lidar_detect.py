#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy
from sensor_msgs.msg import LaserScan
import numpy as np
import time
from time import sleep
import subprocess
import socket

class lidar_detect:

    def __init__(self):
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.callbackLaser)
        self.addr = ('172.16.0.10', 10940) #: IP address and port of the scanner
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timeout = 5
        self._sock.settimeout(self.timeout)
        rospy.on_shutdown(self.shutdown)
        sleep(10.0)
        print("connected")
        self.start_time = time.time()
        self.last_time = time.time()
    
    def pubobs(self):
        if(time.time()-self.last_time>0.7):
            print("trying to reboot")
            subprocess.call(["rosnode","kill","/urg_node"])
            sleep(0.7)
            subprocess.call(["python","/home/xavier/catkin_ws/src/urg_node/scripts/set_urg_ip_sergio.py","--ip","172.16.0.10","172.16.0.10","172.16.0.1"])
            print("kill_node")
            subprocess.call(["roslaunch","pitakuru","hokuyo_only.launch"])
            sleep(14.0)
            self.start_time = time.time()
            self.last_time = time.time()

    def callbackLaser(self,msg):
        self.last_time = time.time()
    
    def shutdown(self):
        subprocess.call(["rosservice","call","/stop_motor"])

def main(args):
    rospy.init_node('lidar_detect', anonymous=True)
    lidar_obj = lidar_detect()
    while not rospy.is_shutdown():
        lidar_obj.pubobs()
        sleep(0.02)

if __name__ == '__main__':
    main(sys.argv)
