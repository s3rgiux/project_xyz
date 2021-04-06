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


nx=np.zeros(360,dtype=np.float)
ny=np.zeros(360,dtype=np.float)

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("shelfborders",Image, queue_size=1)
    self.cost1_pub = rospy.Publisher("costshelf1",Image, queue_size=1)
    self.cost2_pub = rospy.Publisher("costshelf2",Image, queue_size=1)
    self.bord1_pub = rospy.Publisher("bordshelf1",Image, queue_size=1)
    self.bord2_pub = rospy.Publisher("bordshelf2",Image, queue_size=1)
    self.crop_pub = rospy.Publisher("cropshelf",Image, queue_size=1)
    self.shelf_pub = rospy.Publisher("shelf_size",Float32, queue_size=1)
    #self.cost_pub = rospy.Publisher("costdetect",Vector3, queue_size=1)
    
    
    self.bridge = CvBridge()
    self.laser_sub = rospy.Subscriber('/rplidar', LaserScan, self.callbackLaser,queue_size=1)
    self.cmd_vel_sub = rospy.Subscriber('/cmd_vel', Twist, self.vel_callback, queue_size=1)
    self.dilation = 2#rospy.get_param("/cost_detect/dilation")
    self.angulo= Float32()
    self.distancia= Float32()
    self.cost_d= Vector3()
    self.sang=90
    self.lon=100
    self.fin_ang=90
    self.fin_lon=0.4
    self.people=False
    self.low_speed=False
    
    #print(self.mask)
    #print(self.mask+self.mask)

  def vel_callback(self, data):
    linear_speed = (data.linear.x*21)/0.1045
    if(linear_speed>1900):
      self.low_speed=True
    else:
      self.low_speed=False

  
  def callbackLaser(self,msg):
    c=0
    angle=-3.12413907051
    mul=20
    #img = np.zeros((240, 320), dtype = "uint8")
    img = np.zeros((158, 211), dtype = "uint8")

    cost1 = np.zeros((240, 320), dtype = "uint8")
    cost2 = np.zeros((240, 320), dtype = "uint8")
    bord1 = np.ones((158, 211), dtype = "uint8")
    centery=79
    centerx=105
    #for i, theta in enumerate(np.arange(msg.angle_min,msg.angle_max,msg.angle_increment)):
    max1=0
    foundx1=0
    foundy1=0
    max2=0
    foundx2=0
    foundy2=0
    for i, theta in enumerate(np.arange(msg.angle_min,msg.angle_max,msg.angle_increment)):
      #if not np.isinf(msg.ranges[i]) and msg.ranges[i]>0.15 and msg.ranges[i] < 3.7 and (theta>2.35 or theta<-2.35):
      
      if not np.isinf(msg.ranges[i]) and msg.ranges[i]>0.15 and msg.ranges[i] < 0.6 and theta>-0.69 and theta<-0.001:
        y=round(msg.ranges[i]*np.cos(theta)*80/1.1,0)
        x=round(msg.ranges[i]*np.sin(theta)*80/1.1,0)
        img[centery-int(y),centerx-int(x)]=255
        bord1[centery-int(y),centerx-int(x)]=255
        if(theta<max1):
          max1=theta
          foundx1=x
          foundy1=y
      if not np.isinf(msg.ranges[i]) and msg.ranges[i]>0.15 and msg.ranges[i] < 0.6 and theta>0.001 and theta<0.69:#0.7854:
        y=round(msg.ranges[i]*np.cos(theta)*80/1.1,0)
        x=round(msg.ranges[i]*np.sin(theta)*80/1.1,0)
        img[centery-int(y),centerx-int(x)]=255
        bord1[centery-int(y),centerx-int(x)]=255
        if(theta>max2):
          max2=theta
          foundx2=x
          foundy2=y
    shelf_msg=Float32()
    shelf_msg.data=0
    if(foundy2>foundy1-7 and foundy2<foundy1+7):
      print("in the same line")
      print("difference in x {}".format(foundx1-foundx2)) 
      #if((foundx1-foundx2) <33):
      if(np.abs(foundx1-foundx2) <30):
        print("small")
        shelf_msg.data=np.abs(foundx1-foundx2)
      elif(np.abs(foundx1-foundx2) >31):
        print("big")
        shelf_msg.data=np.abs(foundx1-foundx2)
    self.shelf_pub.publish(shelf_msg)
    print("max1 {},{},{}".format(max1,foundx1,foundy1))
    print("max2 {},{},{}".format(max2,foundx2,foundy2))

    #for shelf small <33
    #for shelf big >36
    # kernel = np.ones((3,3),np.uint8)
    # dil = cv2.dilate(img,kernel,iterations = 1)
    # cost1 = cv2.dilate(dil,kernel,iterations = 2)
    # cost2 = cv2.dilate(cost1,kernel,iterations = self.dilation)
  
    # try:
    #   self.image_pub.publish(self.bridge.cv2_to_imgmsg(dil, "mono8"))
    #   self.cost1_pub.publish(self.bridge.cv2_to_imgmsg(cost1, "mono8"))
    #   self.cost2_pub.publish(self.bridge.cv2_to_imgmsg(cost2, "mono8"))
    #   self.bord1_pub.publish(self.bridge.cv2_to_imgmsg(bord1, "mono8"))
    #   #self.crop_pub.publish(self.bridge.cv2_to_imgmsg(crop_img, "mono8"))
    # except CvBridgeError as e:
    #   print(e) 


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
