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
import tf2_ros

MIN_ANGLE = -3.12413907051
MAX_ANGLE = 3.14159274101
STEPS = 2880 #360*4 #1440
ANGLE_INCREMENT = float(1/STEPS) #resolution
TIME_INCREMENT = 0.003 
RANGE_MIN = 0.35
RANGE_MAX = 50

TRANSLATION_X_MAIN  = 0.0
TRANSLATION_Y_MAIN  = 0.0
ANGLE_ROTATION_MAIN = 0.0

TRANSLATION_X_AUX  = 0.0
TRANSLATION_Y_AUX  = -0.20
ANGLE_ROTATION_AUX = 0.0

ANGLE_SIMILARITY = 0.008


#Coordianted system used
#  Robot Front
#       Y
# -X        X
#      -Y
class laser_merger:

    def __init__(self):
        self.laser_merged_publisher = rospy.Publisher("/scan_merged", LaserScan, queue_size = 5)
        self.laser_debug = rospy.Publisher("/scan_debug", LaserScan, queue_size = 2)
        self.laser1_sub = rospy.Subscriber('/scan_main', LaserScan, self.callbackLaserMain, queue_size = 2)
        self.laser2_sub = rospy.Subscriber('/scan_aux', LaserScan, self.callbackLaserAux, queue_size = 2)
        self.min_ang = MIN_ANGLE
        self.max_ang = MAX_ANGLE
        self.angle_increment = ANGLE_INCREMENT
        self.time_increment = TIME_INCREMENT
        self.laser_merged = LaserScan()
        self.laser_tmp1 = LaserScan()
        self.laser_tmp2 = LaserScan()
        self.laser_merged.angle_min = self.min_ang
        self.laser_merged.angle_max = self.max_ang
        self.laser_merged.time_increment = self.time_increment
        self.laser_merged.range_min = RANGE_MIN
        self.laser_merged.range_max = RANGE_MAX
        self.laser_merged.ranges = np.zeros(STEPS)
        self.laser_merged.intensities = 47 * np.ones(STEPS)       
        self.tfBuffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tfBuffer)

        self.min_angle_aux  = rospy.get_param("/laser_merge/min_angle_aux" , MIN_ANGLE)
        self.max_angle_aux  = rospy.get_param("/laser_merge/max_angle_aux" , MAX_ANGLE)
        self.min_angle_main = rospy.get_param("/laser_merge/min_angle_main", MIN_ANGLE)
        self.max_angle_main = rospy.get_param("/laser_merge/max_angle_main", MAX_ANGLE)

    def callbackLaserAux(self,msg):
        #apply trasnformation
        arrayXY2 = self.convertLaserRangesToXY(msg)
        transformedXY2 = self.apply_transformation(arrayXY2 , TRANSLATION_X_AUX , TRANSLATION_Y_AUX , ANGLE_ROTATION_AUX)
        newranges2 = self.convertPointsToLaserRanges(transformedXY2, msg) #self.convertXYtoLAserRanges(transformedXY2, msg)
        msg = self.replaceLaserRanges(newranges2, msg)
        self.laser_tmp2 = msg


    def callbackLaserMain(self,msg):
        self.laser_tmp1 = msg
        #ApplyTransformations in case is needed
        #arrayXY1 = self.convertLaserRangesToXY(self.laser_tmp1)
        #transformedXY1 = self.apply_transformation(arrayXY1 , TRANSLATION_X_MAIN , TRANSLATION_Y_MAIN , ANGLE_ROTATION_MAIN)
        #newranges = self.convertXYtoLAserRanges(transformedXY1, self.laser_tmp1)
        #self.laser_tmp1 = self.replaceLaserRanges(newranges, self.laser_tmp1)
        #Merge
        self.laser_merged.ranges = self.mergeLasers(self.laser_tmp1 , self.laser_tmp2)#laser_aux)
        self.laser_merged.header = self.laser_tmp1.header
        self.laser_merged.header.frame_id = "laser_merged"
        self.laser_merged.header.stamp = rospy.Time.now()
        self.laser_merged.time_increment = self.laser_tmp1.scan_time/len(self.laser_merged.ranges)
        self.laser_merged = self.make_intensities(self.laser_merged)
        self.laser_merged.angle_increment = ( np.absolute(self.min_ang) + np.absolute(self.max_ang) ) / STEPS
        self.laser_merged.scan_time = self.laser_tmp1.scan_time
        self.laser_merged_publisher.publish(self.laser_merged)
        


    
    #generate the intensities of the laaser
    def make_intensities(self,laser):
        for i, element in enumerate(laser.ranges):
            if math.isinf(element):
                laser.intensities[i] = 0

        return laser

    # replace ranges on laser message for new_ranges_array
    def replaceLaserRanges(self, new_ranges, laser):
        new_laser_ranges = np.zeros(len(laser.ranges)) 
        for i , element in enumerate(new_ranges):
            new_laser_ranges[i] = element
        laser.ranges = new_laser_ranges

        return laser

    # put ranges of laser into a new array
    def mergeLaserRanges(self, destinationRanges, laser_source):
        step = len(destinationRanges) / len(laser_source.ranges)
        for i, element in enumerate(laser_source.ranges):
            destinationRanges[int(i * step)] = element

        return destinationRanges

    # put ranges of laser into a new array out of phase
    def mergeLaserRangesAux(self, destinationRanges, laser_source):
        step = len(destinationRanges) / len(laser_source.ranges)
        for i, element in enumerate(laser_source.ranges):
            destinationRanges[int(i * step)-1] = element
        return destinationRanges
    
    def convertPointsToLaserRanges(self, points, laser_ref):
        new_laser_ranges = np.ones(len(laser_ref.ranges)) * np.inf
        auxiliarly_array = np.zeros((len(points),2))
        distance_angles = []       
        for i, point in enumerate (points):
            if not np.isinf(point[0]):
                r = np.sqrt((point[0] * point[0]) + (point[1] * point[1])) # r
                auxiliarly_array[i][0] = r
                auxiliarly_array[i][1] = np.arctan2(point[0] , point[1]) # angle
                if r > RANGE_MIN and r < RANGE_MAX:
                    distance_angles.append((auxiliarly_array[i][0] , auxiliarly_array[i][1]))
        serted_list = sorted(distance_angles, key=lambda x: x[1])
        
        angles_array = np.arange(laser_ref.angle_min, laser_ref.angle_max, laser_ref.angle_increment)
        index = 0
        for element in auxiliarly_array:
            for i in range( index, len(laser_ref.ranges)): 
                if angles_array[i-1] - element[1] < ANGLE_SIMILARITY and angles_array[i-1] - element[1] > -ANGLE_SIMILARITY:
                    index = i
                    new_laser_ranges[i] = element[0]
                    break

        return new_laser_ranges

    # apply transformation matrix
    def apply_transformation(self, points, translation_x, translation_y, angle):
        transformed_points = np.zeros((len(points),2))
        for i, point in enumerate(points):
            if not np.isinf(point[0]):
                x = point[0]  * np.cos(angle)  +  point[1] * np.sin(angle) + translation_x #rotation_x + traslation
                y = -point[0] * np.sin(angle)  +  point[1] * np.cos(angle) + translation_y #rotation_y + traslation
                transformed_points[i][0] = x
                transformed_points[i][1] = y    
            else:
                transformed_points[i][0] = float("inf")
                transformed_points[i][1] = float("inf")
        return transformed_points

    # convert laser ranges  (polar plane) to XY points in cartesian plane
    def convertLaserRangesToXY(self,laser):
        converted_array = []
        for i , theta in enumerate(np.arange(laser.angle_min, laser.angle_max, laser.angle_increment)):
            if not np.isinf(laser.ranges[i]) and laser.ranges[i] > RANGE_MIN and laser.ranges[i] < RANGE_MAX:
                x = laser.ranges[i] * np.sin(theta)
                y = laser.ranges[i] * np.cos(theta)
                converted_array.append((x ,y))

        return np.array(converted_array)

    #convert XY arrar in cartesian plane to polar plane array
    def convertXYtoLAserRanges(self,points,laser):
        converted_array = np.zeros((len(laser.ranges))) 
        for i, laser_range in enumerate(laser.ranges):
            dist_squared = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1])
            r = np.sqrt(dist_squared)
            converted_array[i] = r

        return converted_array

    #merge main and aux lasers
    def mergeLasers(self,laser_main,laser_aux):
        result_merged_ranges = np.ones(STEPS) * np.inf#np.zeros(STEPS)
        result_merged_ranges = self.mergeLaserRangesAux(result_merged_ranges , laser_aux)
        result_merged_ranges = self.mergeLaserRanges(result_merged_ranges , laser_main)
        
        return result_merged_ranges
    


def main(args):
    rospy.init_node('laser_merger', anonymous=True)
    laser_merge_obj = laser_merger()
    while not rospy.is_shutdown():
        time.sleep(0.02)

if __name__ == '__main__':
    main(sys.argv)
