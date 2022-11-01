FROM ubuntu:22.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y locales curl gnupg2 lsb-release sudo git && \
    locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
    export LANG=en_US.UTF-8 && \
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -  && \
    sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list' && \
    rm -rf /var/lib/apt/lists/*

ENV LANG en_US.UTF-8

# ROS2 environment vars
ENV ROS_DISTRO="humble"
ENV ROS_PYTHON_VERSION="3"
ENV ROS_VERSION="2"

# install ROS 2
RUN apt-get update && \
    apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install tzdata && \
    apt-get install -y ros-${ROS_DISTRO}-desktop

# install colcon build tool
RUN apt-get install -y \
    python3-argcomplete \
    python3-rosdep \
    python3-colcon-common-extensions

ENV SHELL=/bin/bash

# set development workspace
WORKDIR /root/dev_ws/src
RUN git clone https://github.com/ros/ros_tutorials.git -b foxy-devel
WORKDIR /root/dev_ws

# copy setup script
COPY ./setup.sh /root/.
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

ENTRYPOINT ["/root/setup.sh"]
CMD ["bash"]
