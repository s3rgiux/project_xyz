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
from sensor_msgs.msg import Image
from sort_track.msg import IntList

import sys,time
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
		#image_sub = rospy.Subscriber(self.camera_topic,Image,self.callback_image)
		#Subscribe to darknet_ros to get BoundingBoxes from YOLOv3
		sub_detection = rospy.Subscriber(self.detection_topic, BoundingBoxes , self.callback_det)
		#Publish results of object tracking
		self.pub_trackers = rospy.Publisher('sorted_tracked',IntList, queue_size=2) #self.tracker_topic, IntList, queue_size=2)
		self.tracker = sort.Sort(max_age=self.max_age, min_hits=self.min_hits) #create instance of the SORT tracker
		self.track = []
		self.msg = IntList()
		self.last_time=0
		

	def callback_det(self,data):
		detec = []
		ntrackers = []
		peop=[]
		new= []
		for box in data.bounding_boxes:
			if box.Class =="person":
				#peop.append(box)
				detec.append(np.array([box.xmin, box.ymin, box.xmax, box.ymax, round(box.probability,2)]))
		if(len(detec)>0):
			self.detections = np.array(detec)
			#Call the tracker
			ntrackers = self.tracker.update(self.detections)
            
			if len(ntrackers)>0:
				for n in ntrackers:
					area=((n[2]-n[0])*(n[3]-n[1]))
					for j in range(len(n)):
						new.append(n[j])
					new.append(area)
					#trackerrss = np.array(n, dtype='int')
					trackerrss = np.array(new, dtype='int')
					self.msg.data = trackerrss
					self.pub_trackers.publish(self.msg)
			self.last_time=time.time()
		#self.trackers = np.array(ntrackers, dtype='int')
		#self.track = self.trackers
		#self.msg.data = self.track
		#t1=self.trackers.shape
		#print(t1[0])
		#print(t1[1])
		#print(a.shape)
		#print(self.track)
		#print(self.trackers.shape)
		#self.pub_trackers.publish(self.msg)
	
	def publish_dat(self):
		if(time.time()-self.last_time>0.5):
			#trackerrss = 
			self.msg.data = np.array([-1,-1,-1,-1,-1,-1], dtype='int')
			self.pub_trackers.publish(self.msg)

			
	def callback_image(self,data):
		#Display Image
		bridge = CvBridge()
		cv_rgb = bridge.imgmsg_to_cv2(data, "bgr8")
		#TO DO: FIND BETTER AND MORE ACCURATE WAY TO SHOW BOUNDING BOXES!!
		#Detection bounding box
		cv2.rectangle(cv_rgb, (int(self.detections[0][0]), int(self.detections[0][1])), (int(self.detections[0][2]), int(self.detections[0][3])), (100, 255, 50), 1)
		cv2.putText(cv_rgb , "person", (int(self.detections[0][0]), int(self.detections[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (100, 255, 50), lineType=cv2.LINE_AA)	
		#Tracker bounding box
		#cv2.rectangle(cv_rgb, (track[0][0], track[0][1]), (track[0][2], track[0][3]), (255, 255, 255), 1)
		#cv2.putText(cv_rgb , str(track[0][4]), (track[0][2], track[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA)
		cv2.imshow("YOLO+SORT", cv_rgb)
		cv2.waitKey(3)

def main():
	rospy.init_node('tracker_node', anonymous = True)
	track_obj = trackclass()
	#rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		track_obj.publish_dat()		
		sleep(0.07)
		#rospy.spin()


if __name__ == '__main__':
	try :
		main()
	except rospy.ROSInterruptException:
		pass
