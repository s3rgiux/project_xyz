#!/usr/bin/env python
from __future__ import print_function
import roslib
import sys
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import numpy as np
import time
import math

MIN_ANGLE = -3.12413907051
MAX_ANGLE = 3.14159274101
STEPS = 360*4 #1440
ANGLE_INCREMENT = float(1/STEPS) #resolution
TIME_INCREMENT = 0.003 
RANGE_MIN = 0.3
RANGE_MAX = 50

class laser_merger:

    def __init__(self):
        self.laser_merged_publisher = rospy.Publisher("/scan_merged", LaserScan)
        self.laser1_sub = rospy.Subscriber('/scan_main', LaserScan, self.callbackLaserMain)
        self.laser2_sub = rospy.Subscriber('/scan_aux', LaserScan, self.callbackLaserAux)
        self.min_ang = MIN_ANGLE
        self.max_ang = MAX_ANGLE
        self.angle_increment = ANGLE_INCREMENT
        self.time_increment = TIME_INCREMENT
        self.laser_merged = LaserScan()
        self.laser_tmp1 = LaserScan()
        self.laser_tmp2 = LaserScan()
        self.laser_merged.angle_min = self.min_ang
        self.laser_merged.angle_max = self.max_ang
        self.laser_merged.angle_increment = 0.00435422640294 #self.angle_increment
        self.laser_merged.time_increment = self.time_increment
        self.laser_merged.range_min = RANGE_MIN
        self.laser_merged.range_max = RANGE_MAX
        print(self.laser_merged.angle_increment)
        
        self.laser_merged.ranges = np.zeros(STEPS)
        self.laser_merged.intensities = 47 * np.ones(STEPS)
        self.received_laser1 = False
        self.received_laser2 = False
        print("created")
        #self.dilation = rospy.get_param("/cost_detect/dilation")


    def callbackLaserAux(self,msg):
        self.laser_tmp2 = msg
        self.received_laser2 = True
        #print("received aux ")
        #print("received aux ", len(msg.ranges))

    def callbackLaserMain(self,msg):
        self.laser_tmp1 = msg
        self.received_laser1 = True
        self.laser_merged.ranges = self.mergeLasers(self.laser_tmp1 , self.laser_tmp2)
        self.laser_merged.header = self.laser_tmp1.header
        self.laser_merged = self.make_intensities(self.laser_merged)
        self.laser_merged.angle_increment = 0.00435422640294
        self.laser_merged_publisher.publish(self.laser_merged)
        #print("received main ", len(msg.ranges))
    def make_intensities(self,laser):
        for i, element in enumerate(laser.ranges):
            #print("step ",step ,"index", int(i * step),"value", element)
            if math.isinf(element):
                laser.intensities[i] = 0
        return laser
    def pubStatus(self):
        print(self.laser_tmp1.ranges)

    def mergeLaserRanges(self, destinationRanges, laser_source):
        step = len(destinationRanges) / len(laser_source.ranges)
        for i, element in enumerate(laser_source.ranges):
            #print("step ",step ,"index", int(i * step),"value", element)
            destinationRanges[int(i * step)] = element

        return destinationRanges

    def mergeLasers(self,laser_main,laser_aux):
        result_merged_ranges = np.zeros(STEPS)
        #print("first merge")
        result_merged_ranges = self.mergeLaserRanges(result_merged_ranges , laser_aux)
        #print("second merge")
        result_merged_ranges = self.mergeLaserRanges(result_merged_ranges , laser_main)
        
        return result_merged_ranges
        
        
        #a = range(self.min_ang, self.max_ang, self.angle_increment)
        #print(self.laser_merged)
        #index = 0
        #for element in laser_aux.ranges:

        #for x in msg.ranges:
        #    if x>0.15 and x<4.0:
        #        nx[c]=nx[c]*0.08+0.92*(mul*x*np.cos(c*3.1416/180))
        #        ny[c]=ny[c]*0.08+0.92*(mul*x*np.sin(c*3.1416/180))
        #        c=c+1
        #    img[110+int(nx[c]),110+int(ny[c]),0]=255
        #kernel = np.ones((2,2),np.uint8)
        #dil = cv2.dilate(img,kernel,iterations = 1)
        #erosion = cv2.erode(dil,kernel,iterations = 1)
        #dil = cv2.dilate(erosion,kernel,iterations = 1)
        #erosion = cv2.erode(dil,kernel,iterations = 1)
        #dil = cv2.dilate(erosion,kernel,iterations = 1)
        #erosion = cv2.erode(dil,kernel,iterations = 1)
        #try:
        #    self.image_pub.publish(self.bridge.cv2_to_imgmsg(erosion, "mono8"))
        #except CvBridgeError as e:
        #    print(e)

def main(args):
    rospy.init_node('laser_merger', anonymous=True)
    laser_merge_obj = laser_merger()
    while not rospy.is_shutdown():
        #laser_merge_obj.pubStatus()
        time.sleep(0.02)

if __name__ == '__main__':
    main(sys.argv)