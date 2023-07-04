#!/usr/bin/env python3

import math
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim_spawn_interfaces.msg import TurtleArray
from turtlesim_spawn_interfaces.srv import CatchTurtle

class TurtleController(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        # state
        self.turtle_pose = None
        self.target_turtle = None

        # subscriptions
        self.turtles_subscription = self.create_subscription(
            TurtleArray,
            "turtle_spawner/alive_turtles",
            self.register_target,
            10
        )
        self.pose_subscription = self.create_subscription(
            Pose,
            "turtle1/pose",
            self.pose_listener_callback,
            10
        )

        # control topics
        control_loop_period = 0.01
        self.control_loop_timer = self.create_timer(control_loop_period, self.control_loop)
        self.twist_publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.catch_client = self.create_client(CatchTurtle, "turtle_spawner/catch")

    def register_target(self, msg):
        if self.target_turtle is None:
            turtles = msg.turtles
            # pick first turtle as target
            if len(turtles) > 0:
                self.target_turtle = turtles[0]
                self.get_logger().info(f"targetting: {self.target_turtle.name}")

    def pose_listener_callback(self, msg):
        self.turtle_pose = msg

    def control_loop(self):
        if self.turtle_pose is None:
            return None
    
        if not self.target_turtle is None:
            twist_msg = Twist()

            x_diff = self.target_turtle.x - self.turtle_pose.x
            y_diff = self.target_turtle.y - self.turtle_pose.y
            theta_diff = math.atan2(y_diff, x_diff) - self.turtle_pose.theta
            if theta_diff > math.pi:
                theta_diff -= 2 * math.pi
            elif theta_diff < -math.pi:
                theta_diff += 2 * math.pi
            distance = math.sqrt(x_diff ** 2 + y_diff ** 2)

            if distance < 0.5:
                twist_msg.linear.x = 0.0
                twist_msg.angular.z = 0.0

                self.catch_turtle()
            else:
                twist_msg.linear.x = 2 * distance
                twist_msg.angular.z = 6 * theta_diff

            self.twist_publisher.publish(twist_msg)

    def catch_turtle(self):
        turtle_name = self.target_turtle.name
        request = CatchTurtle.Request()
        request.turtle_name = turtle_name
        
        future = self.catch_client.call_async(request)
        future.add_done_callback(self.catch_turtle_callback)

    def catch_turtle_callback(self, future):
        try:
            response = future.result()
            if response.return_code == 1:
                self.get_logger().info("turtle caught!")
            else:
                self.get_logger().error("turtle was invalid somehow")
            self.target_turtle = None
        except Exception as e:
            self.get_logger().error(f"service call failed: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
