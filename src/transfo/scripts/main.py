#!/usr/bin/env python  
import roslib
#roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('tf_listener')
    listener = tf.TransformListener()
    #rospy.wait_for_service('spawn')
    #spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    #spawner(4, 2, 0, 'turtle2')
    pub_init_pose = rospy.Publisher('/initial pose', geometry_msgs.msg.PoseWithCovarianceStamped)
    nuevain=geometry_msgs.msg.PoseWithCovarianceStamped()
  
    pub_init_pose.publish()
    rate = rospy.Rate(10.0)
    first=True
    pu
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/odom', '/base_footprint', rospy.Time(0))
            #nuevain.pose.pose.position.x=trans[1]
            if first:
                first=False
                print("published")
                #pub_init_pose.publish
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        print("translation")
        print(trans)
        print(trans[0])
        print(trans[1])
        print(trans[2])
        print("rotation")
        print(rot)

        #angular = 4 * math.atan2(trans[1], trans[0])
        #linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        #cmd = geometry_msgs.msg.Twist()
        #cmd.linear.x = linear
        #cmd.angular.z = angular
        #turtle_vel.publish(cmd)

        rate.sleep()
