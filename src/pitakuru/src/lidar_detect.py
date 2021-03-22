#!/usr/bin/env python

from __future__ import print_function
import roslib
#roslib.load_manifest('opencv_test_python')
import sys
import rospy
import cv2
from std_msgs.msg import String,Float32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import LaserScan
import numpy as np
from matplotlib import pyplot as plt
import imutils
import time
from time import sleep
import subprocess
nx=np.zeros(360,dtype=np.float)
ny=np.zeros(360,dtype=np.float)


import socket
from codecs import encode, decode



class image_converter:

    def __init__(self):
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.callbackLaser)
        
        self.addr = ('172.16.0.10', 10940) #: IP address and port of the scanner
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timeout=5
        self._sock.settimeout(self.timeout)
        #self._sock.connect(self.addr)
        #self.sock = socket.socket()
        #self.sock.connect(('176.16.0.10', 10940))
        sleep(14.0)
        print("connected")
        self.start_time=time.time()
        self.last_time=time.time()
    
    def pubobs(self):
        #if(time.time()-self.start_time>10):
        if(time.time()-last_time>1):
            print("trying to reboot")
            #n = self._sock.send(encode('RB', 'ascii') + b'\n'+encode('RB', 'ascii') + b'\n')
            subprocess.call(["python","/home/xavier/catkin_ws/src/urg_node/scripts/set_urg_ip_sergio.py","--ip","172.16.0.10","172.16.0.10","172.16.0.1"])
            sleep(6.0)
            self.start_time=time.time()
            self.last_time=time.time()
        """ if(time.time()-self.last_time>0.4):
            print("fail_lidar")
            req= 'RS'
            n = self._sock.send(encode(req, 'ascii') + b'\n')
            if len(req) + 1 != n:
                print("fail to send to hokuyo")#raise HokuyoException('Failed to send all data to the sensor')
            #return req
            sleep(5.0)
            self.last_time=time.time() """

    def callbackLaser(self,msg):
        self.last_time=time.time()
        """ c=0
        angle=-3.12413907051
        mul=20
        img = np.zeros((240, 320), dtype = "uint8") """
        #img = 0*np.ones((500, 500, 1), dtype = "uint8")
        """ for i, theta in enumerate(np.arange(msg.angle_min,msg.angle_max,msg.angle_increment)):
            if i<35 or i>324:
            if not np.isinf(msg.ranges[i]) and msg.ranges[i]>0.15 and msg.ranges[i] < 1.5:
                y=round(msg.ranges[i]*np.cos(theta)*210/1.5,0)
                x=round(msg.ranges[i]*np.sin(theta)*210/1.5,0)
                img[240+int(y),160+int(x)]=255 """
    


def main(args):
    rospy.init_node('image_converter', anonymous=True)
    ic = image_converter()
    while not rospy.is_shutdown():
        ic.pubobs()
        sleep(0.02)

if __name__ == '__main__':
    main(sys.argv)
