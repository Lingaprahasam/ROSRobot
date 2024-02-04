#!/bin/bash
# Define variables
USER_NAME="rosadmin"

docker rmi ros-humble-custom:latest
docker build -t ros-humble-custom /home/$USER_NAME/ROSRobot/Docker/ros_humble_custom/