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


#Coordianted system used
#  Robot Front
#       Y
# -X        X
#      -Y
class laser_merger:

    def __init__(self):
       
        
        self.laser1_sub = rospy.Subscriber('/scan_main', LaserScan, self.callbackLaserMain, queue_size = 2)
        self.laser2_sub = rospy.Subscriber('/scan_aux', LaserScan, self.callbackLaserAux, queue_size = 2)
        

        self.min_angle_aux  = rospy.get_param("/laser_merge/min_angle_aux" , MIN_ANGLE)
        self.max_angle_aux  = rospy.get_param("/laser_merge/max_angle_aux" , MAX_ANGLE)
        self.min_angle_main = rospy.get_param("/laser_merge/min_angle_main", MIN_ANGLE)
        self.max_angle_main = rospy.get_param("/laser_merge/max_angle_main", MAX_ANGLE)


    def extract_regions(self, msg):
        up_left_region    = []
        up_rigth_region   = []
        down_left_region  = []
        down_rigth_region = []
        START_ANGLE_UP    = 0.7853
        END_ANGLE_UP      = 1.5708
        START_ANGLE_DOWN  = 1.5708
        END_ANGLE_DOWN    = 2.35


        for i , theta in enumerate(np.arange(laser.angle_min, laser.angle_max, laser.angle_increment)):

            up_left_region    = []
            up_right_region   = []
            down_left_region  = []
            down_right_region = []
            if theta >= START_ANGLE_UP and theta <= END_ANGLE_UP :
                up_left_region.append(msg.ranges[i])
            if theta >= START_ANGLE_DOWN and theta <= END_ANGLE_DOWN :
                down_left_region.append(msg.ranges[i])
            if theta <= -START_ANGLE_UP and theta >= -END_ANGLE_UP :
                up_right_region.append(msg.ranges[i])
            if theta <= -START_ANGLE_DOWN and theta >= -END_ANGLE_DOWN :
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

        print("area ul ", area_ul_region)    


def main(args):
    rospy.init_node('laser_merger', anonymous=True)
    laser_merge_obj = laser_merger()
    while not rospy.is_shutdown():
        time.sleep(0.02)

if __name__ == '__main__':
    main(sys.argv)
