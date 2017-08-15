/*
   Hello CPP
 */
#include<ros/ros.h>

int main(int argc,char** argv)
{
  ros::init(argc,argv,"hello"); // Registering a node in ros master
  ROS_INFO("Welcome to ROSRobot!");
  return 0;
}