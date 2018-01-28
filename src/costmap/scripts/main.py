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
from geometry_msgs.msg import Point, Vector3, PoseWithCovarianceStamped


nx=np.zeros(360,dtype=np.float)
ny=np.zeros(360,dtype=np.float)

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("imageborders",Image, queue_size=1)
    self.cost1_pub = rospy.Publisher("cost1",Image, queue_size=1)
    self.cost2_pub = rospy.Publisher("cost2",Image, queue_size=1)
    self.bord1_pub = rospy.Publisher("bord1",Image, queue_size=1)
    self.bord2_pub = rospy.Publisher("bord2",Image, queue_size=1)
    self.crop_pub = rospy.Publisher("crop",Image, queue_size=1)
    self.cost_pub = rospy.Publisher("costdetect",Vector3, queue_size=1)
    self.ang_pub = rospy.Publisher("peopAng2",Float32, queue_size=1)
    self.dist_pub = rospy.Publisher("peopDist2",Float32, queue_size=1)
    self.bridge = CvBridge()
    self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.callbackLaser,queue_size=1)
    self.dilation = rospy.get_param("/cost_detect/dilation")
    self.angulo= Float32()
    self.distancia= Float32()
    self.cost_d= Vector3()
    self.sang=90
    self.lon=100
    self.fin_ang=90
    self.fin_lon=0.4
    self.people=False
    self.mask=np.array([[-1, -2, -3, 0, 0, 0, 0, 3 , 2 , 1 ],
                        [-1, -2, -3, 0, 0, 0, 0, 3 , 2 , 1 ],
                        [-1, -2, -3, 0, 0, 0, 0, 3 , 2 , 1 ],
                        [-1, -2, -3, 0, 0, 0, 0, 3 , 2 , 1 ],
                        [-1, -2, -3, 0, 0, 0, 0, 3 , 2 , 1 ],
                        [-1, -2, -3, 0, 0, 0, 0, 3 , 2 , 1 ],
                        [-1, -2, -3, 0, 0, 0, 0, 3 , 2 , 1 ],
                        [-1, -2, -3, 0, 0, 0, 0, 3 , 2 , 1 ],
                        [-1, -2, -3, 0, 0, 0, 0, 3 , 2 , 1 ],
                        [-1, -2, -3, 0, 0, 0, 0, 3 , 2 , 1 ]])
    self.mask2=np.array([[-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ]])


    self.mask3=np.array([[-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-1, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 1 ],
                        [-1, -2, -2, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ]])
    
    self.mask4=np.array([[-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 3 ],
                        [-1, -3, -3, -3, -4, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 4, 3, 3, 3, 1 ],
                        [-1, -2, -2, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4 , 4 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -2, -2, -3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3 , 3 , 3, 3, 2, 2, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ],
                        [-1, -1, -1, -2, -2, -2, -3, 0, 0, 0, 0, 0, 0, 3 , 2 , 2, 2, 1, 1, 1 ]])
    
    self.mask6=np.array([[-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ]])

    self.mask7=np.array([[-7, -7, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 7, 7 ],
                        [-7, -7, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 7, 7 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3,-3, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4, 4, 3 , 3 , 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3,-3, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4, 4, 3 , 3 , 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3,-3, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4, 4, 3 , 3 , 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3,-3, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4, 4, 3 , 3 , 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3,-3, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4, 4, 3 , 3 , 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3,-3, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4, 4, 3 , 3 , 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3,-3, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4, 4, 3 , 3 , 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3,-3, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4, 4, 3 , 3 , 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3,-3, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4, 4, 3 , 3 , 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3,-3, -3, -3, -4, -4, 0, 0, 0, 0, 0, 0, 4, 4, 3 , 3 , 3, 3, 3, 3, 3, 3 ]])

    self.mask8=np.array([[-5, -5, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 5, 5 ],
                        [-5, -5, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 5, 5 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3 ]])
    #print(self.mask)
    #print(self.mask)
    #print(self.mask+self.mask)

  

  
  def callbackLaser(self,msg):
    c=0
    angle=-3.12413907051
    mul=20
    #img = np.zeros((240, 320), dtype = "uint8")
    img = np.zeros((158, 211), dtype = "uint8")

    cost1 = np.zeros((240, 320), dtype = "uint8")
    cost2 = np.zeros((240, 320), dtype = "uint8")
    bord1 = np.ones((158, 211), dtype = "uint8")
    centery=138
    centerx=105
    for i, theta in enumerate(np.arange(msg.angle_min,msg.angle_max,msg.angle_increment)):
      if not np.isinf(msg.ranges[i]) and msg.ranges[i]>0.15 and msg.ranges[i] < 3.7:
        y=round(msg.ranges[i]*np.cos(theta)*125/3.7,0)
        x=round(msg.ranges[i]*np.sin(theta)*104/3.7,0)
        img[centery-int(y),centerx-int(x)]=255
        bord1[centery-int(y),centerx-int(x)]=255
    kernel = np.ones((3,3),np.uint8)
    dil = cv2.dilate(img,kernel,iterations = 1)
    cost1 = cv2.dilate(dil,kernel,iterations = 2)
    cost2 = cv2.dilate(cost1,kernel,iterations = self.dilation)

    
    # find contours in the thresholded image
    cnts = cv2.findContours(cost2, cv2.RETR_EXTERNAL,
	                          cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    #M = cv2.moments(cnts[0])
    #cX = int(M["m10"] / M["m00"])
    #cY = int(M["m01"] / M["m00"])
    # draw the contour and center of the shape on the image
    #res=self.mask2*crop_img
    #crop_img = cost2[centery-10:centery+10, centerx-10:centerx+10]
    ncentery=120
    ncenterx=105
    crop_img = cost2[ncentery-20:ncentery+20, ncenterx-13:ncenterx+13]
    res=self.mask8*crop_img
    #rospy.logerr(np.sum(res))
    #print(np.sum(res)/76245)#/58140.0)
    self.cost_d.x=np.sum(res)/271320.0#/222870.0#/222360.0#/222870.0#/122145.0#/76245.0#/58140.0
    self.cost_pub.publish(self.cost_d)

    bord1=bord1*255
    for c in cnts:
      cv2.drawContours(bord1, [c], -1, (0, 0, 0), 2)
      #cv2.drawContours(bord1, [c], -1, (255, 255, 255), 1)
    #cv2.circle(dil, (cX, cY), 5, (255, 255, 255), -1)
    #cv2.imshow("new",dil)
    # find contours in the thresholded image
    cnts = cv2.findContours(cost1.copy(), cv2.RETR_EXTERNAL,
	                          cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
      cv2.drawContours(bord1, [c], -1, (0, 0, 0), 1)
      #cv2.drawContours(bord1, [c], -1, (255, 255, 255), 2)
    # Start coordinate, here (5, 5) 
    # represents the top left corner of rectangle 
    size_robot=20
    start_point = (centerx-size_robot, centery-size_robot) 
    # Ending coordinate, here (220, 220) 
    # represents the bottom right corner of rectangle 
    end_point = (centerx+size_robot, centery+size_robot) 
    # Blue color in BGR 
    color = (0, 0, 0) 
    # Line thickness of 2 px 
    thickness = 1  
    # Using cv2.rectangle() method 
    # Draw a rectangle with blue line borders of thickness of 2 px 
    cv2.rectangle(bord1, start_point, end_point, color, thickness) 
  
    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(dil, "mono8"))
      self.cost1_pub.publish(self.bridge.cv2_to_imgmsg(cost1, "mono8"))
      self.cost2_pub.publish(self.bridge.cv2_to_imgmsg(cost2, "mono8"))
      self.bord1_pub.publish(self.bridge.cv2_to_imgmsg(bord1, "mono8"))
      self.crop_pub.publish(self.bridge.cv2_to_imgmsg(crop_img, "mono8"))
    except CvBridgeError as e:
      print(e) 


def main(args):
  rospy.init_node('image_converter', anonymous=True)
  ic = image_converter()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
