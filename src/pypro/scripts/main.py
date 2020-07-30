#!/usr/bin/env python3
from __future__ import print_function
import roslib
#roslib.load_manifest('opencv_test_python')
import sys
import rospy
#import cv2
#from std_msgs.msg import String
#from sensor_msgs.msg import Image
#from cv_bridge import CvBridge, CvBridgeError
#from sensor_msgs.msg import LaserScan
#import numpy as np
#from matplotlib import pyplot as plt
import commands as cmd
#import msvcrt
import keyboard
import pyproacmd
from pyproacmd import Utils
import struct
import time


class KeyCtrlr:
    def __init__(self, proacmd, id_L=1, id_R=2):
        self.pc = proacmd
        self.id_L = id_L
        self.id_R = id_R

    def forward_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))
    
    def backward_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-1200)))

    def left_rotate_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))
    
    def right_rotate_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-1200)))

    def enable_handler(self):
        result = self.pc.send_receive(cmd.Enable(self.id_R))

    def disable_handler(self):
        result = self.pc.send_receive(cmd.Disable(self.id_R))
    
    def read_foc_handler(self):
        result = self.pc.send_receive(cmd.ReadFOC(self.id_R))
    
    def move_to_handler(self, pos):
        result = self.pc.send_receive(cmd.MoveTo(self.id_R, pos))

    def close(self):
        self.pc.sclose()

class KeyCtrll:
    def __init__(self, proacmd, id_L=1, id_R=2):
        self.pc = proacmd
        self.id_L = id_L
        self.id_R = id_R

    def forward_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))
    
    def backward_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(-1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-1200)))

    def left_rotate_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(-1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(1200)))
    
    def right_rotate_handler(self):
        result = self.pc.send_receive(cmd.RunAtVel(self.id_L, Utils.RPMtoRADpS(1200)))
        #result = self.pc.send_receive(cmd.RunAtVel(self.id_R, Utils.RPMtoRADpS(-1200)))

    def enable_handler(self):
        result = self.pc.send_receive(cmd.Enable(self.id_L))
        #result = self.pc.send_receive(cmd.Disable(self.id_R))

    def disable_handler(self):
        result = self.pc.send_receive(cmd.Disable(self.id_L))
        #result = self.pc.send_receive(cmd.Disable(self.id_R))
    
    def read_foc_handler(self):
        result = self.pc.send_receive(cmd.ReadFOC(self.id_L))
        #result = self.pc.send_receive(cmd.ReadFOC(self.id_R))
    
    def move_to_handler(self, pos):
        result = self.pc.send_receive(cmd.MoveTo(self.id_L, pos))

    def close(self):
        self.pc.sclose()


def main(args):
    rospy.init_node('image_converter', anonymous=True)
    #ic = image_converter()
    #try:
    #    rospy.spin()
    #except KeyboardInterrupt:
    #    print("Shutting down")
    #    cv2.destroyAllWindows()
    baud = 1000000
    print ('Start Test')
    #with pyproacmd.ProaCmd('/dev/ttyACM0', baud) as pc:
    pc = pyproacmd.ProaCmd('/dev/ttyACM0', baud)
    pc2 = pyproacmd.ProaCmd('/dev/ttyACM1', baud)
    kc = KeyCtrlr(pc)
    kc2 = KeyCtrll(pc2)

    continuous = False

    try:
        while True:
            time.sleep(0.01)

            if keyboard.is_pressed('e'): #if c == 'e':
                kc.enable_handler()
                #print('enable1')
                kc2.enable_handler()
        
            elif keyboard.is_pressed('i'): #elif c == 'i':
                kc.forward_handler()
                kc2.forward_handler()
                kc.read_foc_handler()
                kc2.read_foc_handler()

            elif keyboard.is_pressed('j'):#elif c == 'j':
                kc.backward_handler()
                kc2.backward_handler()
                kc.read_foc_handler()
                kc2.read_foc_handler()

    except KeyboardInterrupt:
        print('Ctrl-C')
        kc.close()
        kc2.close()


if __name__ == '__main__':
    main(sys.argv)
