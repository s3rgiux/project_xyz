#include "ros/ros.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv,"my_first_pkg_node");
  ros::NodeHandle n;
  //ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);

  ros::Rate loop_rate(10);

  //int count = 0;
  while (ros::ok())
  {
    /**
     * This is a message object. You stuff it with data, and then publish it.
     */
    //std_msgs::String msg;
    ROS_INFO("Hola mundo");
    ///chatter_pub.publish(msg);

    //ros::spinOnce();

    loop_rate.sleep();
    //++count;
  }


  return 0;
}
