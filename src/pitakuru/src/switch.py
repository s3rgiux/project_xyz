#!/usr/bin/env python
# coding: utf-8
import json
import serial

import rospy
from pitakuru.msg import State, TriggerAction
from std_msgs.msg import Int16


class SwitchInput(object):
    def __init__(self):
        rospy.init_node('PitakuruState')
        
        self.ser = serial.Serial(rospy.get_param('/switch/port_name'), rospy.get_param('/switch/baudrate'), timeout=rospy.get_param('/switch/timeout'))
        self.button_states = dict()
        self.current_bumper = 1 

        #self.sub = rospy.Subscriber('state', State, self.callback)
        self.sub_alerts = rospy.Subscriber('/alerts', Int16, self.alerts_cb,queue_size=1)
        self.pub = rospy.Publisher('trigger_action', TriggerAction, queue_size=5)
        rospy.on_shutdown(self.shutdown)
        self.alert = 0
        self.mode = 2
        self.collision=False
#//6 collision 5 danger 4 warning 3 karugamo 2 idle 1 manual


    def alerts_cb(self,data):
        self.mode=data.data
        
        if(self.mode==6):##handles collision and overrides the others
            self.ser.write(b'4')
            self.collision=True
        if(self.mode==2 and self.collision==True):
            self.collision=False
            self.ser.write(b'2')

        if(self.alert==0 and self.mode==2 and self.collision==False):#handles modes without danger
            self.ser.write(b'2')
        elif(self.alert==0 and self.mode==1 and self.collision==False):
            self.ser.write(b'1')
        elif(self.alert==0 and self.mode==3 and self.collision==False):
            self.ser.write(b'6')
            
        if(self.mode==5 and self.collision==False):#changed 4 danger/warning
            self.ser.write(b'5')
            self.alert = 1
        elif(self.alert==1 and self.mode==2 and self.collision==False):
            self.alert = 0
            self.ser.write(b'2')
        elif(self.alert==1 and self.mode==1 and self.collision==False):
            self.alert = 0
            self.ser.write(b'1')
        elif(self.alert==1 and self.mode==3 and self.collision==False):
            self.alert = 0
            self.ser.write(b'6')
        elif(self.alert==1 and self.mode==8 and self.collision==False):
            self.alert = 0
            self.ser.write(b'3') 
        elif(self.alert==0 and self.mode==8 and self.collision==False):
            self.ser.write(b'3')
        
        

    def request_current_state(self):
        self.ser.write(b'7')

    #def callback(self, state):
        #self.set_LED_color(state)

    def shutdown(self):
        rospy.logwarn("shutting down switch node")
        #self.set_LED_color()
        self.ser.write(b'0')
        self.ser.close()
    
    def update(self):
        current_states_str = self.ser.readline()
        if not current_states_str:
            self.button_states["break"] = 0
            self.button_states["release"] = 0
            self.button_states["karugamo"] = 0
            self.button_states["idle"] = 0
            return

        current_states = json.loads(current_states_str)
        tmp = current_states['bumper']
        if self.current_bumper == tmp:
            self.button_states["break"] = 0
            self.button_states["release"] = 0
        elif self.current_bumper < tmp:
            self.button_states["break"] = 0
            self.button_states["release"] = 1
        elif self.current_bumper > tmp:
            self.button_states["break"] = 1
            self.button_states["release"] = 0
        self.current_bumper = tmp
        self.button_states["karugamo"] = current_states['SW0']
        self.button_states["idle"] = current_states['SW1']

        trigger_action = TriggerAction()
        rospy.logerr(self.button_states)
        if self.button_states["break"] == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_COLLISION
        if self.button_states["release"] == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_BREAK_RELEASE_BUTTON_ON
        if self.button_states["karugamo"] == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_KARUGAMO_BUTTON_ON
        if self.button_states["idle"] == 1:
            trigger_action.trigger = TriggerAction.TRIGGER_IDLE_BUTTON_ON
        if not trigger_action.trigger:
            trigger_action.trigger = TriggerAction.TRIGGER_BREAK_RELEASE_BUTTON_ON
        self.pub.publish(trigger_action)

    def getButton(self,name):
        return self.button_states[name]

    #def set_LED_color(self, state=State):
        #if state.state == State.STATE_ACTIVE_KARUGAMO and self.alert != 1:
            # rgb = 110 (yellow)
            ##self.ser.write(b'6')
        #elif state.state == State.STATE_IDLE and self.alert != 1:
            # rgb = 010 (green)
            ##self.ser.write(b'2')
        #elif state.state == State.STATE_ACTIVE_MANUAL and self.alert != 1:
            # rgb = 001 (blue)
            ##self.ser.write(b'1')
        #elif state.state == State.STATE_ERROR_OBSTACLE or self.mode == 5:
            # rgb = 101 (violet)
            ##self.ser.write(b'5')
        #elif state.state == State.STATE_ERROR_COLLISION:
            # rgb = 100 (red)
            ##self.ser.write(b'4')
        #else:
            # rgb = 000 (off)
            ##self.ser.write(b'0')


if __name__ == "__main__":
    switch_input = SwitchInput()
    switch_input.request_current_state()
    # 制御周期
    ROS_RATE = 30
    R = rospy.Rate(ROS_RATE)
    # [ctrl]+[c]でプログラムの終了するまでループ
    while not rospy.is_shutdown():
        switch_input.update()
        R.sleep()
