#!/bin/bash

# Start roscore
roscore &
P1=$!

# Talker
source ~/ROSRobot/ros-app/devel/setup.bash
roslaunch talker talker.launch &
P2=$!

# Listener
source ~/ROSRobot/ros-app-py/devel/setup.bash
roslaunch listener listener.launch &
P3=$!

wait &P1 &P2 &P3
