#!/usr/bin/env python
# coding: utf-8
import yaml
import numpy as np
import cv2
from cv2 import aruco

import rospy
import message_filters
from tf.transformations import quaternion_matrix
from sensor_msgs.msg import Image, CameraInfo
from fiducial_msgs.msg import FiducialArray, FiducialTransformArray
from cv_bridge import CvBridge


class ArucoImage: 
    

    def __init__(self):
        rospy.init_node('ArucoImage', log_level=rospy.INFO)
        rospy.on_shutdown(self.on_shutdown)
        self.bridge = CvBridge()
        image_sub = message_filters.Subscriber('image_raw', Image)
        info_sub = message_filters.Subscriber('camera_info', CameraInfo)
        position_sub = message_filters.Subscriber('fiducial_vertices', FiducialArray)
        pose_sub = message_filters.Subscriber('fiducial_transforms', FiducialTransformArray)
        ts = message_filters.TimeSynchronizer([image_sub, info_sub, position_sub, pose_sub], 10)
        ts.registerCallback(self.callback)

        self.pub = rospy.Publisher('aruco/image', Image, queue_size=1)

    def callback(self, image_msg, info_msg, position_msg, pose_msg):
        img = self.bridge.imgmsg_to_cv2(image_msg, 'bgr8')
        mtx = np.array(info_msg.K).reshape(3, 3)
        dist = np.array(info_msg.D)
        for fiducial, transform in zip(position_msg.fiducials, pose_msg.transforms):
            fiducial_id = fiducial.fiducial_id
            direction = fiducial.direction
            corners = np.array([
                [fiducial.x0, fiducial.y0],
                [fiducial.x1, fiducial.y1],
                [fiducial.x2, fiducial.y2],
                [fiducial.x3, fiducial.y3],
            ])
            trans = transform.transform.translation
            rot = transform.transform.rotation
            tvec = np.array([trans.x, trans.y, trans.z])
            rvec = np.array(quaternion_matrix([rot.w, rot.x, rot.y, rot.z]))[:3, :3]
            aruco.drawAxis(img, mtx, dist, rvec, tvec,10)#0.25/2)
        #cv2.imshow('frame', img)
        aruco_msg = self.bridge.cv2_to_imgmsg(img, encoding="bgr8")
        self.pub.publish(aruco_msg)
    
    def on_shutdown(self):
        return
        cv2.destroyAllWindows()


if __name__ == '__main__':
    node = ArucoImage()
    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        R.sleep()
