#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim_spawn_interfaces.msg import TurtleArray

class TurtleController(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.target_turtle = None
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
        self.twist_publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)

    def register_target(self, msg):
        if self.target_turtle is None:
            turtles = msg.turtles
            # pick first turtle as target
            if len(turtles) > 0:
                self.target_turtle = turtles[0]
                self.get_logger().info(f"targetting: {self.target_turtle.name}")

    def pose_listener_callback(self, msg):
        pass

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
