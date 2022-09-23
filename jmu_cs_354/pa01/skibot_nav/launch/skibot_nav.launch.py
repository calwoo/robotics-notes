from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="skibot",
            executable="skibot_node",
            name="skibot_node"
        ),
        Node(
            package="skibot_nav",
            executable="skibot_nav_node",
            name="skibot_nav_node"
        )
    ])