#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import rospy
import time
from time import sleep
from std_msgs.msg import String
from std_msgs.msg import Int16
from segement_obstacle_danger.msg import Obstacles, States , DangerStates
from scipy.interpolate import interp1d
import numpy as np
from sensor_msgs.msg import LaserScan

SLEEP_TIME = 0.001
MIN_X_INSIDE_AREA = 0.3 #0.3 #meters
MAX_X_INSIDE_AREA = 0.9 #1.1 #meters
MIN_Y_INSIDE_AREA = -0.35 #0.3 #meters
MAX_Y_INSIDE_AREA = 0.35 #1.1 #meters




MIN_ANGLE = -3.12413907051
MAX_ANGLE = 3.14159274101
STEPS = 2880 #360*4 #1440
ANGLE_INCREMENT = float(1/STEPS) #resolution
TIME_INCREMENT = 0.003 
RANGE_MIN = 0.37
RANGE_MAX = 1.5


class PointsDanger:
    def __init__(self):
        print("Segements_obtacles")
        #self.danger_alert_publisher = rospy.Publisher("danger_states",DangerStates, queue_size=1)
        self.danger_alert_publisher = rospy.Publisher("Danger",String, queue_size=1)
        self.sound_alert_publisher = rospy.Publisher("alerts",Int16, queue_size=1)
        self.laser_sub = rospy.Subscriber('/scan_merged', LaserScan, self.laser_callback, queue_size=1)
        self.states_sub = rospy.Subscriber('/pitakuru_states', States, self.states_callback, queue_size=1)
        self.front_detection = 1.1 #rospy.get_param("/obj_track/front_detection")
        self.side_detection = 0.4 #rospy.get_param("/obj_track/side_detection")
        self.saved_circle_points = []
        self.saved_segment_points = []
        self.last_state = "IDLE"
        self.current_state = "IDLE"
        self.msg = String()
        self.msg.data = "Clear"
        self.state_changed = False
        self.has_shelf_back = False
        self.num_points_inside_shelf_area = 0

    def laser_callback(self,laser):
        self.msg.data = "Clear"
        found_points = self.check_if_points_are_inside_area(laser, 2 )
        if found_points:
            self.msg.data = "Danger"
        self.danger_alert_publisher.publish(self.msg)
                    
    
    def check_if_points_are_inside_area(self,laser,num_points_trigger):
        found_points_inside_area = False
        counter__points_inside = 0
        for i , theta in enumerate(np.arange(laser.angle_min, laser.angle_max, laser.angle_increment)):
            if not np.isinf(laser.ranges[i]) and laser.ranges[i] > RANGE_MIN and laser.ranges[i] < RANGE_MAX:
                
                y = -laser.ranges[i] * np.sin(theta)
                x = -laser.ranges[i] * np.cos(theta)
                #chececk if point is in danger zone defines as rectangle
                if x > MIN_X_INSIDE_AREA and x < MAX_X_INSIDE_AREA and y > MIN_Y_INSIDE_AREA and y < MAX_Y_INSIDE_AREA:#region danger
                    counter__points_inside = counter__points_inside + 1
                    if counter__points_inside >= num_points_trigger:
                        found_points_inside_area = True
                        break

        return found_points_inside_area

    def states_callback(self,states):
        if states.state != self.last_state and states.state != "DANGER":
            self.current_state = states.state
            self.num_points_inside_shelf_area = 0
            self.has_shelf_back = False
            self.state_changed = True
            self.last_state = states.state
            self.saved_circle_points = []
            self.saved_segment_points = []
                    
    
    def shutdown(self):
        rospy.sleep(1)
        

def raw_points_obstacle_main():
    print("raw_points_obstacle_danger")
    rospy.init_node('lidar_danger', anonymous = True)
    segments_obst_obj = PointsDanger()
    while not rospy.is_shutdown():
        sleep(SLEEP_TIME)

if __name__=='__main__':
    raw_points_obstacle_main()