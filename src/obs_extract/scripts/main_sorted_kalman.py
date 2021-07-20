#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import rospy
import numpy as np
from time import sleep
from std_msgs.msg import Float32
from std_msgs.msg import *
from geometry_msgs.msg import  Vector3
from obs_extract.msg import Obstacles,States
import time

SLEEP_TIME = 0.001

class PeopLidarExtract:
    def __init__(self):
        print("Obstacle_extarctor")
        self.ang_pub = rospy.Publisher("peopAng2",Vector3, queue_size=2)
        rospy.Subscriber('/obstacles', Obstacles, self.obstacles_callback, queue_size=1)
        rospy.Subscriber('/peop_ang_yolo', Vector3, self.yolo_callback, queue_size=1)
        rospy.Subscriber('/pitakuru_states', States, self.states_callback, queue_size=1)
        self.angulo = Float32()
        self.distancia = Float32()
        self.ang_dist = Vector3()
        self.front_detection = rospy.get_param("/obj_track/front_detection")
        self.side_detection = rospy.get_param("/obj_track/side_detection")
        self.radius_follow = rospy.get_param("/obj_track/radius_follow")
        self.last_time = 0
        self.yolo_status = 0
        self.yolo_dist  = 0
        self.yolo_ang = 0
        self.last_time_tracked = 0
        self.prev_cx = 0
        self.prev_cy = 0
        self.follow_cx = 0
        self.follow_cy = 0
        self.first_got = False
        self.received_obstacles =  Obstacles()
        self.count_to_track = 0
        self.searching = False
        self.tracked_dist = 0
        
    
    def pubobs(self):
        if(time.time() - self.last_time > 0.35):
            self.angulo.data = -500
            self.ang_dist.x = -0.01
            self.ang_dist.y = -0.01
            self.ang_dist.z = -1
            self.distancia.data = 0
            self.ang_pub.publish(self.ang_dist)
            self.first_got = False
            self.temp_cx = 0
            self.temp_cy = 0
            self.temp_dist = 5000000
            self.try_to_search = False
            self.got_obj_lidar = False

    def search_nearest(self,data):
        lst = []
        self.count_to_track = self.count_to_track+1
        self.searching = True
        print("ang_yolo")
        print(self.yolo_ang)
        for x in data.circles:
            if x.center.x > -0.5 and x.center.x < self.front_detection and x.center.y < self.side_detection and x.center.y > -self.side_detection:              
                ang  =  90-np.arctan2(x.center.x, x.center.y) * 180 / np.pi
                dist  = np.sqrt(x.center.x*x.center.x+x.center.y*x.center.y)
                if np.abs(ang-self.yolo_ang)<9:
                    lst.append(x)
        if len(lst) != 0:
            lst2 = []
            closest =  Vector3()
            for n in (lst):
                e_x = n.center.x
                e_y = n.center.y
                dist = np.sqrt(e_x*e_x+e_y*e_y)
                ang_obj =  90 - np.arctan2(n.center.x, n.center.y) * 180 / np.pi
                print("appended for sort")
                if(dist > 0.25 and dist < 4.0):
                    lst2.append((n,dist))#contains (error distancia and err ang)
                    print(e_x)
                    print(e_y)
                    print(ang_obj)
                    print(ang_obj-self.yolo_ang)
                    print(dist)
            #sort list
            lst2.sort(key = self.takeSecond)
            obj_close = lst2[0]
            closest.x = obj_close[0].center.x
            closest.y = obj_close[0].center.y
            closest.z = len(lst2)
            #####
            print("found")
            if(obj_close[1] < self.temp_dist and obj_close[1] > 0.25):
                self.temp_cx = closest.x
                self.temp_cy = closest.y
                self.temp_dist = obj_close[1]
                ang_obj =  90-np.arctan2(self.temp_cx,self.temp_cy) * 180 / np.pi
                print(self.temp_cx)
                print(self.temp_cy)
                print(ang_obj)
                print(ang_obj-self.yolo_ang)
                print(obj_close[1])

            ######
            if(self.count_to_track > 3):
                self.count_to_track = 0
                self.temp_dist = 50000
                self.follow_cx = closest.x
                self.follow_cy = closest.y
                print("enviados primera vez")
                print(self.follow_cx)
                print(self.follow_cy)
                
                self.prev_cx = closest.x
                self.prev_cy = closest.y
                self.last_time_tracked = time.time()
                self.ang_pub.publish(closest)

                self.first_got = True
                self.searching = False
                self.try_to_search = False
                dist3  = np.sqrt(closest.x*closest.x+closest.y*closest.y)
                self.tracked_dist = dist3
                

    def states_callback(self,states):
        #if states.state=="KARUGAMO" and states.state_karugamo=="losting_with_lidar" and self.first_got==False and self.try_to_search==False and self.yolo_ang!=-500:
        if states.state == "KARUGAMO" and states.state_karugamo == "losting_with_lidar" and self.try_to_search == False and self.yolo_ang != -500:
            print("searching the nearest")
            self.try_to_search = True
            self.got_obj_lidar = False
            self.first_got = False

        elif states.state == "KARUGAMO" and states.state_karugamo == "tracking_lidar" and self.try_to_search == False and self.yolo_status > 0:    
            self.got_obj_lidar=True

        elif states.state != "KARUGAMO":
            print("removed first got")
            self.first_got = False
            self.got_obj_lidar = False
            self.follow_cx = 0
            self.follow_cy = 0


    def yolo_callback(self,data):
        self.yolo_status = data.x
        self.yolo_dist = data.y
        self.yolo_ang = data.z

    def takeSecond(self,elem):
        return elem[1]

    def obstacles_callback(self, data):
        self.received_obstacles = data
        if(self.try_to_search and self.yolo_ang >- 35 and self.yolo_ang < 35):
            print("sent_data")
            self.search_nearest(data)
        lst = []
        inradious = []
        if self.searching == False:
            for x in data.circles:
                if x.center.x>-0.5 and x.center.x<self.front_detection and x.center.y<self.side_detection and x.center.y>-self.side_detection:              
                    ang = 90-np.arctan2(x.center.x, x.center.y) * 180 / np.pi
                    dist = np.sqrt(x.center.x*x.center.x+x.center.y*x.center.y)
                    self.angulo.data=ang
                    self.distancia.data=dist*100
                    if self.first_got:#then we have tracked object
                        e_x = self.follow_cx-x.center.x
                        e_y = self.follow_cy-x.center.y
                        dist = np.sqrt((e_x*e_x)+(e_y*e_y))
                        dist2 = np.sqrt(x.center.x*x.center.x+x.center.y*x.center.y)
                        if(dist<self.radius_follow and np.abs(self.tracked_dist-dist2)<0.5):
                            lst.append(x)
                            new = np.array([x.center.x,x.center.y])
                            inradious.append(new.astype("float"))
                    elif (time.time()-self.last_time_tracked)>0.3:#0.55:
                        self.ang_dist.x = x.center.x
                        self.ang_dist.y = x.center.y#dist*100
                        self.ang_dist.z = -1#dist*100
                        self.ang_pub.publish(self.ang_dist)
                    self.last_time=time.time()#self.timex
            closest= Vector3()
            lst2 = []

            if len(lst)!=0:
                for n in (lst):
                    e_x = self.follow_cx-n.center.x
                    e_y = self.follow_cy-n.center.y
                    dist = np.sqrt(e_x*e_x+e_y*e_y)
                    lst2.append((n,dist))#contains (error distancia and err ang)
                #sort list
                lst2.sort(key=self.takeSecond)
                obj_close=lst2[0]

                closest.x = obj_close[0].center.x
                closest.y = obj_close[0].center.y
                self.follow_cx = closest.x
                self.follow_cy = closest.y
                closest.z = len(lst)
                
                self.prev_cx = closest.x
                self.prev_cy = closest.y

                self.last_time_tracked=time.time()
                self.ang_pub.publish(closest)
                self.tracked_dist = np.sqrt(closest.x*closest.x+closest.y*closest.y)

    def shutdown(self):
        rospy.sleep(1)
        

def peop_lidar_main():
    print("lidar_people_det")
    rospy.init_node('peop_lidar_obj', anonymous = True)
    peop_lidar_obj = PeopLidarExtract()
    while not rospy.is_shutdown():
        peop_lidar_obj.pubobs()
        sleep(SLEEP_TIME)

if __name__=='__main__':
    peop_lidar_main()
