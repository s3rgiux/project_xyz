#!/usr/bin/env python
# coding: utf-8
import serial
import rospy
from sensor_msgs.msg import Imu

def main(ser):
    pub = rospy.Publisher('immu', Imu, queue_size=10)
    rospy.init_node('imu_m5stack')
    
    while not rospy.is_shutdown():
        line = ser.readline().strip()
        data = line.split(",")
        imu = Imu()
        imu.header.frame_id='immu'
        #imu.child_frame_id='base_link3' #quick fix
        imu.linear_acceleration.x = float(data[1])#float(data[0])
        imu.linear_acceleration.y = float(data[0])#float(data[1])
        imu.linear_acceleration.z = float(data[2])#float(data[2])
        imu.angular_velocity.x = float(data[4])#float(data[3])
        imu.angular_velocity.y = float(data[3])#float(data[4])
        imu.angular_velocity.z = float(data[5])#float(data[5])
        pub.publish(imu)
        rospy.sleep(0.01)
       

if __name__ == '__main__':
    try:
        port = '/dev/serial/by-id/usb-Silicon_Labs_CP2104_USB_to_UART_Bridge_Controller_01BAC551-if00-port0'
        baudrate = 2000000
        ser = serial.Serial(port, baudrate)
        main(ser)
    except rospy.ROSInterruptException:
        ser.close()
