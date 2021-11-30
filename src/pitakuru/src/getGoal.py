#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import sys
print(sys.path)
print(sys.version)
import rospy
import os
import numpy as np
from time import sleep
from std_msgs.msg import *
from geometry_msgs.msg import PoseWithCovarianceStamped
from actionlib_msgs.msg import GoalID
from pitakuru.msg import States
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
SLEEP_TIME = 0.001 

class Goals:
    def __init__(self):

        self.pose_amcl = PoseWithCovarianceStamped()
        self.point1 = PoseWithCovarianceStamped()
        self.point2 = PoseWithCovarianceStamped()
        self.is_navigating = False
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.pose_callback, queue_size = 1)
        rospy.Subscriber('/pitakuru_states', States, self.states_callback, queue_size = 1)
        self.cancel_pub = rospy.Publisher("/move_base_flex/move_base/cancel", GoalID, queue_size = 1)
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

    def check_dist(self,pos_rob,goal):
        e_x = np.abs(goal.pose.pose.position.x - pos_rob.pose.pose.position.x)
        e_y = np.abs(goal.pose.pose.position.y - pos_rob.pose.pose.position.y)
        dist = np.sqrt((e_x*e_x) + (e_y*e_y))
        print("dist calculada")
        print(dist)
        if(dist > 2):
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
        

    def states_callback(self,states):
        if states.state != "AUTONOMOUS_NAVIGATION":
            if self.is_navigating:
                cancel_msg = GoalID()
                print("cancelling")
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

        if  states.state_navigation == "save_wp_1":
            self.point1 = self.pose_amcl
            print("saved1")
            print(self.point1)
            sleep(0.2)
        if states.state_navigation == "save_wp_2":
            self.point2 = self.pose_amcl
            print("saved2")
            print(self.point2)
            sleep(0.2)
        if states.state == "AUTONOMOUS_NAVIGATION" and states.state_navigation == "goto_wp_1":
            print("going_to_point1")
            os.system('rosservice call /move_base_flex/clear_costmaps {}')
            enough_distance = self.check_dist(self.pose_amcl,self.point1)
            if(enough_distance):
                print("accepted_dist")
                self.is_navigating=True
                self.send_goal_to_server(self.point1)
        if states.state == "AUTONOMOUS_NAVIGATION" and states.state_navigation == "goto_wp_2":
            print("going_to_point2")
            os.system('rosservice call /move_base_flex/clear_costmaps {}')
            enough_distance=self.check_dist(self.pose_amcl,self.point2)
            if(enough_distance):
                print("accepted_dist")
                self.is_navigating=True
                self.send_goal_to_server(self.point2)
            
        if states.state == "AUTONOMOUS_NAVIGATION" and states.state_navigation == "going_to_wp_1":
            os.system('rosservice call /move_base_flex/clear_costmaps {}')
        if states.state == "AUTONOMOUS_NAVIGATION" and states.state_navigation == "going_to_wp_2":
            os.system('rosservice call /move_base_flex/clear_costmaps {}')




def get_goal_main():
    rospy.init_node('get_goal', anonymous = True)
    get_g = Goals()
    while not rospy.is_shutdown():
        sleep(SLEEP_TIME)

if __name__=='__main__':
    try:
        get_goal_main()
    except rospy.ROSInterruptException:
        print("finish")