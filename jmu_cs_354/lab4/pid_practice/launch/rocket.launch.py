from launch import LaunchDescription
from launch_ros.actions import Node

from launch import LaunchContext
from launch.actions import SetEnvironmentVariable


def generate_launch_description():

    return LaunchDescription([
        Node(
            package="pid_practice",
            executable="guidance",
            name="guidance_node",
            output="screen",
            parameters=[
                {"p_y_gain": 0.8,
                 "i_y_gain": 0.5,
                 "d_y_gain": 1.0,
                 "p_x_gain": 0.8,
                 "i_x_gain": 0.5,
                 "d_x_gain": 1.0}
            ]
        ),
        Node(
            package="rocketbot",
            executable="rocketbot_node",
            name="rocketbot_node",
            output="screen")

    ])
