#!/usr/bin/env python
# coding: utf-8
import time

import rospy
from pitakuru.msg import DriveWheel

from proacmd import pyproacmd
from proacmd import commands as cmd
from proacmd.pyproacmd import Utils


# "Two-Wheel Drive" 
class TWDController: 
    is_shutdown = False
    last_received = None

    def __init__(self):
        rospy.init_node('TWDController', log_level=rospy.INFO)
        self.sub = rospy.Subscriber('drive_wheel_desired', DriveWheel, self.callback)
        self.pub = rospy.Publisher('drive_wheel_actual', DriveWheel, queue_size=10)
        
        self.pc_left = pyproacmd.ProaCmd(rospy.get_param('/motor/port_left'), rospy.get_param('/motor/baud'))
        self.pc_left.setup()
        self.pc_right = pyproacmd.ProaCmd(rospy.get_param('/motor/port_right'), rospy.get_param('/motor/baud'))
        self.pc_right.setup()
        self.id_L = rospy.get_param('/motor/left_id')
        self.id_R = rospy.get_param('/motor/right_id')

        self.current_left_rpm = 0.0
        self.current_right_rpm = 0.0
        self.target_left_rpm = 0.0
        self.target_right_rpm = 0.0

        self.forward_acc = rospy.get_param('/motor/forward_acc') # rpm/s
        self.backward_acc = rospy.get_param('/motor/backward_acc') # rpm/s
        self.stop_acc = rospy.get_param('/motor/stop_acc') # rpm/s

        self.pc_left.send_receive(cmd.Enable(self.id_L))
        self.pc_right.send_receive(cmd.Enable(self.id_R))

        self.last_received = rospy.get_time()

        rospy.on_shutdown(self.shutdown)

    def shutdown(self):
        rospy.logwarn("shutting down motor node")
        self.is_shutdown = True
        self.pc_left.send_receive(cmd.Disable(self.id_L))
        self.pc_right.send_receive(cmd.Disable(self.id_R))
        self.pc_left.close()
        self.pc_right.close()

    def callback(self, drive_wheel):
        # self.target_left_rpm = drive_wheel.left_rpm
        # self.target_right_rpm = drive_wheel.right_rpm
        self.current_left_rpm = drive_wheel.left_rpm
        self.current_right_rpm = drive_wheel.right_rpm

    def calc_diff_vel(self, current, target, acc, dt):
        acc_sign = 1 if target - current >= 0 else -1
        dv = min(abs(acc*dt), abs(target-current)) * acc_sign
        return current + dv

    def update_rpm(self):
        current_time = rospy.get_time()
        dt = current_time - self.last_received
        # 停止コマンドの場合
        if self.target_left_rpm == 0.0 and self.target_right_rpm == 0.0:
            acc = self.stop_acc
        # 後退コマンドの場合
        elif self.target_left_rpm < 0.0 and self.target_right_rpm < 0.0:
            acc = self.backward_acc
        # 前進/旋回の場合
        else:
            acc = self.forward_acc
        self.current_left_rpm = self.calc_diff_vel(self.current_left_rpm, self.target_left_rpm, acc, dt)
        self.current_right_rpm = self.calc_diff_vel(self.current_right_rpm, self.target_right_rpm, acc, dt)
        self.last_received = current_time


    def send_rpm(self):
        if self.is_shutdown:
            return
        self.pc_left.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(self.current_left_rpm)))
        self.pc_right.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-self.current_right_rpm)))
        left_cmd = self.pc_left.send_receive(cmd.ReadFOC(self.id_L))
        left_actual_rpm = left_cmd.resp.body[1]
        right_cmd = self.pc_right.send_receive(cmd.ReadFOC(self.id_R))
        right_actual_rpm = right_cmd.resp.body[1]
        self.pub.publish(DriveWheel(Utils.RADpStoRPM(left_actual_rpm), Utils.RADpStoRPM(left_actual_rpm)))


if __name__ == '__main__':
    twd = TWDController()
    # 制御周期
    ROS_RATE = 10
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    try:
        while not rospy.is_shutdown():
            R.sleep()
            # twd.update_rpm()
            twd.send_rpm()
    except rospy.ROSInterruptException:
        pass