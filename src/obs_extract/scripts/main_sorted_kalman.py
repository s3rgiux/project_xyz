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
from pyimagesearch.centroidtracker_sergio import CentroidTracker
from sort_track.msg import IntList
from obs_extract.msg import Obstacles
import argparse
import imutils

import struct
import time
import rosparam
import cv2 as cv
import numpy as np
import sys


#params = rosparam.get_param("/km_dolly_wheels")
#if params['connect_mode']=='ble':
#    from pykeigan import blecontroller
#    SLEEP_TIME = 0.01
#else:
#    from pykeigan import usbcontroller
#    SLEEP_TIME = 0.1
import atexit


SLEEP_TIME = 0.001
#200mm diameter0





# Instantiate OCV kalman filter
class KalmanFilter:
    kf = cv.KalmanFilter(4, 2)
    kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
    kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)

    def Estimate(self, coordX, coordY):
        ''' This function estimates the position of the object'''
        measured = np.array([[np.float32(coordX)], [np.float32(coordY)]])
        self.kf.correct(measured)
        predicted = self.kf.predict()
        return predicted

class PitWheels:
    def __init__(self):
        print("Obstacle_extarctor")
        #rospy.loginfo("Connected to Right Wheel")
        #self.brinco=False
        self.obst_pub = rospy.Publisher('obstacle_closest', Float32, queue_size=1)
        self.peop_id_pub = rospy.Publisher('/peop_obst_id', IntList, queue_size=1)
        self.estim_pub = rospy.Publisher('estimated_people', Vector3, queue_size=1)
        #self.ang_pub = rospy.Publisher("peopAng2",Float32, queue_size=1)
        self.ang_pub = rospy.Publisher("peopAng2",Vector3, queue_size=2)
        self.speed_pub = rospy.Publisher("peopAngSpeed",Vector3, queue_size=2)
        rospy.Subscriber('/ang_peop_detect_img', Float32, self.ang_cam_callback, queue_size=1)
        self.dist_pub = rospy.Publisher("peopDist2",Float32, queue_size=1)
        #rospy.Subscriber('/cmd_vel', Twist, self.teleop_callback, queue_size=1)
        rospy.Subscriber('/obstacles', Obstacles, self.obstacles_callback, queue_size=1)
        rospy.Subscriber('/tracked', Vector3, self.tracked_callback, queue_size=2)
        rospy.Subscriber('/peop_ang_yolo', Vector3, self.yolo_callback, queue_size=1)
        #rospy.Subscriber('/euler2', Float64, self.angle_callback, queue_size=1)
         # Create Kalman Filter Object
        self.kfObj = KalmanFilter()
        self.predictedCoords = np.zeros((2, 1), np.float32)
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
        self.radius_follow=rospy.get_param("/obj_track/radius_follow")
        self.yolo_status=0
        self.yolo_dist =0
        self.yolo_ang=0
        self.ct = CentroidTracker()
        self.last_time_tracked=0
        self.msg_objects_in_radius = IntList()
        self.prev_cx=0
        self.prev_cy=0
        self.follow_cx=0
        self.follow_cy=0
        self.first_got=False
        self.find_again=False
        self.prev_list= []
    
    def pubobs(self):
        if(time.time()-self.last_time>0.5):
        #if(self.track==0):
            self.angulo.data=-500
            self.ang_dist.x=-0.01
            self.ang_dist.y=-0.01
            self.ang_dist.z=-0.01
            self.distancia.data=0
            self.ang_pub.publish(self.ang_dist)
            self.first_got=False
            #self.dist_pub.publish(self.distancia)
    
    def ang_cam_callback(self,data):
        self.ang_cam=data.data

    def tracked_callback(self,data):
        self.tracked_x=data.x
        self.tracked_y=data.y
        self.tracked_ang=data.z
        if self.tracked_x==-50:
            self.first_got=False
        if self.tracked_x==-70:
            self.find_again=True

    def yolo_callback(self,data):
        self.yolo_status=data.x
        self.yolo_dist=data.y
        self.yolo_ang=data.z

    def takeSecond(self,elem):
        return elem[1]

    


    def obstacles_callback(self, data):
        lst = []
        inradious = []
        again_lst=[]
        for x in data.circles:
            if x.center.x>-0.5 and x.center.x<self.front_detection and x.center.y<self.side_detection and x.center.y>-self.side_detection:              
                ang = 90-np.arctan2(x.center.x, x.center.y) * 180 / np.pi
                dist =np.sqrt(x.center.x*x.center.x+x.center.y*x.center.y)
                self.angulo.data=ang
                self.distancia.data=dist*100
                if self.find_again:
                    if np.abs(ang-self.yolo_ang)<8:
                        again_lst.append(x)
                else:    
                    if self.first_got and x.center.x>0.2 and x.center.x<-0.2 and x.center.y>0.2 and x.center.y<-0.2 and  x.center.x<=(self.follow_cx+self.radius_follow) and x.center.x>=(self.follow_cx-self.radius_follow) and x.center.y <=(self.follow_cy+self.radius_follow) and x.center.y >=(self.follow_cy-self.radius_follow):#then we have tracked object
                        lst.append(x)
                        new=np.array([x.center.x,x.center.y])
                        inradious.append(new.astype("float"))
                    elif self.first_got==False and self.tracked_x != -50 and self.tracked_y != -50 and x.center.x<=(self.tracked_x+self.radius_follow) and x.center.x>=(self.tracked_x-self.radius_follow) and x.center.y <=(self.tracked_y+self.radius_follow) and x.center.y >=(self.tracked_y-self.radius_follow):#then we have tracked object
                    #if self.tracked_x != -50 and self.tracked_y != -50 and x.center.x<=(self.tracked_x+self.radius_follow) and x.center.x>=(self.tracked_x-self.radius_follow) and x.center.y <=(self.tracked_y+self.radius_follow) and x.center.y >=(self.tracked_y-self.radius_follow):#then we have tracked object
                        first_got=True
                        self.follow_cx=x.center.x
                        self.follow_cy=x.center.y
                        lst.append(x)
                        new=np.array([x.center.x,x.center.y])
                        inradious.append(new.astype("float"))

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
        estim= Vector3() 
        aux=[10000,10000]
        val_aux=0.5
        ang_aux=30
        lst2 = []
        lst3 = []
        listid = []
        lst4 = []
        dst_aux=150000
        if len(again_lst)!=0:
            for n in (again_lst):
                #e_x=np.abs(self.tracked_x-n.center.x)
                #e_y=np.abs(self.tracked_y-n.center.y)
                dist=np.sqrt(n.center.x*n.center.x+n.center.y*n.center.y)
                ang_obj= 90-np.arctan2(n.center.x, n.center.y) * 180 / np.pi
                #err_ang= np.abs(self.tracked_ang-ang_obj)
                #if(dist<self.radius_follow):
                lst4.append((n,dist))#contains (error distancia and err ang)
            #sort list
            lst4.sort(key=self.takeSecond)
            obj_close=lst4[0]
            closest.x=obj_close[0].center.x
            closest.y=obj_close[0].center.y
            closest.z=len(lst)
            deltat=time.time()-self.last_time_tracked
            speed_x=(closest.x-self.prev_cx)/deltat
            speed_y=(closest.y-self.prev_cy)/deltat
            speed_p=Vector3()
            speed_p.x=speed_x
            speed_p.y=speed_y
            speed_p.z=obj_close[1]
            self.speed_pub.publish(speed_p)
            self.prev_cx=closest.x
            self.prev_cy=closest.y
            self.last_time_tracked=time.time()
            self.ang_pub.publish(closest)

        if len(lst)!=0:
            #now1=time.time()
            """ objects = self.ct.update(inradious)
            #end_now1=time.time()
            #print('objects')
            #rospy.logerr("a speed: {}".format(angular_speed))
            #rospy.logerr("objects")
            #now2=time.time()
            velx=0
            vely=0
            prev_cx=0
            prev_cy=0
            
            for(objectID,centroid) in objects.items():
                #check if already seen
                for i in range(len(self.prev_list)):
                    if(objectID==self.prev_list[i][0]):
                        prev_cx=self.prev_list[i][1]
                        prev_cy=self.prev_list[i][2]
                        velx=(centroid[0]-self.prev_list[i][1])
                        vely=(centroid[1]-self.prev_list[i][2])
                    else:
                        velx=0#(centroid[0]-self.prev_list[i][0])
                        vely=0#(centroid[1]-self.prev_list[i][1])

                center_x= centroid[0]
                center_y= centroid[1]
                e_x=np.abs(self.tracked_x-center_x)
                e_y=np.abs(self.tracked_y-center_y)
                dist=np.sqrt(e_x*e_x+e_y*e_y)
                ang_obj= 90-np.arctan2(center_x, center_y) * 180 / np.pi
                err_ang= np.abs(self.tracked_ang-ang_obj)
                #if(dist<sel.radius_follow):
                listid.append([objectID,centroid[0],centroid[1]])
                lst2.append(([objectID,centroid],dist))#contains (error distancia and err ang)
                self.msg_objects_in_radius.data=np.array([objectID,center_x*10,center_y*10,velx*100,vely*100,dist*100,center_x*100,prev_cx*100,center_y*100,prev_cy*100,len(self.prev_list)],dtype="int")
                self.peop_id_pub.publish(self.msg_objects_in_radius) 
                
            #end_now2=time.time()
            #rospy.logerr('time ms{},{}'.format(now1-end_now1,end_now2-now2))
            lst2.sort(key=self.takeSecond)
            self.prev_list=listid[:]
            obj_close=lst2[0]
            #for f in lst2:
            #    rospy.logerr(f)    
            closest.x=obj_close[0][1][0]
            closest.y=obj_close[0][1][1]
            closest.z=obj_close[0][0]#len(lst)

            self.follow_cx=closest.x
            self.follow_cx=closest.y

            deltat=time.time()-self.last_time_tracked
            speed_x=(closest.x-self.prev_cx)/deltat
            speed_y=(closest.y-self.prev_cy)/deltat

            speed_p=Vector3()
            speed_p.x=speed_x
            speed_p.y=speed_y
            speed_p.z=obj_close[1]#distancia
            self.speed_pub.publish(speed_p)
            self.prev_cx=closest.x
            self.prev_cy=closest.y

            self.last_time_tracked=time.time()
            self.ang_pub.publish(closest) """
           

            for n in (lst):
                e_x=np.abs(self.tracked_x-n.center.x)
                e_y=np.abs(self.tracked_y-n.center.y)
                dist=np.sqrt(e_x*e_x+e_y*e_y)
                ang_obj= 90-np.arctan2(n.center.x, n.center.y) * 180 / np.pi
                err_ang= np.abs(self.tracked_ang-ang_obj)
                if(dist<self.radius_follow):
                    lst2.append((n,dist))#contains (error distancia and err ang)
            #sort list
            lst2.sort(key=self.takeSecond)
            obj_close=lst2[0]
            #for f in lst2:
            #    rospy.logerr(f)
            #self.predictedCoords = self.kfObj.Estimate(obj_close[0].center.x, obj_close[0].center.y) 
            #estim.x=self.predictedCoords[0]
            #estim.y=self.predictedCoords[1]
            #self.estim_pub.publish(estim)

            closest.x=obj_close[0].center.x
            closest.y=obj_close[0].center.y
            closest.z=len(lst)
            deltat=time.time()-self.last_time_tracked
            speed_x=(closest.x-self.prev_cx)/deltat
            speed_y=(closest.y-self.prev_cy)/deltat
            speed_p=Vector3()
            speed_p.x=speed_x
            speed_p.y=speed_y
            speed_p.z=obj_close[1]
            self.speed_pub.publish(speed_p)
            self.prev_cx=closest.x
            self.prev_cy=closest.y
            self.last_time_tracked=time.time()
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
