#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import sys,time
from math import sqrt, cos, sin
import rospy
#import tf,tf2_ros
import numpy as np
from time import sleep
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import Float32
from std_msgs.msg import Int16
from std_msgs.msg import *
from geometry_msgs.msg import Point, Vector3, PoseWithCovarianceStamped

from obs_extract.msg import Obstacles


import struct
import time
import rosparam

import roslib

import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from matplotlib import pyplot as plt

import os
import time
import sys


SLEEP_TIME = 0.12


class image_converter:
    def __init__(self):
        print("Peopdetector")
        
        self.obst_pub = rospy.Publisher('peop_detect', Int16, queue_size=1)
        self.image_pub2 = rospy.Publisher("image_topic_3",Image, queue_size=1)
        self.peop  = Float32()
        self.bridge = CvBridge()
        self.detected=0
        self.img
        self.image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback, queue_size=1)
        #self.front_detection = rospy.get_param("/obj_track/front_detection")
        #self.side_detection = rospy.get_param("/obj_track/side_detection")
        #self.timex=0
        #self.last_time=0
    
    def pubobs(self):
        a=0
        #if(time.time()-self.last_time>0.1):
        #if(self.track==0):
            #self.angulo.data=-500
            #self.distancia.data=0
            #self.ang_pub.publish(self.angulo)
            #self.dist_pub.publish(self.distancia)


    def callback2(self,data):
        try:
            self.img = self.bridge.imgmsg_to_cv2(data, "mono8")
          
            try:
                self.image_pub2.publish(self.bridge.cv2_to_imgmsg(self.img, "mono8"))
            except CvBridgeError as e:
                print(e)
     
        except CvBridgeError as e:
            print(e)
    

    def shutdown(self):
        rospy.sleep(1)
        

def ic_main():
    rospy.init_node('image_converte', anonymous = True)
    ic = image_converter()

    while not rospy.is_shutdown():
        ic.pubobs()
        sleep(SLEEP_TIME)

if __name__=='__main__':
    ic_main()

