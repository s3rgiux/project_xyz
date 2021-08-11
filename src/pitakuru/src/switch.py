#!/usr/bin/env python
# coding: utf-8
import json
import serial
import rospy
from pitakuru.msg import  TriggerAction
from std_msgs.msg import Int16,Float32
import subprocess


class SwitchInput(object):
    def __init__(self):
        rospy.init_node('PitakuruState')
        self.ser = serial.Serial('/dev/serial/by-id/usb-Arduino_LLC_Arduino_Micro-if00', 115200, timeout=0.1)
        self.button_states = dict()
        self.current_bumper = 1 
        self.volts = 0
        self.pow_btn = 0
        self.sub_alerts = rospy.Subscriber('/alerts', Int16, self.alerts_cb,queue_size=1)
        self.pub = rospy.Publisher('trigger_action', TriggerAction, queue_size=2)
        self.pub_volt = rospy.Publisher('volts', Float32, queue_size=1)
        rospy.on_shutdown(self.shutdown)
        self.alert = 0
        self.mode = 2
        self.collision = False
        self.status_on = False
        self.count_status = 0
        
#//6 collision 5 danger 4 warning 3 karugamo 2 idle 1 manual
#//8 peop follow 6 collision 5 danger 4 warning 3 nothing 2 idle 1 manual with sound
#//78 peop follow 6 collision 75 danger 74 warning 73 nothing 72 idle 71 manual no sound

    def alerts_cb(self,data):
        self.mode = data.data
        if(self.mode == 100):
            self.turn_off_led()
        if(self.mode == 6):##handles collision and overrides the others
            self.ser.write(b'4')
            self.collision=True
        if(self.mode == 76):##just turn red no collision
            self.ser.write(b'4')
        if(self.mode == 2 and self.collision == True):
            self.collision=False
            self.ser.write(b'2')
        if(self.alert == 0 and self.mode == 2 or self.mode == 72 and self.collision == False):#handles modes without danger
            self.ser.write(b'2')
        elif(self.alert == 0 and self.mode == 1 or self.mode == 71 and self.collision == False):
            self.ser.write(b'1')
        elif(self.alert == 0 and self.mode == 3 or self.mode == 73 and self.collision == False):
            self.ser.write(b'6')
        if(self.mode == 5 or self.mode == 75 and self.collision == False):
            self.ser.write(b'5')
            self.alert = 1
        elif(self.alert == 1 and self.mode == 2 or self.mode == 72 and self.collision == False):
            self.alert = 0
            self.ser.write(b'2')
        elif(self.alert == 1 and self.mode == 1 or self.mode == 71 and self.collision == False):
            self.alert = 0
            self.ser.write(b'1')
        elif(self.alert == 1 and self.mode == 3 or self.mode == 73 and self.collision == False):
            self.alert = 0
            self.ser.write(b'6')
        elif(self.alert == 1 and self.mode == 8 or self.mode == 78 and self.collision == False):
            self.alert = 0
            self.ser.write(b'3') 
        elif(self.alert == 0 and self.mode == 8 or self.mode == 78 and self.collision == False):
            self.ser.write(b'3')
        
    def request_current_state(self):
        self.ser.write(b'7')

    def turn_off_led(self):
        self.ser.write(b'0')

    def shutdown(self):
        rospy.logwarn("shutting down switch node")
        self.ser.write(b'0')
        self.ser.close()
    
    def update(self):
        current_states_str = self.ser.readline()
        if not current_states_str:
            return

        current_states = json.loads(current_states_str)
        tmp = current_states['bumper']
        self.current_bumper = tmp
        self.button_states["karugamo"] = current_states['SW0']
        self.button_states["idle"] = current_states['SW1']
        self.volts=current_states['A0']
        self.pow_btn=current_states['A1']
        volts_read = Float32()
        volts_read.data=self.volts*0.03202 #according to the resistor divider
        self.pub_volt.publish(volts_read)

        if(self.pow_btn < 200):
            self.count_status=self.count_status+1
            if(self.count_status>2):
                self.count_status=0
                self.request_current_state()
                self.shutdown()
                rospy.logerr("matando desde switch normal")
                rospy.logerr("subprocess")
                subprocess.call(["/home/xavier/pow_off.sh"])
                rospy.logerr("subprocess")
                self.status_on=False
        else:
            self.count_status=0

        trigger_action = TriggerAction()
        rospy.logerr(self.button_states)
        if self.current_bumper  ==  0:
            trigger_action.trigger = TriggerAction.TRIGGER_COLLISION
        if self.current_bumper == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_BREAK_RELEASE_BUTTON_ON
       
        if self.button_states["karugamo"] == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_KARUGAMO_BUTTON_ON
        if self.button_states["idle"] == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_IDLE_BUTTON_ON
        if not trigger_action.trigger:
            trigger_action.trigger = TriggerAction.TRIGGER_IDLE_BUTTON_ON
        self.pub.publish(trigger_action)

    def getButton(self,name):
        return self.button_states[name]

if __name__ == "__main__":
    switch_input = SwitchInput()
    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        switch_input.update()
        R.sleep()
