#!/usr/bin/env python
# coding: utf-8
import json
from uuid import uuid4
import websocket
import yaml
from threading import Thread
import time
import sys
import math

import rospy
from rospy_message_converter import message_converter
from rospy import Header
from sensor_msgs.msg import CompressedImage


class PublisherNode(object):
    def __init__(self, websocket_ip, port=9090):
	self.i = 0
        print("Connecting to websocket: {}:{}".format(websocket_ip, port))
        self.ws = websocket.create_connection(
            'ws://' + websocket_ip + ':' + str(port))
        self._advertise_dict = {}

        rospy.init_node('bridge_publisher')
        self.sub = rospy.Subscriber('/image_raw/compressed', CompressedImage, self.image_callback, queue_size = 1)

    def image_callback(self, image):
        # publish image to rosbridge server
        self.publish('/image_raw/compressed', image)
    
    def _advertise(self, topic_name, topic_type):
        """
        Advertise a topic with it's type in 'package/Message' format.
        :param str topic_name: ROS topic name.
        :param str topic_type: ROS topic type, e.g. std_msgs/String.
        :returns str: ID to de-advertise later on.
        """
        new_uuid = str(uuid4())
        self._advertise_dict[new_uuid] = {'topic_name': topic_name,
                                          'topic_type': topic_type}
        advertise_msg = {"op": "advertise",
                         "id": new_uuid,
                         "topic": topic_name,
                         "type": topic_type
                         }
        self.ws.send(json.dumps(advertise_msg))
        return new_uuid

    def _unadvertise(self, uuid):
        unad_msg = {"op": "unadvertise",
                    "id": uuid,
                    # "topic": topic_name
                    }
        self.ws.send(json.dumps(unad_msg))

    def __del__(self):
        """Cleanup all advertisings"""
        d = self._advertise_dict
        for k in d:
            self._unadvertise(k)
    
    def _publish(self, topic_name, message):
        """
        Publish onto the already advertised topic the msg in the shape of
        a Python dict.
        :param str topic_name: ROS topic name.
        :param dict msg: Dictionary containing the definition of the message.
        """
	msg = {
            'op': 'publish',
            'topic': topic_name,
            'msg': message
        }
        json_msg = json.dumps(msg)
        self.ws.send(json_msg)

    def publish(self, topic_name, ros_message):
        """
        Publish on a topic given ROS message thru rosbridge.
        :param str topic_name: ROS topic name.
        :param * ros_message: Any ROS message instance, e.g. LaserScan()
            from sensor_msgs/LaserScan.
        """
        # First check if we already advertised the topic
        d = self._advertise_dict
        for k in d:
            if d[k]['topic_name'] == topic_name:
                # Already advertised, do nothing
                break
        else:
            # Not advertised, so we advertise
            topic_type = ros_message._type
            self._advertise(topic_name, topic_type)
        # Converting ROS message to a dictionary thru YAML
        ros_message_as_dict = message_converter.convert_ros_message_to_dictionary(ros_message)
        # Publishing
        self._publish(topic_name, ros_message_as_dict)


if __name__ == "__main__":
    node = PublisherNode('18.176.174.106')
    # 制御周期
    ROS_RATE = 100
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        R.sleep()
