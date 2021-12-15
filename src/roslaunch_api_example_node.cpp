/**
 * @file roslaunch_api_example_node.cpp
 * @brief This node is executed via python script
 */

#include "ros/subscriber.h"
#include <ros/ros.h>
#include <std_msgs/String.h>

void strCB(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("string CB! : %s", msg->data.c_str());
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "roslaunch_api_example_node");
  ros::NodeHandle nh;
  ROS_INFO("%s start", ros::this_node::getName().c_str());

  ros::Publisher data_pub = nh.advertise<std_msgs::String>("chatter", 1);
  ros::Subscriber data_sub = nh.subscribe("calling", 1, strCB);

  ros::Rate loop(10);
  while (ros::ok())
  {
    std_msgs::String msg;
    msg.data = "roslaunch API example : ";
    auto stamp = ros::Time::now();
    msg.data += std::to_string(stamp.toSec());
    data_pub.publish(msg);

    ros::spinOnce();
    loop.sleep();
  }

  return 0;
}
