#!/usr/bin/env python
# coding: utf-8
import yaml
import cv2 
import imutils 
import numpy as np
import sys,time
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import Float32
from std_msgs.msg import Int16
import rospy
import message_filters
from tf.transformations import quaternion_matrix
from sensor_msgs.msg import Image, CameraInfo
from fiducial_msgs.msg import FiducialArray, FiducialTransformArray
from cv_bridge import CvBridge
from geometry_msgs.msg import Point, Vector3


class PeopImage: 
    

    def __init__(self):
        rospy.init_node('people_detect', log_level=rospy.INFO)
        rospy.on_shutdown(self.on_shutdown)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/image_raw', Image, self.callback,queue_size=1)
        self.ang_sub = rospy.Subscriber("peopAng2",Vector3, self.callback_ang,queue_size=1)
        #info_sub = message_filters.Subscriber('camera_info', CameraInfo)
        self.pub = rospy.Publisher('people/image', Image, queue_size=1)
        self.peop_pub = rospy.Publisher('ang_peop_detect_img', Float32, queue_size=1)
        self.hog = cv2.HOGDescriptor() 
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        self.ang_pub= Float32() 
        self.ang_laser=0
        self.timex=0
        self.last_time=0

    def callback_ang(self, msg):
        #self.ang_laser=msg.data
        self.ang_laser=msg.x
   
    def callback(self, image_msg):
        img = self.bridge.imgmsg_to_cv2(image_msg, 'bgr8')
        #image = imutils.resize(img,width=min(360, img.shape[1]))
        image=cv2.resize(img,(320,240))
        (regions, _) = self.hog.detectMultiScale(image,  
                                    winStride=(8 , 8),# winStride=(16, 16), 
                                    padding=(4, 4),#padding=(4, 4), 
                                    scale=1.05)#scale=1.05
   
        # Drawing the regions in the Image
         
        for (x, y, w, h) in regions: 
            cv2.rectangle(image, (x, y),  
                      (x + w, y + h),  
                      (0, 0, 255), 2)
            
            ang =np.arctan2(160-(x + (w/2)),270-( y+(h/2))) * 180 / np.pi #0-np.arctan2(160-(x + (w/2)),270-( y+(h/2))) * 180 / np.pi
            #if(self.ang_laser+7>ang and self.ang_laser-7<ang):
            x2, y2 = 160, 280
            x1, y1 = (x + (w/2)),( y+(h/2))
            line_thickness = 3
            cv2.line(image, (x1, y1), (x2, y2), (255, 255, 255), thickness=line_thickness)
            self.ang_pub.data=ang
            self.peop_pub.publish(self.ang_pub)
            self.last_time=time.time()#self.timex
        # Showing the output Image 
        #cv2.imshow("Image", image)  
        #cv2.imshow('frame', img)
        aruco_msg = self.bridge.cv2_to_imgmsg(image, encoding="bgr8")
        self.pub.publish(aruco_msg)

    def pub_lost(self):
        if(time.time()-self.last_time>0.3):
        #if(self.track==0):
            self.ang_pub.data=-500
            self.peop_pub.publish(self.ang_pub)
        
    
    def on_shutdown(self):
        return
        cv2.destroyAllWindows()


if __name__ == '__main__':
    node = PeopImage()
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    while not rospy.is_shutdown():
        node.pub_lost()
        R.sleep()

