#!/usr/bin/env python3

import random
from functools import partial

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill


class TurtleSpawner(Node):
    def __init__(self):
        super().__init__("turtle_spawner")
        self.spawn_client = self.create_client(Spawn, "spawn")
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not available, waiting again...")

        # self.kill_service = ?

        spawn_period = 2.0
        self.spawn_timer = self.create_timer(spawn_period, self.spawn_turtle)

        # turtle store
        self.turtles = []

    def spawn_turtle(self):
        self.get_logger().info("spawning turtle!")
        turtle_x = random.uniform(0.0, 11.0)
        turtle_y = random.uniform(0.0, 11.0)

        request = Spawn.Request()
        request.x = turtle_x
        request.y = turtle_y
        request.theta = 0.0

        # call spawn service
        future = self.spawn_client.call_async(request)
        future.add_done_callback(partial(self.callback_spawn_turtle, turtle_x=turtle_x, turtle_y=turtle_y))

    def callback_spawn_turtle(self, future, turtle_x, turtle_y):
        try:
            turtle_name = future.result()
            self.get_logger().info(f"spawned turtle {turtle_name} @ x={turtle_x} y={turtle_y}")
        except Exception as e:
            self.get_logger().error(f"service call failed: {e}")

        turtle = {
            "x": turtle_x,
            "y": turtle_y,
            "name": turtle_name
        }
        self.turtles.append(turtle)

    def kill_turtle(self):
        pass

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawner()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
