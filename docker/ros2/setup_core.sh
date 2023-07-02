#!/bin/bash

source /opt/ros/humble/setup.bash
colcon build
source install/local_setup.bash

exec "$@"
