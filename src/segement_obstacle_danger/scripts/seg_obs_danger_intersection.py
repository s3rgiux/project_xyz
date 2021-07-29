#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import rospy
from time import sleep
from std_msgs.msg import String
from segement_obstacle_danger.msg import Obstacles, States
import time
from scipy.interpolate import interp1d
import shapely
from shapely.geometry import LineString, Point
import detect_cross

SLEEP_TIME = 0.001
P0 = (0, 0)
P1_1 = (1.06252, -0.28470) # r = 1.1[m] theta = -15deg ~ +15deg
P1_2 = (1.06252, 0.28470)


class SegmentExtractor:
    def __init__(self):
        print("Segements_obtacles")
        self.danger_alert_publisher = rospy.Publisher("Danger",String, queue_size=1)
        self.obs_sub = rospy.Subscriber('/raw_obstacles', Obstacles, self.obstacles_callback, queue_size=1)
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



    def is_inside_danger_area_circles(self,circle):
        if circle.center.x > 0.0 and circle.center.x < self.front_detection and circle.center.y < self.side_detection and circle.center.y > -self.side_detection:
            print("found_point circle {},{}".format(circle.center.x,circle.center.y))
            return True
        else:
            return False

    def is_inside_danger_area_segment(self,segment_points):
        found_point_inside_danger_area = False
        for point in segment_points:
            x_point = point[0]
            y_point = point[1]
            if x_point > 0.0 and x_point < self.front_detection and y_point < self.side_detection and y_point > -self.side_detection:
                print("found_point segment {},{}".format(x_point,y_point))
                found_point_inside_danger_area = True
        return found_point_inside_danger_area

    def in_area(self, segment):
        q0 = (segment.first_point.x, segment.first_point.y)
        q1 = (segment.last_point.x, segment.last_point.y)

        return detect_cross.is_cross_linear(P0, P1_1, q0, q1) or \
               detect_cross.is_cross_linear(P0, P1_2, q0, q1) or \
               detect_cross.is_cross_circle(P0, P1_1, q0, q1)
        
    # data : Obstacles(segments, circles)
    def obstacles_callback(self, data):
        message_danger = String()
        for circle in data.circles:
            if self.is_inside_danger_area_circles(circle):
                self.dangerous_circles = True
                message_danger.data = "Danger"
                self.danger_alert_publisher.publish(message_danger)

            else:
                self.dangerous_circles = False

        for segment in data.segments:
            print(segment)
            print(self.in_area(segment))
            if self.in_area(segment):

                print("in area, danger")
                # message_danger.data = "Danger"
                # self.danger_alert_publisher.publish(message_danger)
            else:
                print("not in area")
                # message_danger.data = "Clear"
                # self.danger_alert_publisher.publish(message_danger)

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
