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


nx=np.zeros(360,dtype=np.float)
ny=np.zeros(360,dtype=np.float)

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("imageborders",Image, queue_size=1)
    self.cost1_pub = rospy.Publisher("cost1",Image, queue_size=1)
    self.cost2_pub = rospy.Publisher("cost2",Image, queue_size=1)
    self.ang_pub = rospy.Publisher("peopAng2",Float32, queue_size=1)
    self.dist_pub = rospy.Publisher("peopDist2",Float32, queue_size=1)
    self.bridge = CvBridge()
    self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.callbackLaser,queue_size=1)
    self.angulo= Float32()
    self.distancia= Float32()
    self.sang=90
    self.lon=100
    self.fin_ang=90
    self.fin_lon=0.4
    self.people=False

  

  
  def callbackLaser(self,msg):
    c=0
    angle=-3.12413907051
    mul=20
    #img = np.zeros((240, 320), dtype = "uint8")
    img = np.zeros((420, 320), dtype = "uint8")

    cost1 = np.zeros((240, 320), dtype = "uint8")
    cost2 = np.zeros((240, 320), dtype = "uint8")

    for i, theta in enumerate(np.arange(msg.angle_min,msg.angle_max,msg.angle_increment)):
      if i<30 or i>260:
        if not np.isinf(msg.ranges[i]) and msg.ranges[i]>0.15 and msg.ranges[i] < 4:
          y=round(msg.ranges[i]*np.cos(theta)*120/4,0)
          x=round(msg.ranges[i]*np.sin(theta)*120/4,0)
          img[318-int(y),240+int(x)]=255
    kernel = np.ones((3,3),np.uint8)
    dil = cv2.dilate(img,kernel,iterations = 1)
    #cost1 = cv2.dilate(dil,kernel,iterations = 2)
    #cost2 = cv2.dilate(cost1,kernel,iterations = 2)

    # find contours in the thresholded image
    #cnts = cv2.findContours(dil.copy(), cv2.RETR_EXTERNAL,
	  #                        cv2.CHAIN_APPROX_SIMPLE)
    #cnts = imutils.grab_contours(cnts)
    #M = cv2.moments(cnts[0])
    #cX = int(M["m10"] / M["m00"])
    #cY = int(M["m01"] / M["m00"])
    # draw the contour and center of the shape on the image
    #cv2.drawContours(dil, [cnts[0]], -1, (255, 255, 255), 2)
    #cv2.circle(dil, (cX, cY), 5, (255, 255, 255), -1)
    #cv2.imshow("new",dil)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(dil, "mono8"))
      self.cost1_pub.publish(self.bridge.cv2_to_imgmsg(cost1, "mono8"))
      self.cost2_pub.publish(self.bridge.cv2_to_imgmsg(cost2, "mono8"))
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
