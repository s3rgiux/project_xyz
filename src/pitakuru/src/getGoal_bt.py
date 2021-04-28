#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import sys,time
print(sys.path)
print(sys.version)
from math import sqrt, cos, sin
import rospy
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
#import msvcrt
#import keyboard

import struct
import time
import functools
import py_trees
import py_trees_ros
import py_trees.console as console
import mbf_msgs.msg as mbf_msgs


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

    def states_callback(self,states):
        if states.state!="AUTONOMOUS_NAVIGATION":
            #print("cancelling")
            #cancel_msg = GoalID()
            
            #self.cancel_pub.publish(cancel_msg)
            #sleep(0.02)
            #self.cancel_pub.publish(cancel_msg)
            if self.is_navigating:
                cancel_msg = GoalID()
                print("cancelling")
                #self.cancel_goal(self.pose_amcl)
                self.cancel_pub.publish(cancel_msg)
                self.client.cancel_all_goals()
                self.cancel_pub.publish(cancel_msg)
                sleep(0.02)
                self.cancel_pub.publish(cancel_msg)
                self.client.cancel_all_goals()
                self.cancel_pub.publish(cancel_msg)
                sleep(0.02)
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
            self.is_navigating=True
            self.send_goal_to_server(self.point1)
        if states.state=="AUTONOMOUS_NAVIGATION" and states.state_navigation=="goto_wp_2":
            print("going_to_point2")
            self.is_navigating=True
            self.send_goal_to_server(self.point2)
        
    
    def pubodo(self):
        try:
            a=1
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
