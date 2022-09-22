"""
Some help from: https://medium.com/@danieljeswin/introduction-to-programming-with-ros2-launch-files-52eac873f9d0
"""

import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import launch_ros.actions
from launch_ros.actions import Node


def generate_launch_description():

    # We need to get the path to the .rviz file...
    this_prefix = get_package_share_directory('skibot')
    images = os.path.join(this_prefix, 'images')

    return LaunchDescription([
        Node(
            package="skibot",
            executable="skibot_node",
            name="skibot_node",
            arguments=['-d', images]
        ),
    ])
