#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import time
from math import sqrt
import rospy
import numpy as np
from time import sleep
from std_msgs.msg import Float32
from std_msgs.msg import *
from geometry_msgs.msg import Vector3
from peop_extract.msg import people_box, peoples, States


SLEEP_TIME = 0.018
BBOX_SIZE_THRESH = 40 # if bbox is larger than this, then it may be people.
ERROR_LIDAR_DISTGANCE = -0.050 # if lidar could not detect the target, then return this position value
CAMERA_POSITION_X = 640 / 2 # center of camera frame in x-axis
CAMERA_POSITION_Y = 480 # camera frame height
POSITION_UPDATE_RATE = 0.69
BASE_BBOX_AREA_DISTANCE = 100000
YOLO_LIDAR_MATCH_ANGLE = 10


class PeopleExtractSort:
    def __init__(self):
        # tracking target Vector3(x:[1-tracking, -1-not_tracking], y:distance[m], z:angle[degree]) with YOLO
        self.people_position_publisher = rospy.Publisher("/peop_ang_yolo", Vector3, queue_size=2)
        
        # tracking target Vector3(x:orig_x, y:orig_y, z:angular, in other nodes, usually this is used as flag_tracking_or_not, if it is positive then tracking) detected with LiDAR
        rospy.Subscriber('/tracked', Vector3, self.tracked_callback, queue_size=2)
        # detected peoples with YOLO and SORT
        rospy.Subscriber('/peoples_sorted_tracked', peoples, self.peoples_sort_callback, queue_size=2)
        # this state is used to know that current state is karugamo or not.
        rospy.Subscriber('/pitakuru_states', States, self.states_callback, queue_size=1)

        self.ang_dist = Vector3()
        self.latest_tracking_lidar_x = ERROR_LIDAR_DISTGANCE
        self.latest_tracking_lidar_y = ERROR_LIDAR_DISTGANCE
        self.latest_tracking_lidar_angle = 0
        self.has_detected_people = False
        self.lost_count_before_reset = 0
        self.last_estimated_distance = 0
        self.last_time_detected_yolo = time.time()
        self.current_biggest_people = people_box()
        self.current_biggest_people.id = -1

        self.reset_karugamo_state()


    def pubobs(self):
        if time.time() - self.last_time_detected_yolo > 0.4:
            # lost
            self.ang_dist.x = -1
            self.ang_dist.y = -0.01
            self.ang_dist.z = -500
            self.people_position_publisher.publish(self.ang_dist)

            self.is_tracking_yolo = False
            self.has_detected_people = False
            self.lost_count_before_reset = 0
            self.last_estimated_distance = 0
            self.last_time_detected_yolo = time.time()
            self.current_biggest_people.id = -1
            self.is_tracking_lidar = False

    def reset_karugamo_state(self):
        # LiDAR variable
        self.is_tracking_lidar = False
        self.tracking_lidar_angle = 0
        self.last_tracking_lidar_angle = 0
        # YOLO variable
        self.is_tracking_yolo = False
        self.tracking_yolo_id = -1
        self.has_detected_people = False

    
    def states_callback(self, states):
        if states.state == 'KARUGAMO':
            # tracking with only LiDAR
            if states.state_karugamo == "tracking_lidar":
                self.is_tracking_lidar = True
                self.tracking_lidar_angle = states.trackeds.linear.y
            # lost with LiDAR and not ready to track with YOLO
            if states.state_karugamo == "losting_with_lidar" and not self.is_tracking_yolo:
                self.is_tracking_lidar = False
                # but if YOLO "detects" people
                if self.is_people(self.current_biggest_people):
                    # save latest lidar angle on losting target with LiDAR
                    self.last_tracking_lidar_angle = self.latest_tracking_lidar_angle
                    # lidar lost but start to track only YOLO
                    self.is_tracking_yolo = True
                    self.has_detected_people = True
                    self.tracking_yolo_id = int(self.current_biggest_people.id)
        else:
            # reset all variable if the state changes to not karugamo
            self.reset_karugamo_state()
    
    def is_people(self, people):
        return people.id != -1 and people.area > BBOX_SIZE_THRESH

    def is_tracking_bbox(self, detected_bbox):
        return self.tracking_yolo_id == int(detected_bbox.id)
    
    def center(self,bbox):
        return (bbox.xmax + bbox.xmin) / 2, (bbox.ymax + bbox.ymin) / 2
    
    # return angle from camera in degree
    def bbox_angle_from_camera(self,bbox):
        center_x, center_y = self.center(bbox)
        diff_x = CAMERA_POSITION_X - center_x
        diff_y = CAMERA_POSITION_Y - center_y
        angle_degree = np.arctan2(diff_x, diff_y) * 180 / np.pi
        return angle_degree

    def is_same_lidar_yolo_target(self,yolo_target_angle, lidar_target_angle):
        return np.abs(yolo_target_angle - lidar_target_angle) < YOLO_LIDAR_MATCH_ANGLE

    def peoples_sort_callback(self, data):
        biggest_bbox = None
        curent_biggest_area = 0
        
        people = [detected_bbox for detected_bbox in data.people if int(detected_bbox.id) != -1]
        for detected_bbox in people:
            # found target with yolo
            if self.has_detected_people and self.is_tracking_bbox(detected_bbox):
                angle_degree = self.bbox_angle_from_camera(detected_bbox)

                # estimate target distance from bounding box area
                bbox_width = detected_bbox.xmax - detected_bbox.xmin
                bbox_height = detected_bbox.ymax - detected_bbox.ymin
                estimated_distance = BASE_BBOX_AREA_DISTANCE / (bbox_width * bbox_height)
                self.last_estimated_distance = (POSITION_UPDATE_RATE * self.last_estimated_distance) + ((1 - POSITION_UPDATE_RATE) * estimated_distance)

                # publish target position with YOLO
                self.ang_dist.x = 1 # flag, success to tracking
                self.ang_dist.y = self.last_estimated_distance
                self.ang_dist.z = angle_degree
                self.people_position_publisher.publish(self.ang_dist)

                # [TODO] remove this line if it works without this line
                self.last_tracking_lidar_angle = self.latest_tracking_lidar_angle

                # reset lost count
                self.lost_count_before_reset = 0
                self.last_time_detected_yolo = time.time()
                return

            elif detected_bbox.area > curent_biggest_area:
                curent_biggest_area = detected_bbox.area
                biggest_bbox = detected_bbox

        # could not find target bounding box id, but found biggest bounding box with another id
        if biggest_bbox:
            self.current_biggest_people = biggest_bbox
            self.last_time_detected_yolo = time.time()

            angle_degree = self.bbox_angle_from_camera(biggest_bbox)

            # if it tracks with lidar and have not detecterd with yolo
            # and the biggest bbox is like target
            if self.is_tracking_lidar and \
                not self.has_detected_people and \
                self.is_same_lidar_yolo_target(angle_degree, self.tracking_lidar_angle) and \
                self.current_biggest_people.area > BBOX_SIZE_THRESH:
                    self.last_tracking_lidar_angle = self.latest_tracking_lidar_angle
                    self.is_tracking_yolo = True
                    self.has_detected_people = True
                    self.tracking_yolo_id = self.current_biggest_people.id
                    self.last_time_detected_yolo = time.time()

            # if lidar detects then the state transit
            if not self.has_detected_people and not self.is_tracking_yolo:
                #self.has_detected_people = True
                self.tracking_yolo_id = biggest_bbox.id
                self.lost_count_before_reset = 0
                self.last_time_detected_yolo = time.time()
            
            else:
                self.lost_count_before_reset += 1
                if self.lost_count_before_reset > 7:
                    self.lost_count_before_reset = 0
                    self.has_detected_people = False
                    self.last_estimated_distance = 0
                if not self.has_detected_people:
                    # publish biggest people not tracked YOLO
                    self.ang_dist.x = -biggest_bbox.id # flag with id negative not tracking 
                    self.ang_dist.y = 0 
                    self.ang_dist.z = angle_degree
                    self.people_position_publisher.publish(self.ang_dist)
                self.last_time_detected_yolo=time.time()


    def did_success_detection(self, position):
        return position.x != ERROR_LIDAR_DISTGANCE and position.y != ERROR_LIDAR_DISTGANCE

    def tracked_callback(self,data):
        # store latest tracking position with lidar
        self.latest_tracking_lidar_x = data.x
        self.latest_tracking_lidar_y = data.y
        self.latest_tracking_lidar_angle = data.z

        if self.did_success_detection(data) and not self.is_tracking_yolo:
            # start to track with yolo
            self.last_tracking_lidar_angle = self.latest_tracking_lidar_angle
            self.is_tracking_yolo = True

    def shutdown(self):
        rospy.sleep(1)


def pit_wheels_main():
    rospy.init_node('pit_wheels', anonymous=True)
    people_extract_sort = PeopleExtractSort()

    while not rospy.is_shutdown():
        people_extract_sort.pubobs()
        sleep(SLEEP_TIME)

if __name__=='__main__':
    pit_wheels_main()
