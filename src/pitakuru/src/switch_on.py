#!/usr/bin/env python
# coding: utf-8
import json
import serial
import os
import rospy
import subprocess
from pitakuru.msg import State, TriggerAction
from std_msgs.msg import Int16,Float32


class SwitchInput(object):
    def __init__(self):
        rospy.init_node('PitakuruState')
        
        #self.ser = serial.Serial(rospy.get_param('/switch/port_name'), rospy.get_param('/switch/baudrate'), timeout=rospy.get_param('/switch/timeout'))
        self.ser = serial.Serial('/dev/serial/by-id/usb-Arduino_LLC_Arduino_Micro-if00', 115200, timeout=0.1)
        self.button_states = dict()
        self.current_bumper = 1 
        self.volts=0

        #self.sub = rospy.Subscriber('state', State, self.callback)
        self.sub_alerts = rospy.Subscriber('/alerts', Int16, self.alerts_cb,queue_size=1)
        self.pub = rospy.Publisher('trigger_action', TriggerAction, queue_size=2)
        self.pub_volt = rospy.Publisher('volts', Float32, queue_size=1)
        rospy.on_shutdown(self.shutdown)
        self.alert = 0
        self.mode = 2
        self.collision = False
        self.status_on = False
        self.count_status = 0
        self.gpid=0
#//6 collision 5 danger 4 warning 3 karugamo 2 idle 1 manual
#//8 peop follow 6 collision 5 danger 4 warning 3 nothing 2 idle 1 manual with sound
#//78 peop follow 6 collision 75 danger 74 warning 73 nothing 72 idle 71 manual no sound

    def alerts_cb(self,data):
        self.mode=data.data
       

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
            """self.button_states["break"] = 0
            self.button_states["release"] = 0
            self.button_states["karugamo"] = 0
            self.button_states["idle"] = 0
             """
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
        self.volts=current_states['A0']
        volts_read = Float32()
        volts_read.data=self.volts*0.03205#according to the resistor divider
        self.pub_volt.publish(volts_read)
        #if(self.button_states["karugamo"] == 1 and self.status_on==False):
        if(current_states['A1'] < 200 and self.status_on==False):
            self.count_status=self.count_status+1
            if(self.count_status>0):
                self.status_on=True
                self.count_status=0
                rospy.logerr("encendiendo")
                #self.request_current_state()
                #self.ser.write(b'6')
                # try:
                #     p=subprocess.Popen(["roslaunch","pitakuru","pitakuru_on_off.launch"])
                #     self.gpid=p.pid
                #     #print(self.gpid)
                # except:
                #     print('cant launch')
                #os.system("roslaunch pitakuru pitakuru_yolo_heavy.launch")
                #os.system("roslaunch pitakuru pitakuru_switch.launch")
                #subprocess.call(["shutdown", "-h", "now"])
                subprocess.call(["roslaunch", "pitakuru", "pitakuru_yolo_heavy.launch"])
                #subprocess.call(["/home/xavier/pow_off.sh"])
                rospy.logerr("matando desde on")
                #os.system('sudo systemctl poweroff')
        #else:
        #    self.count_status=0
        if(self.button_states["karugamo"] == 1 and self.status_on):
        # if(self.button_states["karugamo"] == 1):
            self.count_status=self.count_status+1
            if(self.count_status>2):
                #os.system("shutdown /s /t 1")
                #request_current_state()
                self.shutdown()
                os.system('systemctl poweroff')
                self.status_on=False

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
            trigger_action.trigger = TriggerAction.TRIGGER_IDLE_BUTTON_ON#TRIGGER_BREAK_RELEASE_BUTTON_ON
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
