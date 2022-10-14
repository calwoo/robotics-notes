#!/usr/bin/env python

"""Python rocket control node using PID controller.

Author: Nathan Sprague & ???
Version:

"""
import rclpy
import rclpy.node

from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3

from jmu_ros2_util import pid


class GuidanceNode(rclpy.node.Node):
    def __init__(self):
        super().__init__('guidance_node')

        self.create_subscription(Point, 'location', self.location_callback, 10)
        self.create_subscription(Point, 'target_event', self.target_callback,
                                 10)

        self.thrust_pub = self.create_publisher(Vector3, 'thrust', 10)

        # Set an arbitrary initial target
        self.target = Point()
        self.target.x = 240.0
        self.target.y = 100.0
        self.target.z = 0.0

        # THESE SHOULD BE READ FROM PARAMETERS!
        self.declare_parameter("p_x_gain", 0.0)
        self.declare_parameter("i_x_gain", 0.0)
        self.declare_parameter("d_x_gain", 0.0)
        self.declare_parameter("p_y_gain", 0.0)
        self.declare_parameter("i_y_gain", 0.0)
        self.declare_parameter("d_y_gain", 0.0)

        p_x_gain = self.get_parameter("p_x_gain").get_parameter_value().double_value
        i_x_gain = self.get_parameter("i_x_gain").get_parameter_value().double_value
        d_x_gain = self.get_parameter("d_x_gain").get_parameter_value().double_value
        p_y_gain = self.get_parameter("p_y_gain").get_parameter_value().double_value
        i_y_gain = self.get_parameter("i_y_gain").get_parameter_value().double_value
        d_y_gain = self.get_parameter("d_y_gain").get_parameter_value().double_value

        self.pid_x = pid.PID(p_x_gain, i_x_gain, d_x_gain)
        self.pid_x.reset()

        self.pid_y = pid.PID(p_y_gain, i_y_gain, d_y_gain)
        self.pid_y.reset()

        log_str = "P_x gain: {}, I_x gain: {}, D_x gain: {}"
        self.get_logger().info(log_str.format(p_x_gain, i_x_gain, d_x_gain))

        log_str = "P_y gain: {}, I_y gain: {}, D_y gain: {}"
        self.get_logger().info(log_str.format(p_y_gain, i_y_gain, d_y_gain))

    def location_callback(self, location):
        thrust = Vector3()

        # if location.y < self.target.y:
        #     thrust.y = 20.0

        error_x = self.target.x - location.x
        error_y = self.target.y - location.y

        control_cmd_x = self.pid_x.update_PID(error_x)
        control_cmd_y = self.pid_y.update_PID(error_y)
        thrust.x = control_cmd_x
        thrust.y = control_cmd_y
        self.get_logger().info(f"Command for thrust-- x: {control_cmd_x}  y: {control_cmd_y}")

        self.thrust_pub.publish(thrust)

    def target_callback(self, target_msg):
        self.target = target_msg


def main():
    rclpy.init()
    thruster_node = GuidanceNode()
    rclpy.spin(thruster_node)

    thruster_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
