#!/usr/bin/env python
# coding: utf-8
import rospy
import rosparam
import os
from rospy.core import rospydebug
from std_msgs.msg import Int32, Float32
from mongodb_store.message_store import MessageStoreProxy

class ChargeCountNode:
    def __init__(self):
        rospy.init_node('charge_count')
        self.volt_store = MessageStoreProxy(database="pitakuru",collection="volt")
        self.charge_store = MessageStoreProxy(database="pitakuru", collection="charge_count")
        self.init_charge_data()
        self.pub = rospy.Publisher('charge_count', Int32, queue_size=1)
        self.sub = rospy.Subscriber('volts', Float32, self.callback)
    
    def init_charge_data(self):
        try:
            charge_count, meta = self.charge_store.query_named("charge_count", Int32._type)
            if charge_count is None:
                count_id = self.charge_store.insert_named("charge_count", Int32(0))
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
    
    def callback(self, data):
        try:
            prev_volt = self.volt_store.query_named("prev_volt", Float32._type)
            if prev_volt[0] is None:
                #print "insert prev_volt"
                volt_id = self.volt_store.insert_named("prev_volt", data)
            elif data.data > prev_volt[0].data:
                charge_count, meta = self.charge_store.query_named("charge_count", Int32._type)
                charge_count.data += 1
                charge_id = self.charge_store.update_named("charge_count", charge_count)
                rospy.logdebug("charge: %d", charge_count.data)
            volt_id = self.volt_store.update_named("prev_volt", data, upsert=True)
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
    
    def pub_charge_count(self):
        try:
            charge_count, meta = self.charge_store.query_named("charge_count", Int32._type)
            if charge_count is None:
                return
            else:
                self.pub.publish(charge_count)
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e  

if __name__ == '__main__':
    try:
        node = ChargeCountNode()
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            rate.sleep()
            node.pub_charge_count()

    except rospy.ROSInterruptException:
        pass