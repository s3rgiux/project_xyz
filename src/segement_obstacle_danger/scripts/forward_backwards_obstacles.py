#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import rospy
from time import sleep
from std_msgs.msg import String
from segement_obstacle_danger.msg import Obstacles, States , DangerStates
import time
from scipy.interpolate import interp1d
import shapely
from shapely.geometry import LineString, Point
import detect_cross
import numpy as np

SLEEP_TIME = 0.001
MIN_DISTANCE_INSIDE_AREA = 0.3 #meters
MAX_DISTANCE_INSIDE_AREA = 1.1 #meters

class SegmentExtractor:
    def __init__(self):
        print("Segements_obtacles")
        self.danger_alert_publisher = rospy.Publisher("danger_states",DangerStates, queue_size=1)
        self.obs_sub = rospy.Subscriber('/raw_obstacles', Obstacles, self.obstacles_callback, queue_size=1)
        self.states_sub = rospy.Subscriber('/pitakuru_states', States, self.states_callback, queue_size=1)
        self.front_detection = 1.1 #rospy.get_param("/obj_track/front_detection")
        self.side_detection = 0.4 #rospy.get_param("/obj_track/side_detection")
        self.last_time_received_osbtacle_msg = time.time()
        self.messages_states_danger = DangerStates()

    def msg_all_clear(self):
        self.messages_states_danger.state_forward_circle = DangerStates.CLEAR
        self.messages_states_danger.state_backward_circle = DangerStates.CLEAR
        self.messages_states_danger.state_forward_segment = DangerStates.CLEAR
        self.messages_states_danger.state_backward_segment = DangerStates.CLEAR

    def pubobs(self):
        if(time.time() - self.last_time_received_osbtacle_msg  > 0.5):
            self.last_time_received_osbtacle_msg  = time.time()
            self.msg_all_clear()
            self.danger_alert_publisher.publish(self.messages_states_danger)

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
        points_interpolated = []
        new_points=[]
        y_point_interpolation = interp1d(x_points_segment, y_points_segment) #object cointainign interpolation
        for x_point_interpolation in x_for_interpolation:
            points_interpolated.append( ( x_point_interpolation , float( y_point_interpolation( x_point_interpolation ) ) ) )

        return points_interpolated

    def is_point_inside_determined_area(self,pointx,pointy):
        dist=np.sqrt(pointx * pointx + pointy * pointy)
        if dist > MIN_DISTANCE_INSIDE_AREA and dist < MAX_DISTANCE_INSIDE_AREA: # is inside circular area "Donut"
            if pointx > -self.front_detection and pointx < self.front_detection and pointy < self.side_detection and pointy > -self.side_detection:
                return True
            else:
                return False

    def is_inside_danger_area_circles(self,circle):

        if self.is_point_inside_determined_area(circle.center.x,circle.center.y):
            print("found_point circle {},{}".format(circle.center.x , circle.center.y))
            return True
        else:
            return False

    def is_inside_danger_area_segment(self,segment_points):
        found_point_inside_danger_area_forward = False
        found_point_inside_danger_area_backward = False

        for point in segment_points:
            x_point = point[0]
            y_point = point[1]
            if self.is_point_inside_determined_area(x_point,y_point):
                if x_point > 0:
                    print("found_point segment {},{}".format(x_point,y_point))
                    found_point_inside_danger_area_forward = True
                else:
                    print("found_point segment {},{}".format(x_point,y_point))
                    found_point_inside_danger_area_backward = True
        return found_point_inside_danger_area_forward,found_point_inside_danger_area_backward

        
    # data : Obstacles(segments, circles)
    def obstacles_callback(self, data):
        self.msg_all_clear()

        for circle in data.circles:
            if self.is_inside_danger_area_circles(circle):
                if circle.center.x > 0:
                    self.messages_states_danger.state_forward_circle = DangerStates.DANGER
                else:
                    self.messages_states_danger.state_backward_circle = DangerStates.DANGER

        for segment in data.segments:
            points_in_segment = self.calculate_points(segment) # list of points in segment
            found_forward , found_backward = self.is_inside_danger_area_segment(points_in_segment)
            if found_forward: #if any point inside danger area then show danger
                self.messages_states_danger.state_forward_segment = DangerStates.DANGER
            elif found_backward:
                self.messages_states_danger.state_backward_segment = DangerStates.DANGER

    
        self.danger_alert_publisher.publish(self.messages_states_danger)
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