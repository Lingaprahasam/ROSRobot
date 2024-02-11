# This is an auto generated Dockerfile for ros:ros-base
# generated from docker_images_ros2/create_ros_image.Dockerfile.em
FROM ros:humble-ros-core-jammy

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    git \
    python3-colcon-common-extensions \
    python3-colcon-mixin \
    python3-rosdep \
    python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init && \
  rosdep update --rosdistro $ROS_DISTRO

# setup colcon mixin and metadata
RUN colcon mixin add default \
      https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml && \
    colcon mixin update && \
    colcon metadata add default \
      https://raw.githubusercontent.com/colcon/colcon-metadata-repository/master/index.yaml && \
    colcon metadata update

# install ros2 packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-humble-ros-base=0.10.0-1* \
    && rm -rf /var/lib/apt/lists/*

# ROS2 environment variables
ENV ROS_SETUP_SCRIPT=/opt/ros/humble/setup.bash
ENV ROS_DOMAIN_ID=10


# source ros distro setup.bash
# ENTRYPOINT ["/bin/bash", "ros_entrypoint.sh"]
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source /opt/rosrobot_ws/install/setup.bash" >> ~/.bashrc

# User permission from root to user
# By default docker image will run from root
# When host folder is mapped to docker image and run by the conatiner
# the permission will be changed as root
ARG USERNAME=ros
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
  && mkdir /home/$USERNAME/.config && chown $USER_UID:$USER_GID /home/$USERNAME/.config

# Setup sudo
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME \
  && rm -rf /var/lib/apt/lists/*

# install other packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    wget \
    nano \
    # wiringpi \
    python3-gpiozero \
    python3-pigpio \
    && rm -rf /var/lib/apt/lists/*
    
# pip install
RUN pip install setuptools==58.2.0

# install pi gpio packages
RUN wget --no-check-certificate https://project-downloads.drogon.net/wiringpi-latest.deb
# continue executing even if command fails
RUN dpkg -i wiringpi-latest.deb || true