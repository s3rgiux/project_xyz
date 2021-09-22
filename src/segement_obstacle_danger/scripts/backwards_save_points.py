#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import rospy
from time import sleep
from std_msgs.msg import String
from segement_obstacle_danger.msg import Obstacles, States , DangerStates
import time
from scipy.interpolate import interp1d
import numpy as np

SLEEP_TIME = 0.001
MIN_DISTANCE_INSIDE_AREA = 0.3 #0.3 #meters
MAX_DISTANCE_INSIDE_AREA = 1.0 #1.1 #meters
ANGLE_REGION_MIN = -2.1 #radians 1.57 = 90 deg
ANGLE_REGION_MAX = 2.1 #radians
RADIUS_SIMILARITY = 0.09
DISTANCE_BACK_SHELF_MIN = 0.5
DISTANCE_BACK_SHELF_MAX = 0.8
NUM_POINTS_TO_DETECT_SHELF = 1

class SegmentExtractor:
    def __init__(self):
        print("Segements_obtacles")
        #self.danger_alert_publisher = rospy.Publisher("danger_states",DangerStates, queue_size=1)
        self.danger_alert_publisher = rospy.Publisher("danger_back",String, queue_size=1)
        self.obs_sub = rospy.Subscriber('/raw_obstacles', Obstacles, self.obstacles_callback, queue_size=1)
        self.states_sub = rospy.Subscriber('/pitakuru_states', States, self.states_callback, queue_size=1)
        self.front_detection = 1.1 #rospy.get_param("/obj_track/front_detection")
        self.side_detection = 0.4 #rospy.get_param("/obj_track/side_detection")
        self.saved_circle_points = []
        self.saved_segment_points = []
        self.last_state = "IDLE"
        self.msg = String()
        self.msg.data = "Clear"
        self.state_changed = False
        self.has_shelf_back = False
        self.num_points_inside_shelf_area = 0


    def states_callback(self,states):
        if states.state != self.last_state and states.state != "DANGER":
            self.num_points_inside_shelf_area = 0
            self.has_shelf_back = False
            self.state_changed = True
            self.last_state = states.state
            self.saved_circle_points = []
            self.saved_segment_points = []
            


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
        y_point_interpolation = interp1d(x_points_segment, y_points_segment) #object cointains interpolation
        for x_point_interpolation in x_for_interpolation:
            points_interpolated.append( ( x_point_interpolation , float( y_point_interpolation( x_point_interpolation ) ) ) )

        return points_interpolated

    def is_point_inside_shelf_area(self, pointx, pointy):
        is_inside_shelf_area = False
        dist = np.sqrt(pointx * pointx + pointy * pointy)
        angle = np.arctan2(pointy , pointx)
        #print("dist shelf", dist, "num_points",self.num_points_inside_shelf_area, "angle",angle)
        
        if dist > DISTANCE_BACK_SHELF_MIN  and dist < DISTANCE_BACK_SHELF_MAX: # is inside circular area "Donut"
            if angle < ANGLE_REGION_MIN or angle > ANGLE_REGION_MAX:
                is_inside_shelf_area = True
        
        return is_inside_shelf_area
        
    def is_point_inside_determined_area(self, pointx, pointy):
        is_inside_area = False
        dist = np.sqrt(pointx * pointx + pointy * pointy)
        angle = np.arctan2(pointy , pointx)
        
        if dist > MIN_DISTANCE_INSIDE_AREA and dist < MAX_DISTANCE_INSIDE_AREA: # is inside circular area "Donut"
            if angle < ANGLE_REGION_MIN or angle > ANGLE_REGION_MAX:
                is_inside_area = True                
        
        return is_inside_area

    def is_inside_danger_area_circles(self,circle):
        is_circle_inside = False
        if self.is_point_inside_determined_area(circle.center.x,circle.center.y):
            is_circle_inside = True
        if self.is_point_inside_shelf_area(circle.center.x, circle.center.y):
            self.num_points_inside_shelf_area = self.num_points_inside_shelf_area + 1
            
        return is_circle_inside

    def is_inside_danger_area_segment(self,segment_points):
        found_point_inside_danger_area = False
        for point in segment_points:
            x_point = point[0]
            y_point = point[1]
            if self.is_point_inside_determined_area(x_point,y_point):
                found_point_inside_danger_area = True
            if self.is_point_inside_shelf_area(x_point,y_point):
                self.num_points_inside_shelf_area = self.num_points_inside_shelf_area + 1
        return found_point_inside_danger_area

        
    # data : Obstacles(segments, circles)
    def obstacles_callback(self, data):
        self.msg.data = "Clear"
        
        if self.state_changed:   
            # To save elements already in the zone
            for circle in data.circles:
                if self.is_inside_danger_area_circles(circle): #chack if circle is in area
                    self.saved_circle_points.append((circle.center.x , circle.center.y))

            for segment in data.segments:
                points_in_segment = self.calculate_points(segment) # list of points in segment
                if self.is_inside_danger_area_segment(points_in_segment): # check if segment is in area
                    self.saved_segment_points.append((segment.first_point.x , segment.first_point.y , segment.last_point.x , segment.last_point.y))                            
            self.state_changed = False
            print("num_pts", self.num_points_inside_shelf_area)
            if self.num_points_inside_shelf_area >= NUM_POINTS_TO_DETECT_SHELF:
                self.has_shelf_back = True
                print("shelf detected")
            else:
                print("shelf not detected")

        
        #check every circle and segment if was prevoiulsy seen
        if not self.has_shelf_back:
            for circle in data.circles:
                if self.is_inside_danger_area_circles(circle):
                    if len(self.saved_circle_points) > 0:
                        if not self.is_in_list_circle(circle , self.saved_circle_points):
                            self.msg.data = "Danger" #not found in list
                    else: # no prevously seen in list
                        self.msg.data = "Danger"

            for segment in data.segments:
                points_in_segment = self.calculate_points(segment) # list of points in segment
                if self.is_inside_danger_area_segment(points_in_segment):
                    if len(self.saved_segment_points) > 0:
                        if not self.is_in_list_segment(segment, self.saved_segment_points):                            
                            self.msg.data = "Danger" # new segment not in list
                    else: #no previous elements in list
                        self.msg.data = "Danger"
        
        self.danger_alert_publisher.publish(self.msg)

    def is_in_list_circle(self,circle,list_of_point_saved):
        is_listed_circle = False
        for element in list_of_point_saved:
            if self.is_similar_circle(circle , element):
                is_listed_circle = True #found similar circle in list
        return is_listed_circle

    def is_in_list_segment(self,segment,list_of_segment_saved):
        is_listed = False
        for element in list_of_segment_saved:
            if self.is_similar_segment(segment , element):
                is_listed = True #found similar segment in list
        return is_listed

    # To check if objesct is similar to one element in the list
    def is_similar_segment(self,segment,element):
        is_similar_segment = False
        ex_first = float(element[0]) - segment.first_point.x
        ey_first = float(element[1]) - segment.first_point.y
        ex_last  = float(element[2]) - segment.last_point.x
        ey_last  = float(element[3]) - segment.last_point.y

        if np.absolute(ex_first) < RADIUS_SIMILARITY and np.absolute(ey_first) < RADIUS_SIMILARITY and np.absolute(ex_last) < RADIUS_SIMILARITY and np.absolute(ey_last) < RADIUS_SIMILARITY:
            is_similar_segment = True

        return is_similar_segment

    # To check if objesct is similar to one element in the list
    def is_similar_circle(self,circle,saved_list): 
        is_similar = False
        ex_ = float(saved_list[0]) - circle.center.x
        ey_ = float(saved_list[1]) - circle.center.y

        if np.absolute(ex_) < RADIUS_SIMILARITY and np.absolute(ey_) < RADIUS_SIMILARITY:
            is_similar = True

        return is_similar

    def shutdown(self):
        rospy.sleep(1)
        

def segment_obstacle_main():
    print("segments_obstacles_danger")
    rospy.init_node('peop_lidar_obj', anonymous = True)
    segments_obst_obj = SegmentExtractor()
    while not rospy.is_shutdown():
        sleep(SLEEP_TIME)

if __name__=='__main__':
    segment_obstacle_main()