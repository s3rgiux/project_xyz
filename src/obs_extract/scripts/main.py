#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import sys,time
from math import sqrt, cos, sin
import rospy
#import tf,tf2_ros
import numpy as np
from time import sleep
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import Float32
from std_msgs.msg import *
from geometry_msgs.msg import Point, Vector3, PoseWithCovarianceStamped


from obs_extract.msg import Obstacles


import struct
import time
import rosparam
#params = rosparam.get_param("/km_dolly_wheels")
#if params['connect_mode']=='ble':
#    from pykeigan import blecontroller
#    SLEEP_TIME = 0.01
#else:
#    from pykeigan import usbcontroller
#    SLEEP_TIME = 0.1
import atexit


SLEEP_TIME = 0.019
#200mm diameter0


class PitWheels:
    def __init__(self):
        print("Obstacle_extarctor")
        #rospy.loginfo("Connected to Right Wheel")
        #self.brinco=False
        self.obst_pub = rospy.Publisher('obstacle_closest', Float32, queue_size=1)
        #self.ang_pub = rospy.Publisher("peopAng2",Float32, queue_size=1)
        self.ang_pub = rospy.Publisher("peopAng2",Vector3, queue_size=4)
        rospy.Subscriber('/ang_peop_detect_img', Float32, self.ang_cam_callback, queue_size=1)
        self.dist_pub = rospy.Publisher("peopDist2",Float32, queue_size=1)
        #rospy.Subscriber('/cmd_vel', Twist, self.teleop_callback, queue_size=1)
        rospy.Subscriber('/obstacles', Obstacles, self.obstacles_callback, queue_size=1)
        rospy.Subscriber('/tracked', Vector3, self.tracked_callback, queue_size=2)
        rospy.Subscriber('/peop_ang_yolo', Vector3, self.yolo_callback, queue_size=1)
        #rospy.Subscriber('/euler2', Float64, self.angle_callback, queue_size=1)
        self.obsta  = Float32()
        self.detected=0
        self.track=0
        self.angulo= Float32()
        self.distancia= Float32()
        self.ang_dist= Vector3()
        self.tracked_obj= Vector3()
        self.front_detection = rospy.get_param("/obj_track/front_detection")
        self.side_detection = rospy.get_param("/obj_track/side_detection")
        self.timex=0
        self.last_time=0
        self.first_detection=False
	self.tracked=False
        self.ang_cam=-500
        self.tracked_x=-50
        self.tracked_y=-50
	self.tracked_ang=0
        self.radius_follow=0.35
        self.yolo_status=0
        self.yolo_dist =0
        self.yolo_ang=0
        self.last_time_tracked=0
    
    def pubobs(self):
        if(time.time()-self.last_time>0.4):
        #if(self.track==0):
            self.angulo.data=-500
            self.ang_dist.x=-0.01
            self.ang_dist.y=-0.01
            self.ang_dist.z=-0.01
            self.distancia.data=0
            self.ang_pub.publish(self.ang_dist)
            #self.dist_pub.publish(self.distancia)
    
    def ang_cam_callback(self,data):
        self.ang_cam=data.data

    def tracked_callback(self,data):
        self.tracked_x=data.x
        self.tracked_y=data.y
        self.tracked_ang=data.z

    def yolo_callback(self,data):
        self.yolo_status=data.x
        self.yolo_dist=data.y
        self.yolo_ang=data.z

    def obstacles_callback(self, data):
        lst = []
        for x in data.circles:
            if x.center.x>-0.5 and x.center.x<self.front_detection and x.center.y<self.side_detection and x.center.y>-self.side_detection: 
                #print("#########")
                #circles = data.circles
                #print(circles)
                #self.obsta.data = 1
                #self.detected = 1
                #self.obst_pub.publish(self.obsta)               
                ang = 90-np.arctan2(x.center.x, x.center.y) * 180 / np.pi
                dist =np.sqrt(x.center.x*x.center.x+x.center.y*x.center.y)
                #print(ang)
                #print(dist*120)
                #track=1
                self.angulo.data=ang
                self.distancia.data=dist*100
                #self.ang_dist.x=ang
                #self.ang_dist.y=dist*100
                
                if self.tracked_x != -50 and self.tracked_y != -50 and x.center.x<=(self.tracked_x+self.radius_follow) and x.center.x>=(self.tracked_x-self.radius_follow) and x.center.y <=(self.tracked_y+self.radius_follow) and x.center.y >=(self.tracked_y-self.radius_follow):#then we have tracked object
                    lst.append(x)
                    #self.ang_dist.x=x.center.x
                    #self.ang_dist.y=x.center.y#dist*100
                    #self.ang_pub.publish(self.ang_dist)
                #else:
                elif self.tracked_x == -50 and self.tracked_y == -50 or (time.time()-self.last_time_tracked)>0.25:
                    self.ang_dist.x=x.center.x
                    self.ang_dist.y=x.center.y#dist*100
                    self.ang_dist.z=-1#dist*100
                    self.ang_pub.publish(self.ang_dist)

                #self.ang_pub.publish(self.angulo)
                #self.dist_pub.publish(self.distancia)
                #print(x)
                
                self.last_time=time.time()#self.timex
        closest= Vector3() 
        aux=[10000,10000]
        val_aux=0.5
        ang_aux=30
        lst2 = []
        dst_aux=150000
        if len(lst)!=0:
            for n in (lst):
                e_x=np.abs(self.tracked_x-n.center.x)
                e_y=np.abs(self.tracked_y-n.center.y)
                dist=np.sqrt(e_x*e_x+e_y*e_y)
                ang_obj= 90-np.arctan2(n.center.x, n.center.y) * 180 / np.pi
                err_ang= np.abs(self.tracked_ang-ang_obj)
                if dist<val_aux and err_ang<ang_aux: #and err_ang<7 and err_ang>-7 :
                    val_aux=dist
                    ang_aux=err_ang
                    #closest.x=n.center.x
                    #closest.y=n.center.y
                    lst2.append(n)
            if len(lst2)!=0:
                for n in (lst2):
                    dist=np.sqrt(n.center.x*n.center.x+n.center.y*n.center.y)
                    ang_obj= 90-np.arctan2(n.center.x, n.center.y) * 180 / np.pi
                    err_ang= np.abs(self.tracked_ang-ang_obj)
                    if err_ang<ang_aux: #and err_ang<7 and err_ang>-7 :
                        val_aux=dist
                        ng_aux=err_ang
                    if dist<dst_aux: #and err_ang<7 and err_ang>-7 :
                        dst_aux=dist
                        closest.x=n.center.x
                        closest.y=n.center.y
                        closest.z=1#dist*100
                        self.last_time_tracked=time.time()
                self.ang_pub.publish(closest)        
                #print("HHHHH")
                #print(closest.x)
                #print(closest.y)
            #print(lst)           
    
    

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
