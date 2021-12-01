#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import rospy
from time import sleep
from std_msgs.msg import *
from segement_obstacle_danger.msg import Obstacles, States
import time
from scipy.interpolate import interp1d
from pyimagesearch.centroidtracker_sergio import CentroidTracker
import sys,time
from math import sqrt, cos, sin
import rospy
from geometry_msgs.msg import Vector3
import numpy as np

SLEEP_TIME = 0.001


class SegmentExtractor:
    def __init__(self):
        print("Segements_obtacles")
        self.danger_alert_publisher = rospy.Publisher("Danger",String, queue_size=1)
        self.obs_sub = rospy.Subscriber('/raw_obstacles', Obstacles, self.obstacles_callback, queue_size=1)
        self.front_detection = 1.0 #rospy.get_param("/obj_track/front_detection")
        self.side_detection = 0.35 #rospy.get_param("/obj_track/side_detection")
        self.last_time_received_osbtacle_msg = time.time()
        self.ct = CentroidTracker()
        self.prev_list= []

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

        return detect_cross.is_cross_linear(P0, P1_1, q0, q1) or \
               detect_cross.is_cross_linear(P0, P1_2, q0, q1) or \
               detect_cross.is_cross_circle(P0, P1_1, q0, q1)
        
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
    
    def check_obstacle(self, data):
        lst = []
        inradious = []
        distance_limit_meters = 1 
        for x in data.circles:
            dist_from_center_to_obstacle = np.sqrt( x.center.x * x.center.x + x.center.y * x.center.y)
            if dist_from_center_to_obstacle < distance_limit_meters: #1 meter
                lst.append(x)
                new = np.array([x.center.x , x.center.y])
                inradious.append(new.astype("float")) # add element inside area 
                self.last_time = time.time()#self.timex
        val_aux=0.5
        ang_aux=30
        lst2 = []
        lst3 = []
        listid = []
        dst_aux=150000
        if len(lst)!=0:
            objects = self.ct.update(inradious)            
            for(objectID , centroid) in objects.items():
                #check if already seen
                for i in range(len(self.prev_list)):
                    if(objectID == self.prev_list[i][0]):
                        prev_cx = self.prev_list[i][1]
                        prev_cy = self.prev_list[i][2]

                center_x = centroid[0] 
                center_y = centroid[1]
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
                
            
            lst2.sort(key=self.takeSecond)
            self.prev_list=listid[:] #save id of the prevoiusly seen objects
            obj_close=lst2[0]
              
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
            self.ang_pub.publish(closest) 
           

            
            

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

























class ObstacleTrack:
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
        self.prev_list= []
    
    def publish_in_case_no_objects(self):
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

    def yolo_callback(self,data):
        self.yolo_status=data.x
        self.yolo_dist=data.y
        self.yolo_ang=data.z

    def takeSecond(self,elem):
        return elem[1]

    def obstacles_callback(self, data):
        lst = []
        inradious = []
        for x in data.circles:
            if x.center.x>-0.5 and x.center.x<self.front_detection and x.center.y<self.side_detection and x.center.y>-self.side_detection:              
                ang = 90-np.arctan2(x.center.x, x.center.y) * 180 / np.pi
                dist =np.sqrt(x.center.x*x.center.x+x.center.y*x.center.y)
                self.angulo.data=ang
                self.distancia.data=dist*100
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
        dst_aux=150000
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
        

def main_track_obstacles():
    rospy.init_node('obstacle_tracking', anonymous = True)
    track_obstacles_obj = ObstacleTrack()

    while not rospy.is_shutdown():
        track_obstacles_obj.publish_in_case_no_objects()
        sleep(SLEEP_TIME)

if __name__=='__main__':
    main_track_obstacles()
