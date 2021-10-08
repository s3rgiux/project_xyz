#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import sys,time
print(sys.path)
print(sys.version)
from math import sqrt, cos, sin
import rospy
import os
#import tf2_ros
import tf,tf2_ros
import numpy as np
from time import sleep
from geometry_msgs.msg import Twist, Pose, TransformStamped,Quaternion
from sensor_msgs.msg import Imu, JointState
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import *
from geometry_msgs.msg import Point, Vector3, PoseWithCovarianceStamped
from actionlib_msgs.msg import GoalID
import commands as cmd
import std_srvs
#import msvcrt
#import keyboard
import struct
import time
from pitakuru.msg import States, TriggerAction
import rosparam

import atexit
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

SLEEP_TIME = 0.001 #0.015#0.05


class Goals:
    def __init__(self):
        #self.left_pub = rospy.Publisher('left_wheel', Float32, queue_size=1)
        self.x = np.array([0.0, 0.0, 0.0])
        self.current_time = time.time()
        self.last_time = time.time()
        self.pose_amcl=PoseWithCovarianceStamped()
        self.point1=PoseWithCovarianceStamped()
        self.point2=PoseWithCovarianceStamped()
        self.is_navigating=False
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        #rospy.Subscriber('/cmd_vel', Twist, self.teleop_callback, queue_size=1)
        rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.pose_callback, queue_size=1)
        rospy.Subscriber('/pitakuru_states', States, self.states_callback, queue_size=1)
        self.cancel_pub = rospy.Publisher("/move_base_flex/move_base/cancel", GoalID, queue_size=1)
        print("started node")
        self.list_wp=[]
        self.goto_end=False
        self.goto_start=False
        self.next_wp=PoseWithCovarianceStamped()
        self.actual_index=0

    def pose_callback(self, data):
        self.pose_amcl=data

    def cancel_goal(self,goals):    
        self.client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = goals.pose.pose.position.x
        goal.target_pose.pose.position.y = goals.pose.pose.position.y
        goal.target_pose.pose.orientation.w = goals.pose.pose.orientation.w
        goal.target_pose.pose.orientation.z = goals.pose.pose.orientation.z
        self.client.send_goal(goal)

    def check_dist(self,pos_rob,goal):
        e_x=np.abs(goal.pose.pose.position.x-pos_rob.pose.pose.position.x)
        e_y=np.abs(goal.pose.pose.position.y-pos_rob.pose.pose.position.y)
        dist=np.sqrt((e_x*e_x)+(e_y*e_y))
        print("dist calculada")
        print(dist)
        if(dist>2):
            return True
        else:
            return False


    def send_goal_to_server(self,goals):    
        
        self.client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = goals.pose.pose.position.x
        goal.target_pose.pose.position.y = goals.pose.pose.position.y
        goal.target_pose.pose.orientation.w = goals.pose.pose.orientation.w
        goal.target_pose.pose.orientation.z = goals.pose.pose.orientation.z
        self.client.send_goal(goal)
        
        # wait = self.client.wait_for_result()
        # if not wait:
        #     rospy.logerr("Action server not available!")
        #     rospy.signal_shutdown("Action server not available!")
        # else:
        #     self.is_navigating=False
        #     print("achieved or result")
        #     return self.client.get_result()
    def goto_start(self):
        if len(self.list_wp)>0:
            if len(self.list_wp)==2:
                self.next_wp=self.list_wp(len(self.list_wp)-1)
                self.actual_index=len(self.list_wp)-1
            elif len(self.list_wp)>2:
                self.next_wp=self.list_wp(len(self.list_wp)-1)
                self.actual_index=len(self.list_wp)-1
                a=self.check_dist(self.pose_amcl,self.next_wp)
                if(a):
                    print("accepted_dist")
                    self.is_navigating=True
                    self.send_goal_to_server(self.next_wp)

    def goto_end(self):
        if len(self.list_wp)>0:
            if len(self.list_wp)==2:
                self.next_wp=self.list_wp(len(self.list_wp))
                self.actual_index=len(self.list_wp)
            elif len(self.list_wp)>2:
                self.next_wp=self.list_wp(2)
                a=self.check_dist(self.pose_amcl,self.next_wp)
                self.actual_index=2
                if(a):
                    print("accepted_dist")
                    self.is_navigating=True
                    self.send_goal_to_server(self.next_wp)

    def states_callback(self,states):
        if states.state!="AUTONOMOUS_NAVIGATION":

            if self.is_navigating:
                cancel_msg = GoalID()
                print("cancelling")
                #self.cancel_goal(self.pose_amcl)
                for i in range(50):
                    self.cancel_pub.publish(cancel_msg)
                    self.client.cancel_all_goals()
                    self.cancel_pub.publish(cancel_msg)
                    sleep(0.01)
                    self.cancel_pub.publish(cancel_msg)
                    self.client.cancel_all_goals()
                    self.cancel_pub.publish(cancel_msg)
                    sleep(0.01)
                    self.cancel_pub.publish(cancel_msg)
                    self.client.cancel_all_goals()
                    self.cancel_pub.publish(cancel_msg)
                    
                self.is_navigating=False
                # cancel_msg = GoalID()
                # self.cancel_pub.publish(cancel_msg)
                # sleep(0.02)
                # self.cancel_pub.publish(cancel_msg)
                #sleep(0.02)
                #self.cancel_pub.publish(cancel_msg)
                #sleep(0.02)
                #self.cancel_pub.publish(cancel_msg)
                #self.client.cancel_goal()
                #self.client.cancel_goal()
                #self.is_navigating=False
            #else:
            #    print("changing mode")
            #    self.is_navigating=False
        
        if  states.state_navigation=="save_wp":#states.state=="AUTONOMUS_NAVIGATION" and states.state_navigation=="save_wp_1":
            #self.point1=self.pose_amcl
            self.list_wp.append(self.pose_amcl)
            # print("saved")
            # print(self.pose_amcl)
            # print("list of saved")
            # print(self.list_wp)
            # print("elem zero")
            # print(self.list_wp[0])
            sleep(0.5)
        if  states.state_navigation=="clear_wp":#states.state=="AUTONOMUS_NAVIGATION" and states.state_navigation=="save_wp_1":
            #self.point1=self.pose_amcl
            self.list_wp.clear()
            print("cleared")
            #print(self.point1)
            sleep(0.2)
        if  states.state_navigation=="save_wp_1":#states.state=="AUTONOMUS_NAVIGATION" and states.state_navigation=="save_wp_1":
            self.point1=self.pose_amcl
            print("saved1")
            print(self.point1)
            sleep(0.2)
        if states.state_navigation=="save_wp_2":#states.state=="AUTONOMUS_NAVIGATION" and states.state_navigation=="save_wp_2":
            self.point2=self.pose_amcl
            print("saved2")
            print(self.point2)
            sleep(0.2)
        if states.state=="AUTONOMOUS_NAVIGATION" and states.state_navigation=="goto_wp_1":
            print("going_to_point1")
            #rospy.ServiceProxy("/move_base_flex/clear_costmaps",std_srvs.Empty)
            os.system('rosservice call /move_base_flex/clear_costmaps {}')
            self.goto_start()
            self.to_start=True
            self.to_end=False
            # a=self.check_dist(self.pose_amcl,self.point1)
            # if(a):
            #     print("accepted_dist")
            #     self.is_navigating=True
            #     self.send_goal_to_server(self.point1)
        if states.state=="AUTONOMOUS_NAVIGATION" and states.state_navigation=="goto_wp_2":
            print("going_to_point2")
            
            #rospy.ServiceProxy("/move_base_flex/clear_costmaps",std_srvs.Empty)
            os.system('rosservice call /move_base_flex/clear_costmaps {}')
            self.goto_end()
            self.to_end=True
            self.to_start=False
            # a=self.check_dist(self.pose_amcl,self.point2)
            # if(a):
            #     print("accepted_dist")
            #     self.is_navigating=True
            #     self.send_goal_to_server(self.point2)
            
        if states.state=="AUTONOMOUS_NAVIGATION" and states.state_navigation=="going_to_wp_1":
            os.system('rosservice call /move_base_flex/clear_costmaps {}')
        if states.state=="AUTONOMOUS_NAVIGATION" and states.state_navigation=="going_to_wp_2":
            os.system('rosservice call /move_base_flex/clear_costmaps {}')

        
    def check_dist_goal(self):
        e_x=np.abs(self.pose_amcl.pose.pose.position.x-self.next_wp.pose.pose.position.x)
        e_y=np.abs(self.pose_amcl.pose.pose.position.y-self.next_wp.pose.pose.position.y)
        dist=np.sqrt((e_x*e_x)+(e_y*e_y))
        #print("dist calculada")
        #print(dist)
        if(self.goto_end):
            if(dist<0.5 and self.actual_index<len(self.list_wp)):
                self.actual_index=self.actual_index+1
                self.next_wp=self.list_wp(self.actual_index)
                self.send_goal_to_server(self.next_wp)
            # else:
            #     return False
        if(self.goto_start):
            if(dist<0.5 and self.actual_index>1):
                self.actual_index=self.actual_index-1
                self.next_wp=self.list_wp(self.actual_index)
                self.send_goal_to_server(self.next_wp)

    def pubodo(self):
        try:
            a=1
            self.check_dist_goal()
            # self.current_time = time.time()
            # dt = self.current_time-self.last_time
            # self.x = MotionModel(self.x,u,dt)
            # self.last_time = time.time()
            # self.odo.header.stamp = rospy.Time.now()
            # self.odo.pose.pose.position.x = self.x[0]
            # self.odo.pose.pose.position.y = self.x[1]
            # q = tf.transformations.quaternion_from_euler(0, 0, self.x[2])
            # self.odo.pose.pose.orientation = Quaternion(*q)
            # self.pub_odo.publish(self.odo)

           
        except:
            import traceback
            traceback.print_exc()

    

    def shutdown(self):
        #rospy.sleep(1)
        self.left_w_dev.disable_handler()
        self.right_w_dev.disable_handler()


def get_goal_main():
    rospy.init_node('get_goal', anonymous = True)
    get_g = Goals()
    while not rospy.is_shutdown():
        get_g.pubodo()
        sleep(SLEEP_TIME)
        
   

if __name__=='__main__':
    try:
        get_goal_main()
    except rospy.ROSInterruptException:
        print("finish")
        #pit_wheels.shutdown()