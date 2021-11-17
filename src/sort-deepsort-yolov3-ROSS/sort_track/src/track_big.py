#!/usr/bin/env python

"""
ROS node to track objects using SORT TRACKER and YOLOv3 detector (darknet_ros)
Takes detected bounding boxes from darknet_ros and uses them to calculated tracked bounding boxes
Tracked objects and their ID are published to the sort_track node
No delay here
""" 

import rospy
import numpy as np
from darknet_ros_msgs.msg import BoundingBoxes
from sort import sort 
from cv_bridge import CvBridge
import cv2
from sort_track.msg import IntList
from sort_track.msg import people_box,peoples
import time
from time import sleep

class trackclass:
	def __init__(self):
		#Initialize ROS node
		#(camera_topic, detection_topic, tracker_topic, cost_threshold, max_age, min_hits) = self.get_parameters()
		self.camera_topic = rospy.get_param("~camera_topic")
		self.detection_topic = rospy.get_param("~detection_topic")
		self.tracker_topic = rospy.get_param('~tracker_topic')
		self.cost_threhold = rospy.get_param('~cost_threhold')
		self.min_hits = rospy.get_param('~min_hits')
		self.max_age = rospy.get_param('~max_age')
		#Subscribe to darknet_ros to get BoundingBoxes from YOLOv3
		sub_detection = rospy.Subscriber(self.detection_topic, BoundingBoxes , self.callback_det)
		#Publish results of object tracking
		self.pub_trackers = rospy.Publisher('sorted_tracked',IntList, queue_size=2) #self.tracker_topic, IntList, queue_size=2)
		self.pub_peoples = rospy.Publisher('peoples_sorted_tracked',peoples, queue_size=2) #self.tracker_topic, IntList, queue_size=2)
		self.tracker = sort.Sort(max_age=self.max_age, min_hits=self.min_hits) #create instance of the SORT tracker
		self.track = []
		self.msg = IntList()
		self.last_time = 0
		self.people_box = people_box()
		self.people_msg = peoples()
		
	def callback_det(self,data):
		detec = []
		ntrackers = []
		for box in data.bounding_boxes:
			if box.Class =="person":
				detec.append(np.array([box.xmin, box.ymin, box.xmax, box.ymax, round(box.probability,2)]))
		if(len(detec)>0):
			self.detections = np.array(detec)
			#Call the tracker
			people_msg_no1=peoples()
			ntrackers = self.tracker.update(self.detections)
			if len(ntrackers)>0:
				for n in ntrackers:
					area=((n[2]-n[0])*(n[3]-n[1]))
					neew=[]
					people_boxs1=people_box()
					
					for j in range(len(n)):
						neew.append(n[j])
					neew.append(area)
					people_boxs1.xmin=int(neew[0])
					people_boxs1.ymin=int(neew[1])
					people_boxs1.xmax=int(neew[2])
					people_boxs1.ymax=int(neew[3])
					people_boxs1.id  =int(neew[4])
					people_boxs1.area=int(area/1000)
					people_msg_no1.people.append(people_boxs1)
					trackerrss = np.array(neew, dtype='int')
					self.msg.data = trackerrss
					self.pub_trackers.publish(self.msg)
				self.pub_peoples.publish(people_msg_no1)
			self.last_time=time.time()

	
	def publish_dat(self):
		if(time.time()-self.last_time>0.4):
			self.last_time=time.time()
			people_msg_no=peoples()
			people_boxs=people_box()
			people_boxs.xmin=-1
			people_boxs.ymin=-1
			people_boxs.xmax=-1
			people_boxs.ymax=-1
			people_boxs.id=-1
			people_boxs.area=-1
			people_msg_no.people.append(people_boxs)
			self.msg.data = np.array([-1,-1,-1,-1,-1,-1], dtype='int')
			self.pub_peoples.publish(people_msg_no)
			self.pub_trackers.publish(self.msg)


def main():
	rospy.init_node('tracker_node', anonymous = True)
	track_obj = trackclass()
	while not rospy.is_shutdown():
		track_obj.publish_dat()		
		sleep(0.07)

if __name__ == '__main__':
	try :
		main()
	except rospy.ROSInterruptException:
		pass