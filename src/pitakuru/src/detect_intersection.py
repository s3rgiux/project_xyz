#!/usr/bin/env python
from __future__ import print_function
import roslib
import sys
import rospy
from std_msgs.msg import String, Float32
from sensor_msgs.msg import LaserScan
import numpy as np
import time
import math


#Coordianted system used
#  Robot Front
#       Y
# -X        X
#      -Y
class DetectIntersection:

    def __init__(self):
        self.laser1_sub = rospy.Subscriber('/scan_main', LaserScan, self.callbackLaserMain, queue_size = 2)
        self.inter_area_front_pub  = rospy.Publisher("intersection_area_front", Float32)
        self.inter_area_rear_pub   = rospy.Publisher("intersection_area_rear", Float32)
        self.inter_der_pub   = rospy.Publisher("intersection_der_rear", Float32)
        self.inter_ratio_pub   = rospy.Publisher("intersection_ratio", Float32)
        self.area_front_msg = Float32()
        self.area_rear_msg = Float32()
        self.der_msg = Float32()
        self.ratio_msg = Float32()
        self.deriv = 0
        #self.laser2_sub = rospy.Subscriber('/scan_aux', LaserScan, self.callbackLaserAux, queue_size = 2)
        #self.min_angle_aux  = rospy.get_param("/laser_merge/min_angle_aux" , MIN_ANGLE)
        #self.max_angle_aux  = rospy.get_param("/laser_merge/max_angle_aux" , MAX_ANGLE)
        #self.min_angle_main = rospy.get_param("/laser_merge/min_angle_main", MIN_ANGLE)
        #self.max_angle_main = rospy.get_param("/laser_merge/max_angle_main", MAX_ANGLE)


    def extract_regions(self, msg):
        up_left_region    = []
        up_rigth_region   = []
        down_left_region  = []
        down_rigth_region = []
        START_ANGLE_UP    = 0.7853
        END_ANGLE_UP      = 1.5708
        START_ANGLE_DOWN  = 1.5708
        END_ANGLE_DOWN    = 2.35
        
        #START_ANGLE_UP    = 0.01
        #END_ANGLE_UP      = 1.5708
        #START_ANGLE_DOWN  = 1.5708
        #END_ANGLE_DOWN    = 3.1
        
        up_left_region    = []
        up_right_region   = []
        down_left_region  = []
        down_right_region = []
        for i , theta in enumerate(np.arange(msg.angle_min, msg.angle_max, msg.angle_increment)):

            if not np.isinf(msg.ranges[i]):
                if theta >= START_ANGLE_UP and theta <= END_ANGLE_UP :
                #if theta >= 0 and theta <= 0.2 :
                    #print("e ", i , " v ", msg.ranges[i])
                    up_left_region.append(msg.ranges[i])

                if theta >= START_ANGLE_DOWN and theta <= END_ANGLE_DOWN :
                #if theta >= 0.2 and theta <= 0.4 :
                    #print("f ", i , " v ", msg.ranges[i])
                    down_left_region.append(msg.ranges[i])
                if theta <= -START_ANGLE_UP and theta >= -END_ANGLE_UP :
                #if theta <= -0.01 and theta >= -0.2 :
                    #print("g ", i , " v ", msg.ranges[i])
                    up_right_region.append(msg.ranges[i])
                if theta <= -START_ANGLE_DOWN and theta >= -END_ANGLE_DOWN :
                #if theta <= -0.2 and theta >= -0.4 :
                    #print("h ", i , " v ", msg.ranges[i])
                    down_right_region.append(msg.ranges[i])
        
        return up_left_region, up_right_region, down_left_region, down_right_region


    def calculate_area(self, region):
        #simply using sum because is a list
        return sum(region)

    def callbackLaserMain(self,msg):
        up_left_region, up_right_region, down_left_region, down_right_region = self.extract_regions(msg)
        area_ul_region = self.calculate_area(up_left_region)
        area_ur_region = self.calculate_area(up_right_region)
        area_dl_region = self.calculate_area(down_left_region)
        area_dr_region = self.calculate_area(down_right_region)
        self.area_front_msg.data = area_dl_region + area_dr_region
        self.area_rear_msg.data = area_ul_region + area_ur_region
        self.der_msg.data = self.deriv
        self.deriv = (self.area_front_msg.data - self.deriv) / 0.1
        self.inter_area_front_pub.publish(self.area_front_msg)
        self.inter_area_rear_pub.publish(self.area_rear_msg)
        self.inter_der_pub.publish(self.der_msg)
        
        front_area = area_dl_region + area_dr_region
        rear_area  = area_ul_region + area_ur_region
        ratio = rear_area / front_area
        print("ratio ", ratio)
        self.ratio_msg.data = ratio
        self.inter_ratio_pub.publish(self.ratio_msg)
        if ratio < 0.43:
            print("detectet condition grater ratio")
        #print(" rear ", area_ul_region + area_ur_region , "front ", area_dl_region + area_dr_region, "fl ", area_dl_region, "fr ", area_dr_region, "rl ", area_ul_region, "rr ", area_ur_region ) 

        #if np.abs(area_ul_region - area_dl_region) > 1000:
        #    print("detectted something in left")
        #if np.abs(area_ur_region - area_dr_region) > 1000:
        #    print("detectted something in right")


def main(args):
    rospy.init_node('DetectIntersection', anonymous=True)
    laser_merge_obj = DetectIntersection()
    while not rospy.is_shutdown():
        time.sleep(0.02)

if __name__ == '__main__':
    main(sys.argv)
