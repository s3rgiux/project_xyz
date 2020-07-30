#!/usr/bin/env python
from __future__ import print_function
import roslib
#roslib.load_manifest('opencv_test_python')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import LaserScan
import numpy as np
from matplotlib import pyplot as plt

nx=np.zeros(360,dtype=np.float)
ny=np.zeros(360,dtype=np.float)
class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image)
    self.image_pub2 = rospy.Publisher("image_topic_3",Image)

    self.bridge = CvBridge()
    #self.image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback)
    #self.image_sub = rospy.Subscriber("/ocam/image_raw",Image,self.callback)
    #self.image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback)
    #self.image_sub = rospy.Subscriber("/usb_cam2/image_raw",Image,self.callback2)
    self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.callbackLaser)


  def callbackLaser(self,msg):
    #print(len(msg.ranges))
    #print(msg.ranges[0])
    c=0
    mul=25
    img = np.zeros((220, 220, 1), dtype = "uint8")
    #img = 0*np.ones((500, 500, 1), dtype = "uint8")
    
    #print(img.shape)
    for x in msg.ranges:
      if x>0.15 and x<4.0:
      #if not np.isinf(x):
        nx[c]=nx[c]*0.08+0.92*(mul*x*np.cos(c*3.1416/180))
        #print(nx[c])
        ny[c]=ny[c]*0.08+0.92*(mul*x*np.sin(c*3.1416/180))
        #print(ny[c])
        c=c+1
        img[110+int(nx[c]),110+int(ny[c]),0]=255
        kernel = np.ones((2,2),np.uint8)
        dil = cv2.dilate(img,kernel,iterations = 1)
        erosion = cv2.erode(dil,kernel,iterations = 1)
        dil = cv2.dilate(erosion,kernel,iterations = 1)
        erosion = cv2.erode(dil,kernel,iterations = 1)
        dil = cv2.dilate(erosion,kernel,iterations = 1)
        erosion = cv2.erode(dil,kernel,iterations = 1)
        
        
         
    #for x in msg.ranges:
    #  if not np.isinf(x):
    #    xc=int(mul*x*np.cos(c*3.1416/180))
    #    #print(xc)
    #    #print(",")
    #    yc=int(mul*x*np.sin(c*3.1416/180))
    #    #print(yc)
    #    c=c+1
    #    img[100+xc,100+yc,0]=255
    #    kernel = np.ones((2,2),np.uint8)
    #    dil = cv2.dilate(img,kernel,iterations = 4)
    #    eros = cv2.erode(dil,kernel,iterations = 1)    
    #plt.imshow(img)
    #plt.show()
    #cv2.imshow("Image window", img)
    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(erosion, "mono8"))
    except CvBridgeError as e:
      print(e)

      

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "mono8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    print(rows)
    print(cols)
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (200,200), 50, 255)
	
    #cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "mono8"))
    except CvBridgeError as e:
      print(e)

  def callback2(self,data):
    try:
      cv_image2 = self.bridge.imgmsg_to_cv2(data, "mono8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image2.shape
    print(rows)
    print(cols)
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image2, (200,200), 50, 255)
	
    #cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub2.publish(self.bridge.cv2_to_imgmsg(cv_image, "mono8"))
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
