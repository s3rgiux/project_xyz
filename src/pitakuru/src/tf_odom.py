#!/usr/bin/env python  
import sys,time
from time import sleep
import rospy
import math
import tf,tf2_ros
import geometry_msgs.msg

#import turtlesim.srv
from geometry_msgs.msg import Twist, Pose, TransformStamped,Quaternion
from sensor_msgs.msg import Imu, JointState
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import *
from geometry_msgs.msg import Point, Vector3, PoseWithCovarianceStamped
SLEEP_TIME = 0.05
class Transformation:
    def __init__(self):
        
        self.tfBuffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tfBuffer)
        self.new_odo = rospy.Publisher('/odom2', Odometry, queue_size=1)
        self.odom_sub = rospy.Subscriber('/odom',Odometry, self.odom_callback, queue_size=1)  
        self.odo = Odometry()
        self.odo.header.frame_id='odom2'
        self.odo.child_frame_id='base_link' #quick fix
        self.odocount = 0
        self.frame1 = 'map'
        self.frame2 = 'base_link'
        self.x = 0
        self.y = 0
        self.quat= Quaternion()
        self.current_time = time.time()
        self.last_time = time.time()
        #rospy.Subscriber('/euler2', Float64, self.angle_callback, queue_size=1)
        #self.tf_broadcaster = tf2_ros.TransformBroadcaster()
        #self.odom_trans = TransformStamped()
        #self.odom_trans.header.stamp = rospy.Time.now()
        #self.odom_trans.header.frame_id = "odom"
        #self.odom_trans.child_frame_id = "base_link"

    def pubodo2(self):
        try:
            print(3)                
        except:
            import traceback
            traceback.print_exc()

    def odom_callback(self,data):
        self.x= data.pose.pose.position.y
        self.y= data.pose.pose.position.y
        print(self.x)


    def pubodo(self):
        try:
            try:
                trans = self.tfBuffer.lookup_transform(self.frame1, self.frame2, rospy.Time())
            except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                print('error_trans')
                
            #msg = geometry_msgs.msg.Twist()
            self.current_time = time.time()
            self.last_time = time.time()
            print(trans.transform.translation.x)
            self.odocount += 1
            self.current_time = time.time()
            dt = self.current_time-self.last_time            
            self.odo.header.seq = self.odocount
            self.odo.header.stamp = rospy.Time.now()
            self.odo.pose.pose.position.x = 0 #self.x[0]
            self.odo.pose.pose.position.y = 0 #self.x[1]

            q = tf.transformations.quaternion_from_euler(0, 0, 0)
            self.odo.pose.pose.orientation = Quaternion(*q)
            self.odo.twist.twist.linear.x = 0
            self.odo.twist.twist.linear.y = 0
            self.odo.twist.twist.angular.z = 0
            self.new_odo.publish(self.odo)
            #self.odom_trans.header.stamp = rospy.Time.now()
            #self.odom_trans.transform.translation.x = self.x[0] #-self.x[1]
            #self.odom_trans.transform.translation.y = self.x[1] #self.x[0]
            #self.odom_trans.transform.translation.z = 0
            #self.odom_trans.transform.rotation = Quaternion(*q)
            #self.tf_broadcaster.sendTransform(self.odom_trans)

        except:
            import traceback
            traceback.print_exc()

    
    def correct_callback(self, data):
        
	rospy.logerr("got correct callback")
        self.yPosLas =data.pose.pose.position.y
        self.xPosLas =data.pose.pose.position.x
        self.can_correct=True
        self.dbg_pub.publish(self.yPosLas-self.x[1])
        

   

    def shutdown(self):
        rospy.sleep(0.1)
        

def tf_main():
    rospy.init_node('pit_wheels', anonymous = True)
    transf = Transformation()
    

    while not rospy.is_shutdown():
        transf.pubodo()
        sleep(SLEEP_TIME)
        
   

if __name__=='__main__':
    try:
        tf_main()
    except rospy.ROSInterruptException:
        print("finish")
        transf.shutdown()














