import copy
import struct
import time
import math

from proacmd import pyproacmd
from proacmd import commands as cmd
from proacmd.pyproacmd import Utils

from config import config


# "Two-Wheel Drive" 
class TWDController: 
    eI = 0 # integral
    theta_old = 0 # old_value of theta

    def __init__(self, C=config()):
        self.C = C
        self.pc_left = pyproacmd.ProaCmd(C['motor']['port_left'], C['motor']['baud'])
        self.pc_left.setup()
        self.pc_right = pyproacmd.ProaCmd(C['motor']['port_right'], C['motor']['baud'])
        self.pc_right.setup()
        self.id_L = 2
        self.id_R = 1

    def send_rpm(self, left_rpm, right_rpm):
        left_rpm = -left_rpm

        if left_rpm == 0 or right_rpm == 0:
            self.pc_left.send_receive(cmd.Disable(self.id_L))
            self.pc_right.send_receive(cmd.Disable(self.id_R))
        else:
            result_left = self.pc_left.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(left_rpm)))
            result_right = self.pc_right.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(right_rpm)))

    
    def thresh_theta(self, theta):
        if theta > math.pi:
            return theta - 2*math.pi
        return theta

    # joystickの十字キーからrpmへ変換
    def dpad_to_rpm(self, up, left, down, right):
        max_speed = self.C['joystick']['max_ud']
        low_speed = self.C['joystick']['max_lr']
        if up == 1:
            self.send_rpm(max_speed, max_speed)
        elif down == 1:
            self.send_rpm(-max_speed, -max_speed)
        elif left == 1:
            self.send_rpm(low_speed, -low_speed)
        elif right == 1:
            self.send_rpm(-low_speed, low_speed)
        else:
            self.send_rpm(0, 0)

    # joystickコントローラのx/yからrpmへ変換
    def ctrlv_to_rpm(self, raw_x, raw_y):
        rpm_left, rpm_right = 0, 0

        # ジョイスティックのX, Yの範囲
        # 範囲: 0~1023
        # 中央値:        
        cx = self.C['joystick']['js_center_x']
        cx = self.C['joystick']['js_center_y']
        c_diff = self.C['joystick']['js_center_diff']
        maxspeed = self.C['joystick']['manual_max_speed']
        x = raw_x * maxspeed
        y = raw_y * maxspeed
        r = math.sqrt(x**2 + y**2)


        th = math.atan2(y, x) #  -pi < theta < +pi

        if r < self.C['joystick']['js_neutral_area']:
            print("NEUTRAL AREA")
            rpm_left, rpm_right = 0, 0
        elif th >= -math.pi/8 and th <= math.pi/2:
            print("1st q")
            rpm_left = r
            rpm_right = -2*x*x/r + r
        elif th > math.pi/2 or th < -7*math.pi/8:
            print("2nd q")
            rpm_left = -2*x*x/r + r
            rpm_right = r
        elif th < -math.pi/2:
            print("3rd q")
            rpm_left = 2*x*x/r - r
            rpm_right = 0 - r
        elif th < 0 and th >= -math.pi/2:
            print("4th q")
            rpm_left = 0 - r
            rpm_right = 2*x*x/r - r
        else:
            print("Exception")
            # rpm_left = 0
            # rpm_right = 0

        v = 500
        lv = 100
        if rpm_left > lv and rpm_left < v:
            rpm_left = v
        if rpm_right > lv and rpm_right < v:
            rpm_right = v
        if rpm_left < -lv and rpm_left > -v:
            rpm_left = -v
        if rpm_right < -lv and rpm_right > -v:
            rpm_right = -v

        print('L:{}, R:{}'.format(rpm_left, rpm_right))
        self.send_rpm(rpm_left, rpm_right)

    def follow(self, distance, theta):
        theta = self.thresh_theta(theta)

        interval = self.C['motor']['interval']
        max_speed_rpm = self.C['motor']['max_speed_rpm']
        speed_p = self.C['motor']['speed_p']
        steer_p = self.C['motor']['steer_p']
        steer_i = self.C['motor']['steer_i']
        steer_d = self.C['motor']['steer_d']

        v = min(speed_p * distance, max_speed_rpm)
        self.eI = self.eI + interval * theta; # Integral

        delta_v = steer_p * theta + steer_i * self.eI + steer_d * (theta - self.theta_old) / interval
        self.theta_old = theta
        
        print("delta_v: ", delta_v)

        rpm_left = v - delta_v
        rpm_right = v + delta_v
        print('L:{}, R:{}'.format(rpm_left, rpm_right))
        self.send_rpm(rpm_left, rpm_right)

if __name__ == '__main__':
    twd = TWDController()
    print("dist: 100, theta: 0")
    twd.follow(100, 0)
    print("dist: 50, theta: -pi/2")
    twd.follow(50, -3.1415/2)

