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
P1_1 = (-0.28470, 1.06252) # r = 1.1[m] theta = -15deg ~ +15deg
P1_2 = (0.28470, 1.06252)


class SegmentExtractor:
    def __init__(self):
        print("Segements_obtacles")
        self.danger_alert_publisher = rospy.Publisher("Danger",String, queue_size=1)
        self.obs_sub = rospy.Subscriber('/raw_obstacles', Obstacles, self.obstacles_callback, queue_size=1)
        self.front_detection = 1.0 #rospy.get_param("/obj_track/front_detection")
        self.side_detection = 0.35 #rospy.get_param("/obj_track/side_detection")
        self.last_time_received_osbtacle_msg = time.time()

    def pubobs(self):
        if(time.time() - self.last_time_received_osbtacle_msg  > 0.35):
            self.last_time_received_osbtacle_msg  = time.time()
            msg = String()
            msg.data = "Clear"
            self.danger_alert_publisher.publish(msg)

    def in_area_circle(self, circle):
        q = (circle.center.y, circle.center.x)
        return detect_cross.is_point_in_circle(P1_1, P1_2, q)

    def in_area_linear(self, segment):
        q0 = (segment.first_point.y, segment.first_point.x)
        q1 = (segment.last_point.y, segment.last_point.x)
        print("p0 p1 q0 q1", P0, P1_1, q0, q1 )
        print("first detect", detect_cross.is_cross_linear(P0, P1_1, q0, q1))
        print("second detect", detect_cross.is_cross_linear(P0, P1_2, q0, q1))
        print("third detect", detect_cross.is_cross_circle(P1_1, P0, q0, q1))
        return detect_cross.is_cross_linear(P0, P1_1, q0, q1) or \
               detect_cross.is_cross_linear(P0, P1_2, q0, q1)# or \
               #detect_cross.is_cross_circle(P0, P1_1, q0, q1)
        
    # data : Obstacles(segments, circles)
    def obstacles_callback(self, data):
        message_danger = String()
        message_danger.data = "Clear"

        for circle in data.circles:
            if self.in_area_circle(circle):
                message_danger.data = "Danger"
        for segment in data.segments:
            if self.in_area_linear(segment):
                message_danger.data = "Danger"
                self.danger_alert_publisher.publish(message_danger)
        
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
