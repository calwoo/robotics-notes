cmake_minimum_required(VERSION 3.8)
project(wheeled_robot_kinematics)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
# find_package(catkin REQUIRED COMPONENTS
#  geometry_msgs
#  message_generation
# )

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/DiffDriveAction.msg"
  "srv/DiffDriveFK.srv"
  "srv/DiffDriveIK.srv"
)

ament_package()
