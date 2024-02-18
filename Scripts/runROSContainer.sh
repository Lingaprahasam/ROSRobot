#!/bin/bash
# Define variables
USER_NAME="rosadmin"
IMAGE_NAME="ros-humble-custom"
CONTAINER_NAME="ros2-container"

[[ $(docker ps -al -f name=$CONTAINER_NAME --format '{{.Names}}') == $CONTAINER_NAME ]] ||
docker run --user ros --network=host --ipc=host  --privileged --device=/dev/gpiomem0 -v /home/rosadmin/ROSRobot/ros2_ws:/opt/ros2_ws --name ros2-container ros-humble-custom:latest tail -f /dev/null

# Doing tail after running, the below command doesn't execute
#docker exec -it ros2-container /bin/bash