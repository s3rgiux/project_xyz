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


class PitWheels:
    def __init__(self):
        self.ang_pub = rospy.Publisher("/peop_ang_yolo", Vector3, queue_size=2)
        
        # tracking target Vector3(x:orig_x, y:orig_y, z:flag_tracking_or_not, if it is positive then tracking) detected with LiDAR
        rospy.Subscriber('/tracked', Vector3, self.tracked_callback, queue_size=2)
        # detected peoples with YOLO and SORT
        rospy.Subscriber('/peoples_sorted_tracked', peoples, self.peoples_sort_callback, queue_size=2)
        # this state is used to know that current state is karugamo or not.
        rospy.Subscriber('/pitakuru_states', States, self.states_callback, queue_size=1)

        self.ang_dist = Vector3()
        self.tracked_x = -50
        self.tracked_y = -50
        self.tracked_ang = 0
        self.first_got = False
        self.prev_cx = 0
        self.prev_cy = 0
        self.pixels_radius = 45
        self.lost_count = 0
        self.dist_estim = 0
        self.last_time = time.time()
        self.biggest_people = people_box()
        self.biggest_people.id = -1

        self.reset_karugamo_state()


    def pubobs(self):
        if(time.time()-self.last_time>0.4):
            self.ang_dist.x=-1
            self.ang_dist.y=-0.01
            self.ang_dist.z=-500
            self.ang_pub.publish(self.ang_dist)
            self.is_tracking_yolo=False
            self.first_got=False
            self.lost_count=0
            self.dist_estim=0
            self.last_time=time.time()
            self.biggest_people.id=-1
            self.is_tracking_lidar=False
            
    
    def states_callback(self, states):
        if states.state == 'KARUGAMO':
            # tracking with only LiDAR
            if states.state_karugamo == "tracking_lidar":
                self.is_tracking_lidar = True
                self.tracking_lidar_angle = states.trackeds.linear.y
            # lost with YOLO and LiDAR
            if states.state_karugamo == "losting_with_lidar" and not self.is_tracking_yolo:
                self.is_tracking_lidar = False
                if self.biggest_people.id != -1 and self.biggest_people.area > 40:
                    self.previous_tracking_lidar_angle = self.tracked_ang
                    self.is_tracking_yolo = True
                    self.first_got = True
                    self.tracking_yolo_id = self.biggest_people.id
        else:
            # reset all variable if the state changes to not karugamo
            self.reset_karugamo_state()
    

    def reset_karugamo_state(self):
        # LiDAR variable
        self.is_tracking_lidar = False
        self.tracking_lidar_angle = 0
        self.previous_tracking_lidar_angle = 0
        # YOLO variable
        self.is_tracking_yolo = False
        self.tracking_yolo_id = -1
        # 
        self.first_got = False

    def peoples_sort_callback(self,data):
        biggest=people_box()
        biggest.id==-1
        area_aux=000
        for n in data.people:
            if self.first_got and self.tracking_yolo_id==n.id:
                    center_x=(n.xmax+n.xmin)/2
                    center_y=(n.ymax+n.ymin)/2
                    auxx=320-center_x
                    auxy=480-center_y
                    ang = np.arctan2(auxx, auxy) * 180 / np.pi
                    self.lost_count=0
                    
                    alf=0.69
                    estim=1/(((n.xmax-n.xmin)*(n.ymax-n.ymin))/100000)
                    self.dist_estim=(alf*self.dist_estim)+((1-alf)*estim)
                    self.ang_dist.x=1
                    self.ang_dist.y=self.dist_estim
                    self.ang_dist.z=ang
                    self.previous_tracking_lidar_angle = self.tracked_ang
                    self.ang_pub.publish(self.ang_dist)
                    self.lost_count=0
                    self.last_time=time.time()
                    return
            elif(n.area>area_aux and int(n.id)!=-1):
                area_aux=n.area
                biggest=n
                self.biggest_people=biggest
                self.last_time=time.time()
        if(biggest.id>0):
            center_x=(biggest.xmax+biggest.xmin)/2
            center_y=(biggest.ymax+biggest.ymin)/2
            auxx=320-center_x
            auxy=480-center_y
            ang = np.arctan2(auxx, auxy) * 180 / np.pi

            if(self.is_tracking_lidar and self.first_got== False):
                if np.abs(ang-self.tracking_lidar_angle)<10 and self.biggest_people.area>40:
                    self.previous_tracking_lidar_angle = self.tracked_ang
                    self.is_tracking_yolo = True
                    self.first_got = True
                    self.tracking_yolo_id = self.biggest_people.id
            if self.first_got== False and self.is_tracking_yolo :
                self.first_got=True
                self.tracking_yolo_id= biggest.id
                self.lost_count=0
                self.last_time=time.time()

    def sort_callback(self,data):
        rcv=data.data
        xmin=rcv[0]
        ymin=rcv[1]
        xmax=rcv[2]
        ymax=rcv[3]
        identif =rcv[4]
        area=rcv[5]
        
        if(identif!=-1 ):
            center_x=(xmax+xmin)/2
            center_y=(ymax+ymin)/2
            auxx=320-center_x
            auxy=480-center_y
            ang = np.arctan2(auxx, auxy) * 180 / np.pi
            if not self.first_got and self.is_tracking_yolo and self.tracked_x != -50 and self.tracked_y != -50 and self.tracked_ang < (self.tracked_ang + 7) and self.tracked_ang > (self.tracked_ang - 7) :
                self.first_got=True
                self.tracking_yolo_id= identif
                self.lost_count=0
            elif self.first_got and self.tracking_yolo_id==identif:
                self.lost_count=0
                alf=0.69
                estim=1/(((xmax-xmin)*(ymax-ymin))/100000)
                self.dist_estim=(alf*self.dist_estim)+((1-alf)*estim)
                self.ang_dist.x=1
                self.ang_dist.y=self.dist_estim
                self.ang_dist.z=ang
                self.previous_tracking_lidar_angle = self.tracked_ang
                self.ang_pub.publish(self.ang_dist)
                self.lost_count=0
                self.last_time=time.time()
            else:
                self.lost_count=self.lost_count+1
                if(self.lost_count>7):
                    self.lost_count=0
                    self.first_got=False
                    self.dist_estim=0
                if self.first_got==False:
                    self.ang_dist.x=-1
                    self.ang_dist.y=0
                    self.ang_dist.z=ang
                    self.ang_pub.publish(self.ang_dist)
                    self.lost_count=self.lost_count=+1
                self.last_time=time.time()

    def tracked_callback(self,data):
        self.tracked_x=data.x
        self.tracked_y=data.y
        self.tracked_ang=data.z
        if self.tracked_x != -50 and self.tracked_y != -50 and self.is_tracking_yolo==False:
            self.previous_tracking_lidar_angle = self.tracked_ang
            self.is_tracking_yolo=True
            

    def boundings_callback(self, data):
        lst = []
        cnt=0
        cnt2=0
        width=640
        height=480
        for x in data.bounding_boxes:
            if x.Class=="person":
                center_x=(x.xmax+x.xmin)/2
                center_y=(x.ymax+x.ymin)/2
                auxx=320-center_x
                auxy=480-center_y
                ang = np.arctan2(auxx, auxy) * 180 / np.pi
                cnt2=cnt2+1
                
                if self.first_got== False and self.is_tracking_yolo and self.tracked_ang < (self.tracked_ang + 7) and self.tracked_ang > (self.tracked_ang - 7) :
                    self.first_got=True
                    self.prev_cx=center_x
                    self.prev_cy=center_y
                    self.previous_tracking_lidar_angle = self.tracked_ang
                    self.dist_estim=0
                elif self.first_got and self.is_tracking_yolo and center_x < self.prev_cx+ self.pixels_radius and center_x > self.prev_cx- self.pixels_radius and center_y<self.prev_cy+self.pixels_radius and center_y>self.prev_cy-self.pixels_radius:
                    alf=0.65
                    estim=1/(((x.xmax-x.xmin)*(x.ymax-x.ymin))/100000)
                    self.dist_estim=(alf*self.dist_estim)+((1-alf)*estim)
                    self.prev_cx=center_x
                    self.prev_cy=center_y
                    self.ang_dist.x=1
                    self.ang_dist.y=self.dist_estim
                    self.ang_dist.z=ang
                    self.previous_tracking_lidar_angle = self.tracked_ang
                    self.ang_pub.publish(self.ang_dist)
                    self.lost_count=0
                else:
                    self.ang_dist.x=-1
                    self.ang_dist.y=0
                    self.ang_dist.z=ang
                    self.ang_pub.publish(self.ang_dist)
                    self.lost_count=self.lost_count=+1
                    if(self.lost_count>4):
                        self.lost_count=0
                        self.first_got=False
                        self.dist_estim=0
                self.last_time=time.time()
        closest= Vector3()
        aux=[10000,10000]
        val_aux=10000
        ang_aux=1500
        lst2 = []
        dst_aux=150000
        if len(lst)!=0:
            for n in (lst):
                e_x=np.abs(self.tracked_x-n.center.x)
                e_y=np.abs(self.tracked_y-n.center.y)
                dist=np.sqrt(e_x*e_x+e_y*e_y)
                ang_obj= 90+np.arctan2(n.center.x, n.center.y) * 180 / np.pi
                err_ang= self.tracked_ang-ang_obj
                if dist<val_aux and err_ang<ang_aux: 
                    val_aux=dist
                    ang_aux=err_ang
                    lst2.append(n)
            if len(lst2)!=0:
                for n in (lst2):
                    dist=np.sqrt(n.center.x*n.center.x+n.center.y*n.center.y)
                    if dist<dst_aux: 
                        dst_aux=dist
                        closest.x=n.center.x
                        closest.y=n.center.y
                self.ang_pub.publish(closest)

    def shutdown(self):
        rospy.sleep(1)


def pit_wheels_main():
    rospy.init_node('pit_wheels', anonymous = True)
    pit_wheels = PitWheels()

    while not rospy.is_shutdown():
        pit_wheels.pubobs()
        sleep(SLEEP_TIME)

if __name__=='__main__':
    pit_wheels_main()
