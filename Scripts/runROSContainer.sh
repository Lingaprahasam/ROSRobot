#!/bin/bash
# Define variables
IMAGE_NAME="ros-humble-custom"
CONTAINER_NAME="ros2-container"

[[ $(docker ps -al -f name=$CONTAINER_NAME --format '{{.Names}}') == $CONTAINER_NAME ]] ||
docker run -i -t -v ~/ros2_ws:/opt/ros2_ws  -d --name $CONTAINER_NAME $IMAGE_NAME