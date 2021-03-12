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
from sort_track.msg import IntList
from peop_extract.msg import BoundingBox,BoundingBoxes
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


SLEEP_TIME = 0.018
#200mm diameter0


class PitWheels:
    def __init__(self):
        print("people_extarctor")
        #rospy.loginfo("Connected to Right Wheel")
        #self.brinco=False
        self.obst_pub = rospy.Publisher('obstacle_closest', Float32, queue_size=1)
        #self.ang_pub = rospy.Publisher("peopAng2",Float32, queue_size=1)
        self.ang_pub = rospy.Publisher("/peop_ang_yolo",Vector3, queue_size=2)
        #rospy.Subscriber('/ang_peop_detect_img', Float32, self.ang_cam_callback, queue_size=1)
        self.dist_pub = rospy.Publisher("peopDist2",Float32, queue_size=1)
        #rospy.Subscriber('/cmd_vel', Twist, self.teleop_callback, queue_size=1)
        #rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes, self.boundings_callback, queue_size=1)
        rospy.Subscriber('/tracked', Vector3, self.tracked_callback, queue_size=2)
        rospy.Subscriber('/sorted_tracked', IntList, self.sort_callback, queue_size=2)
        #rospy.Subscriber('/euler2', Float64, self.angle_callback, queue_size=1)
        self.obsta  = Float32()
        self.detected=0
        self.track=0
        self.angulo= Float32()
        self.distancia= Float32()
        self.ang_dist= Vector3()
        self.tracked_obj= Vector3()
        self.tracked_peop= Vector3()
        #self.front_detection = rospy.get_param("/obj_track/front_detection")
        #self.side_detection = rospy.get_param("/obj_track/side_detection")
        self.timex=0
        self.last_time=0
        self.first_detection=False
	self.tracked=False
        self.ang_cam=-500
        self.tracked_x=-50
        self.tracked_y=-50
	self.tracked_ang=0
        self.radius_follow=0.35
        self.tracking=False
        self.first_got=False
        self.tracked_cx=0
        self.tracked_cy=0
        self.prev_cx=0
        self.prev_cy=0
        self.tracked_id=0
        self.pixels_radius=45
        self.lost_count=0
        self.dist_estim=0
    
    def pubobs(self):
        if(time.time()-self.last_time>0.4):
        #if(self.track==0):
            self.angulo.data=-500
            self.ang_dist.x=-0.01
            self.ang_dist.y=-0.01
            self.ang_dist.z=-500
            self.distancia.data=0
            self.ang_pub.publish(self.ang_dist)
            self.tracking=False
            self.first_got=False
            self.lost_count=0
            self.dist_estim=0
            #self.dist_pub.publish(self.distancia)
    
    def sort_callback(self,data):
        rcv=data.data
        xmin=rcv[0]
        ymin=rcv[1]
        xmax=rcv[2]
        ymax=rcv[3]
        identif =rcv[4]
        if(xmin!=-1 and xmin!=-1 and xmax!=-1 and ymax!=-1 and identif!=-1 ):
            #print(rcv[0])
            center_x=(xmax+xmin)/2
            center_y=(ymax+ymin)/2
            auxx=320-center_x
            auxy=480-center_y
            ang = np.arctan2(auxx, auxy) * 180 / np.pi
            #print('{},{},{},{},{},{}'.format(xmin,ymin,xmax,ymax,identif,ang))
            #cnt2=cnt2+1
            if self.first_got== False and self.tracking and self.tracked_x != -50 and self.tracked_y != -50 and self.tracked_ang < (self.tracked_ang + 7) and self.tracked_ang > (self.tracked_ang - 7) :#then we have tracked object
                #lst.append(x)
                #print("tracking first time")
                self.first_got=True
                self.tracked_id= identif
                self.lost_count=0
                #self.prev_cx=center_x
                #self.prev_cy=center_y
                #self.prev_ang = self.tracked_ang
                #self.dist_estim=0
            #elif self.first_got and self.tracking and self.tracked_ang < (self.prev_ang + 4) and self.tracked_ang > (self.prev_ang - 4) and center_x < self.prev_cx+ self.pixels_radius and center_x > self.prev_cx- self.pixels_radius and center_y<self.prev_cy+self.pixels_radius and center_y>self.prev_cy-self.pixels_radius:#then we have tracked object
            #elif self.first_got and self.tracking and self.tracked_ang < (self.prev_ang + 9) and self.tracked_ang > (self.prev_ang - 9) and center_x < self.prev_cx+ self.pixels_radius and center_x > self.prev_cx- self.pixels_radius and center_y<self.prev_cy+self.pixels_radius and center_y>self.prev_cy-self.pixels_radius:#then we have tracked object
            elif self.first_got and self.tracked_id==identif:#then we have tracked object
                self.lost_count=0
                #print('tracking id {}'.format(identif))
                alf=0.65
                estim=1/(((xmax-xmin)*(ymax-ymin))/100000)#1/((x.xmax+x.xmin)+(x.ymax+x.ymin))
                self.dist_estim=(alf*self.dist_estim)+((1-alf)*estim)
                #print('{},{},{},{}'.format(center_x,center_y,self.tracked_ang,self.dist_estim))
                
                #self.prev_cx=center_x
                #self.prev_cy=center_y
                self.ang_dist.x=1#1identif#1 #x.center.x
                self.ang_dist.y=self.dist_estim#x.center.y#dist*100
                self.ang_dist.z=ang
                self.prev_ang = self.tracked_ang
                self.ang_pub.publish(self.ang_dist)
                self.lost_count=0
                self.last_time=time.time()#self.timex
            else:
                self.lost_count=self.lost_count+1
                if(self.lost_count>9):
                    self.lost_count=0
                    self.first_got=False
                    self.dist_estim=0
                if self.first_got==False:
                    self.ang_dist.x=-1#x.center.x
                    self.ang_dist.y=0#x.center.y#dist*100
                    self.ang_dist.z=ang
                    self.ang_pub.publish(self.ang_dist)
                    self.lost_count=self.lost_count=+1
                self.last_time=time.time()#self.timex
        

    
    def ang_cam_callback(self,data):
        self.ang_cam=data.data

    def tracked_callback(self,data):
        self.tracked_x=data.x
        self.tracked_y=data.y
        self.tracked_ang=data.z
        if self.tracked_x != -50 and self.tracked_y != -50 and self.tracking==False:
            self.prev_ang = self.tracked_ang
            self.tracking=True
            

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
                #print(ang)
                #print(center_x)
                #print(center_y)
                #print(auxx)
                #print(auxy)
                #print(ang)
                #print("encontre persona")
                cnt2=cnt2+1
                #print(cnt2)
            
                #if self.tracked_x != -50 and self.tracked_y != -50 and x.center.x<=(self.tracked_x+self.radius_follow) and x.center.x>=(self.tracked_x-self.radius_follow) and x.center.y <=(self.tracked_y+self.radius_follow) and x.center.y >=(self.tracked_y-self.radius_follow):#then we have tracked object
                if self.first_got== False and self.tracking and self.tracked_x != -50 and self.tracked_y != -50 and self.tracked_ang < (self.tracked_ang + 7) and self.tracked_ang > (self.tracked_ang - 7) :#then we have tracked object
                    #lst.append(x)
                    #print("track first time")
                    self.first_got=True
                    self.prev_cx=center_x
                    self.prev_cy=center_y
                    ##self.ang_dist.x=1#x.center.x
                    #self.ang_dist.y=1#x.center.y#dist*100
                    #self.ang_dist.z=ang
                    self.prev_ang = self.tracked_ang
                    self.dist_estim=0
                    
                    #self.ang_pub.publish(self.ang_dist)
                    #self.ang_dist.x=x.center.x
                    #self.ang_dist.y=x.center.y#dist*100
                    #self.ang_pub.publish(self.ang_dist)
                #elif self.first_got and self.tracking and self.tracked_ang < (self.prev_ang + 4) and self.tracked_ang > (self.prev_ang - 4) and center_x < self.prev_cx+ self.pixels_radius and center_x > self.prev_cx- self.pixels_radius and center_y<self.prev_cy+self.pixels_radius and center_y>self.prev_cy-self.pixels_radius:#then we have tracked object
                #elif self.first_got and self.tracking and self.tracked_ang < (self.prev_ang + 9) and self.tracked_ang > (self.prev_ang - 9) and center_x < self.prev_cx+ self.pixels_radius and center_x > self.prev_cx- self.pixels_radius and center_y<self.prev_cy+self.pixels_radius and center_y>self.prev_cy-self.pixels_radius:#then we have tracked object
                elif self.first_got and self.tracking and center_x < self.prev_cx+ self.pixels_radius and center_x > self.prev_cx- self.pixels_radius and center_y<self.prev_cy+self.pixels_radius and center_y>self.prev_cy-self.pixels_radius:#then we have tracked object
                    #lst.append(x)
                    #tracking correcto
                    #print("tracking")
                    alf=0.65
                    estim=1/(((x.xmax-x.xmin)*(x.ymax-x.ymin))/100000)#1/((x.xmax+x.xmin)+(x.ymax+x.ymin))
                    self.dist_estim=(alf*self.dist_estim)+((1-alf)*estim)
                    #print('{},{},{},{}'.format(center_x,center_y,self.tracked_ang,self.dist_estim))
                    
                    self.prev_cx=center_x
                    self.prev_cy=center_y
                    self.ang_dist.x=1#x.center.x
                    self.ang_dist.y=self.dist_estim#x.center.y#dist*100
                    self.ang_dist.z=ang
                    self.prev_ang = self.tracked_ang
                    self.ang_pub.publish(self.ang_dist)
                    self.lost_count=0
                else:
                    #print("lost")
                    #print('{} {} {}'.format(center_x,center_y,self.tracked_ang))
                    self.ang_dist.x=-1#x.center.x
                    self.ang_dist.y=0#x.center.y#dist*100
                    self.ang_dist.z=ang
                    self.ang_pub.publish(self.ang_dist)
                    self.lost_count=self.lost_count=+1
                    if(self.lost_count>4):
                        self.lost_count=0
                        self.first_got=False
                        self.dist_estim=0

                #self.ang_pub.publish(self.angulo)
                #self.dist_pub.publish(self.distancia)
                #print(x)
                self.last_time=time.time()#self.timex
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
                if dist<val_aux and err_ang<ang_aux: #and err_ang<7 and err_ang>-7 :
                    val_aux=dist
                    ang_aux=err_ang
                    #closest.x=n.center.x
                    #closest.y=n.center.y
                    lst2.append(n)
            if len(lst2)!=0:
                for n in (lst2):
                    dist=np.sqrt(n.center.x*n.center.x+n.center.y*n.center.y)
                    if dist<dst_aux: #and err_ang<7 and err_ang>-7 :
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
