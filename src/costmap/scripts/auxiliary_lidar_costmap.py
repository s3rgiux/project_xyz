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
from geometry_msgs.msg import Twist, Pose, TransformStamped,Quaternion
from geometry_msgs.msg import Point, Vector3, PoseWithCovarianceStamped


nx = np.zeros(360,dtype=np.float)
ny = np.zeros(360,dtype=np.float)

COSTMAP_HEIGHT = 158
COSTMAP_WIDTH = 211
OFFSET_COSMAP_X = 105
OFFSET_COSMAP_Y = 138
MIN_ANGLE = -3.1415 / 2
MAX_ANGLE = 3.1415 / 2
LIMIT_MIN_X = 0.15
LIMIT_MAX_X = 3.7
PI = 3.1415

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("imageborders_aux",Image, queue_size=1)
    self.cost1_pub = rospy.Publisher("cost1_aux",Image, queue_size=1)
    self.cost2_pub = rospy.Publisher("cost2_aux",Image, queue_size=1)
    self.border_lidar_matrix_pub = rospy.Publisher("bord1_aux",Image, queue_size=1)
    self.bord2_pub = rospy.Publisher("bord2_aux",Image, queue_size=1)
    self.crop_pub = rospy.Publisher("crop_aux",Image, queue_size=1)
    self.cost_pub = rospy.Publisher("costdetect_aux",Vector3, queue_size=1)
    
    
    self.bridge = CvBridge()
    self.laser_sub = rospy.Subscriber('/scan_aux', LaserScan, self.callbackLaser,queue_size=1)
    self.cmd_vel_sub = rospy.Subscriber('/cmd_vel', Twist, self.vel_callback, queue_size=1)
    self.dilation = rospy.get_param("/cost_detect/dilation")
    self.angulo= Float32()
    self.distancia= Float32()
    self.cost_d= Vector3()
    self.sang=90
    self.lon=100
    self.fin_ang=90
    self.fin_lon=0.4
    self.people=False
    self.low_speed = False
    print("initialized")
    self.lidar_rotated = True #True for rplidar
    self.mask9=np.array([[-6, -6, -6, -7, -7, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 7, 7, 6, 6, 6 ],
                        [-6, -6, -6, -7, -7, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 7, 7, 6, 6, 6],
                        [-6, -6, -6, -7, -7, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 7, 7, 6, 6, 6 ],
                        [-6, -6, -6, -7, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 6, 6, 6 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ],
                        [-3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3 ]])
    
    
    
    
    
    self.mask10=np.array([[-6, -6, -6, -6, -6, -7, -7, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 7, 7, 6, 6,6, 6 , 6 ],
                        [-6, -6, -6, -6, -6, -7, -7, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 7, 7, 6, 6, 6, 6 , 6 ],
                        [-6, -6, -6, -6, -6, -7, -7, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 7, 7, 6, 6, 6, 6 , 6 ],
                        [-6, -6, -6, -6, -6, -7, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 6, 6, 6, 6 , 6 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ],
                        [-5, -2, -3, -3, -3, -3, -3, -3, -3, -4,-4, -4, -4, -5, -5, 0, 0, 0, 0, 0, 0, 5, 5, 4 , 4 , 4, 4, 3, 3, 3, 3, 3, 3, 3, 2 , 5 ]])

  def vel_callback(self, data):
    linear_speed = (data.linear.x*21)/0.1045
    if(linear_speed>1900):
      self.low_speed=True
    else:
      self.low_speed=False

  def convert_rotation(self, angle):
    rotated = angle + PI
    if rotated > PI:
      rotated = rotated - 2 * PI
    return rotated

  def convert_rotations(self, angle_dists):
    converted = []
    for (angle, distance) in angle_dists:
      rotated = self.convert_rotation(angle)
      converted.append((rotated, distance))
    return converted
  
  # :returns: list[(angle, distance)]
  def angle_and_distance(self, scan_message):
    angle_dists = []
    for i, angle in enumerate(np.arange(scan_message.angle_min, scan_message.angle_max, scan_message.angle_increment)):
      distance = scan_message.ranges[i]
      angle_dists.append((angle, distance))
    return angle_dists

  
  def filter_scans(self, angle_distances):
    filtered_angle_dists = []
    for (angle, distance) in angle_distances:
      if not np.isinf(distance) and \
         distance > LIMIT_MIN_X and \
         distance < LIMIT_MAX_X and \
         angle > MIN_ANGLE and \
         angle < MAX_ANGLE:
        filtered_angle_dists.append((angle, distance))
    return filtered_angle_dists
      
  
  def callbackLaser(self, msg):
    # convert angles and distances
    angle_distances = self.angle_and_distance(msg)
  
    # convert axes of rplidar into hokuyo
    if self.lidar_rotated:
      angle_distances = self.convert_rotations(angle_distances)
    
    # remove unused data
    angle_distances = self.filter_scans(angle_distances)
    #print (angle_distances)
    lidar_matrix = np.zeros((COSTMAP_HEIGHT, COSTMAP_WIDTH), dtype="uint8")
    border_lidar_matrix = np.ones((COSTMAP_HEIGHT, COSTMAP_WIDTH), dtype="uint8")
    #generate the matrix of points from lidar
    for (angle, distance) in angle_distances:
      y = round(distance * np.cos(angle) * 125 / LIMIT_MAX_X, 0)
      x = round(distance * np.sin(angle) * 104 / LIMIT_MAX_X, 0)
      lidar_matrix[OFFSET_COSMAP_Y-int(y), OFFSET_COSMAP_X-int(x)] = 255
      border_lidar_matrix[OFFSET_COSMAP_Y-int(y), OFFSET_COSMAP_X-int(x)] = 255

    kernel = np.ones((3,3),np.uint8)
    #dilate the points form lidar to create a zone to avoid
    dil = cv2.dilate(lidar_matrix,kernel,iterations = 1)
    cost1 = cv2.dilate(dil,kernel,iterations = 2)
    cost2 = cv2.dilate(cost1,kernel,iterations = self.dilation)

    #debug purposes
    # find contours in the thresholded image
    cnts = cv2.findContours(cost2, cv2.RETR_EXTERNAL,
	                          cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if self.low_speed:
      ncentery=130#117#mask10
      ncenterx=105
      crop_img = cost2[ncentery-18:ncentery+18, ncenterx-16:ncenterx+16]#mask9
      res=self.mask9*crop_img
      self.cost_d.x=np.sum(res)/1 #2000.0##/271320.0#/222870.0#/222360.0#/222870.0#/122145.0#/76245.0#/58140.0
    else:
      ncentery=125#112#mask10
      ncenterx=105
      crop_img = cost2[ncentery-20:ncentery+20, ncenterx-18:ncenterx+18] #mask10
      res=self.mask10*crop_img
      self.cost_d.x=np.sum(res)/1 #2200.0##/271320.0#/222870.0#/222360.0#/222870.0#/122145.0#/76245.0#/58140.0

    self.cost_pub.publish(self.cost_d)

    border_lidar_matrix=border_lidar_matrix*255
    for c in cnts:
      cv2.drawContours(border_lidar_matrix, [c], -1, (0, 0, 0), 2)

    # find contours in the thresholded image
    cnts = cv2.findContours(cost1.copy(), cv2.RETR_EXTERNAL,
	                          cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
      cv2.drawContours(border_lidar_matrix, [c], -1, (0, 0, 0), 1)
    # Start coordinate, here (5, 5) 
    # represents the top left corner of rectangle 
    size_robot=20
    start_point = (OFFSET_COSMAP_X-size_robot, OFFSET_COSMAP_Y-size_robot) 
    # Ending coordinate, here (220, 220) 
    # represents the bottom right corner of rectangle 
    end_point = (OFFSET_COSMAP_X+size_robot, OFFSET_COSMAP_Y+size_robot) 
    # Blue color in BGR 
    color = (0, 0, 0) 
    # Line thickness of 2 px 
    thickness = 1  
    # Using cv2.rectangle() method 
    # Draw a rectangle with blue line borders of thickness of 2 px 
    cv2.rectangle(border_lidar_matrix, start_point, end_point, color, thickness) 
  
    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(dil, "mono8"))
      self.cost1_pub.publish(self.bridge.cv2_to_imgmsg(cost1, "mono8"))
      self.cost2_pub.publish(self.bridge.cv2_to_imgmsg(cost2, "mono8"))
      self.border_lidar_matrix_pub.publish(self.bridge.cv2_to_imgmsg(border_lidar_matrix, "mono8"))
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
