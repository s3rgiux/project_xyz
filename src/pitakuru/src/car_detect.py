#!/usr/bin/env python



import rospy
import numpy as np
from darknet_ros_msgs.msg import BoundingBoxes
from std_msgs.msg import String
import time
from time import sleep

MIN_AREA_DETECTION = 40

class carDetectClass:
	def __init__(self):
		#Initialize ROS node
		#Subscribe to darknet_ros to get BoundingBoxes from YOLOv3
		sub_detection = rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes , self.callback_det)
		#Publish results of object tracking
		self.car_detectors = rospy.Publisher('cars_detected',String , queue_size=1)
		

	def calc_area(self, box):
		return (box.xmax - box.xmin) *  (box.ymax - box.ymin)

	def callback_det(self,data):
		detected_car = String()
		detected_car.data = "false"
		for box in data.bounding_boxes:
			if box.Class == "car":
				#print("detected_car")
				area = self.calc_area(box)
				if area > MIN_AREA_DETECTION:
					detected_car.data = "detected_car"
		self.car_detectors.publish(detected_car)

def main():
	rospy.init_node('tracker_node', anonymous = True)
	car_detector = carDetectClass()
	while not rospy.is_shutdown():		
		sleep(0.07)

if __name__ == '__main__':
	try :
		main()
	except rospy.ROSInterruptException:
		pass