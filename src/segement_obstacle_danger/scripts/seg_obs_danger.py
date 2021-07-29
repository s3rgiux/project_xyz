#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import rospy
from time import sleep
from std_msgs.msg import String
from segement_obstacle_danger.msg import Obstacles,States
import time
from scipy.interpolate import interp1d


SLEEP_TIME = 0.001

class SegmentExtractor:
    def __init__(self):
        print("Segements_obtacles")
        self.danger_alert_publisher = rospy.Publisher("Danger",String, queue_size=1)
        rospy.Subscriber('/raw_obstacles', Obstacles, self.obstacles_callback, queue_size=1)
        self.front_detection = 1.0 #rospy.get_param("/obj_track/front_detection")
        self.side_detection = 0.35 #rospy.get_param("/obj_track/side_detection")
        self.last_time_received_osbtacle_msg = time.time()
        self.dangerous_circles = False
        self.dangerous_segments = False

    def pubobs(self):
        if(time.time() - self.last_time_received_osbtacle_msg  > 0.35):
            self.last_time_received_osbtacle_msg  = time.time()
            msg = String()
            msg.data="Clear"
            self.danger_alert_publisher.publish(msg)

    
    def states_callback(self,states):
        if states.state == "KARUGAMO":
            print("KARUGAMO")
        elif states.state == "MANUAL": 
            print("MANUAL")
        elif states.state == "IDLE":
            print("IDLE")

    def calculate_points(self, segment):
        x_points_segment = [segment.first_point.x,segment.last_point.x] # x initial and final coordinate segment
        y_points_segment = [segment.first_point.y,segment.last_point.y] # y initial and final coordinate segment
        num_points = 20
        x_segement_difference = segment.last_point.x - segment.first_point.x 
        x_for_interpolation = []
        for i in range(num_points):
            x_for_interpolation.append(segment.first_point.x + (x_segement_difference / num_points) * i)
        #print("points")
        #print(x_points_segment)
        #print(y_points_segment)
        #print("x for interpolation")
        #print(x_for_interpolation)
        # Finding the interpolation
        points_interpolated = []
        new_points=[]
        y_point_interpolation = interp1d(x_points_segment, y_points_segment) #object cointainign interpolation
        #generate y ponits of interpolated segment acording to inital and end point
        for x_point_interpolation in x_for_interpolation:
            points_interpolated.append( ( x_point_interpolation , float( y_point_interpolation( x_point_interpolation ) ) ) )
        #print(points_interpolated)
        return points_interpolated


    def is_inside_danger_area_circles(self,circle):
        if circle.center.x > 0.0 and circle.center.x < self.front_detection and circle.center.y < self.side_detection and circle.center.y > -self.side_detection:
            return True
        else:
            return False

    def is_inside_danger_area_segment(self,segment_points):
        found_point_inside_danger_area = False
        for point in segment_points:
            x_point = point[0]
            y_point = point[1]
            if x_point > 0.0 and x_point < self.front_detection and y_point < self.side_detection and y_point > -self.side_detection:
                found_point_inside_danger_area = True
        return found_point_inside_danger_area 
        
    def obstacles_callback(self, data):
        message_danger = String()

        for circle in data.circles:
            if self.is_inside_danger_area_circles(circle):
                self.dangerous_circles = True
                message_danger.data = "Danger"
                self.danger_alert_publisher.publish(message_danger)
                print("dangerous_circles")
                break
            else:
                self.dangerous_circles = False
                print("clear_circles")

        for segment in data.segments:
            print("segment_found")
            points_in_segment = self.calculate_points(segment) # list of points in segment
            #print(points_in_segment)
            if self.is_inside_danger_area_segment(points_in_segment): #if any point inside danger area then show danger
                self.dangerous_segments = True
                message_danger.data = "Danger"
                self.danger_alert_publisher.publish(message_danger)
                print("dangerous_segmants")
                break

            else:
                self.dangerous_segments = False
                print("clear_segments")
        if not self.dangerous_circles and not self.dangerous_segments:
            message_danger.data = "Clear"
            self.danger_alert_publisher.publish(message_danger)


        self.last_time_received_osbtacle_msg = time.time()
        
        

    def shutdown(self):
        rospy.sleep(1)
        

def segment_obstacle_main():
    print("segments_obstacles_danger")
    rospy.init_node('peop_lidar_obj', anonymous = True)
    segments_obst_obj = SegmentExtractor()
    while not rospy.is_shutdown():
        segments_obst_obj.pubobs()
        sleep(SLEEP_TIME)

if __name__=='__main__':
    segment_obstacle_main()
