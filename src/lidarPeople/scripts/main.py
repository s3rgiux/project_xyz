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
    self.image_pub = rospy.Publisher("imageLaser",Image, queue_size=1)
    self.ang_pub = rospy.Publisher("peopAng2",Float32, queue_size=1)
    self.dist_pub = rospy.Publisher("peopDist2",Float32, queue_size=1)
    self.bridge = CvBridge()
    self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.callbackLaser)
    self.angulo= Float32()
    self.distancia= Float32()
    self.sang=90
    self.lon=100
    self.fin_ang=90
    self.fin_lon=0.4
    self.people=False

  def sort_contours(self,cnts, method="bottom-to-top"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0
    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
      reverse = True
    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
      i = 1
    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),key=lambda b:b[1][i], reverse=reverse))
    #(cnts) = zip(*sorted(zip(cnts),
    #  key=lambda b:b[i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return (cnts,boundingBoxes)

  
  def callbackLaser(self,msg):
    c=0
    angle=-3.12413907051
    mul=20
    img = np.zeros((240, 320), dtype = "uint8")
    #img = 0*np.ones((500, 500, 1), dtype = "uint8")
    
    for i, theta in enumerate(np.arange(msg.angle_min,msg.angle_max,msg.angle_increment)):
      if i<35 or i>324:
        if not np.isinf(msg.ranges[i]) and msg.ranges[i]>0.15 and msg.ranges[i] < 1.5:
          y=round(msg.ranges[i]*np.cos(theta)*210/1.5,0)
          x=round(msg.ranges[i]*np.sin(theta)*210/1.5,0)
          img[240+int(y),160+int(x)]=255
    kernel = np.ones((3,3),np.uint8)
    dil = cv2.dilate(img,kernel,iterations = 2)

    # find contours in the thresholded image
    cnts = cv2.findContours(dil.copy(), cv2.RETR_EXTERNAL,
	                          cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    #print(len(cnts))
    if len(cnts)==1:
      area = cv2.contourArea(cnts[0])
      #print(area)
      if(area>17):
        M = cv2.moments(cnts[0])
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # draw the contour and center of the shape on the image
        cv2.drawContours(dil, [cnts[0]], -1, (255, 255, 255), 2)
        cv2.circle(dil, (cX, cY), 5, (255, 255, 255), -1)
        #cv2.imshow("new",dil)
        #cv2.putText(dil, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        x2, y2 = 160, 240
        x1, y1 = cX, cY
        line_thickness = 1
        cv2.line(dil, (x1, y1), (x2, y2), (255, 255, 255), thickness=line_thickness)
        self.sang=np.arctan2(y2-y1, x2-x1) * 180 / np.pi
        self.lon=np.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))
        self.people=True
        #print(ang)
        #print(lon)
        
    
    elif len(cnts)>=2:
      nang=np.zeros(2)
      dist=np.zeros(2)
      cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5] 
      #(cnts , bbox) = self.sort_contours(cnts)#, method="bottom-to-top")
      #ang=np.zeros(5,dtype=np.float)
      for i in range(0, 2):
        # compute the center of the contour
        area = cv2.contourArea(cnts[i])
        if(area>17):
          M = cv2.moments(cnts[i])
          cX = int(M["m10"] / M["m00"])
          cY = int(M["m01"] / M["m00"])
          # draw the contour and center of the shape on the image
          cv2.drawContours(dil, [cnts[i]], -1, (255, 255, 255), 2)
          cv2.circle(dil, (cX, cY), 5, (255, 255, 255), -1)
          #cv2.putText(dil, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
          x2, y2 = 160, 240
          x1, y1 = cX, cY
          line_thickness = 1
          cv2.line(dil, (x1, y1), (x2, y2), (255, 255, 255), thickness=line_thickness)
          #if(g<=4):
          nang[i]=np.arctan2(y2-y1, x2-x1) * 180 / np.pi
          dist[i]=np.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))
          self.people=True
          #print(ang)
          #  g+=1
          # show the image
      self.sang=(nang[0]+nang[1])/2
      self.lon=(dist[0]+dist[1])/2
      
      # if not nang[1]==0 and not nang[1]==0:
      # else if()
      # print("2ang")
      # print(sang)
      # print(lon)
    else:
      self.people=False

    if(self.people==False):
      self.angulo.data=-500
      self.distancia.data=0
    else:
      self.fin_ang=self.fin_ang*0.7+0.3*self.sang
      self.angulo.data=(self.fin_ang-90)#self.sang
      self.fin_lon=self.fin_lon*0.6+0.4*self.lon
      self.distancia.data=self.fin_lon

    self.ang_pub.publish(self.angulo)
    self.dist_pub.publish(self.distancia)
    #print("###")  
    #print(self.fin_lon)
    #print(self.fin_ang)
    x1, y1 = 160, 0
    x2, y2 = 160, 240
    line_thickness = 1
    cv2.line(dil, (x1, y1), (x2, y2), (255, 255, 255), thickness=line_thickness)
    #cv2.imshow("dilatacion",dil)
    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(dil, "mono8"))
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
