#!/bin/bash
# Define variables
IMAGE_NAME="ros-humble-custom"
CONTAINER_NAME="ros2-container"

[[ $(docker ps -al -f name=$CONTAINER_NAME --format '{{.Names}}') == $CONTAINER_NAME ]] ||
docker run --user ros --network=host --ipc=host  --privileged --device=/dev/gpiomem0 -v /home/rosadmin/ROSRobot/rosrobot_ws:/opt/rosrobot_ws --name ros2-container ros-humble-custom:latest tail -f /dev/null

# Doing tail after running, the below command doesn't execute
#docker exec -it ros2-container /bin/bash