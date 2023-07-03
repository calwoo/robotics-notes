from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="turtlesim",
            executable="turtlesim_node",
        ),
        Node(
            package="turtlesim_catch_them_all",
            executable="turtle_spawner",
        ),
        Node(
            package="turtlesim_catch_them_all",
            executable="turtle_controller",
        )
    ])