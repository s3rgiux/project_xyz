#!/usr/bin/env python
# coding: utf-8
import math

import rospy
from pitakuru.msg import TriggerAction
from obstacle_detector.msg import Obstacles


class FindObstacle():
    IGNORE_DISTANCE = rospy.get_param('/find_obstacle/ignore/distance') # ターゲットからいくらまでの近傍の障害物を無視するか [m]
    IGNORE_ANGLE_MIN = math.degrees(rospy.get_param('/find_obstacle/ignore/angle_min')) # 前方を0度として、半時計回りに何度からのデータのみ認識するか [deg]
    IGNORE_ANGLE_MAX = math.degrees(rospy.get_param('/find_obstacle/ignore/angle_max')) # 前方を0度として、半時計回りに何度までのデータのみ認識するか [deg]
    WARNING_DISTANCE = rospy.get_param('/find_obstacle/warning/distance') # これより近くに障害物があった場合、警告を出します [m]
    DANGER_DISTANCE = rospy.get_param('/find_obstacle/warning/distance') # これより近くに障害物があった場合、危険と判断して停止します [m]

    def __init__(self):
        rospy.init_node('FindObstacle')
        self.sub = rospy.Subscriber('/tracked_obstacles', Obstacles, self.callback)
        self.trigger_pub = rospy.Publisher('/trigger_action', TriggerAction, queue_size=10)
        self.sound_pub = rospy.Publisher('/trigger_action', TriggerAction, queue_size=10)

    def callback(self, obstacles):
        # 障害物を検知し、一定の距離以内にあれば通知する
        circles = obstacles.circles
        for circle in circles:
            # 距離と角度を算出
            distance = math.sqrt(circle.center.x**2, circle.center.z**2)
            angle = math.atan2(circle.center.z, circle.center.x)
            if angle > math.pi/2:
                angle -= math.pi
            elif angle < -math.pi/2:
                angle += math.pi
            # 近傍の場合は無視
            if distance < self.IGNORE_DISTANCE:
                continue
            # 範囲外の場合は無視
            if angle > self.IGNORE_ANGLE_MAX:
                continue
            if angle < self.IGNORE_ANGLE_MIN:
                continue
            # 危険な位置にある場合は停止コマンド送信
            if distance < self.DANGER_DISTANCE:
                self.trigger_pub.publish(TriggerAction.TRIGGER_DETECT_DANGER_OBSTACLE)
                return
            # 近い位置にある場合は警告音声を再生
            if distance < self.WARNING_DISTANCE:
                debug.logwarn('detected obstacle: d={}, theta={}'.format(distance, angle))


if __name__ == '__main__':
    find_obstacle = FindObstacle()
    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        R.sleep()
