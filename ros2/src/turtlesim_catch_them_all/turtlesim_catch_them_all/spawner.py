#!/usr/bin/env python3

import random
from functools import partial

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill
from turtlesim_spawn_interfaces.msg import Turtle, TurtleArray
from turtlesim_spawn_interfaces.srv import CatchTurtle


class TurtleSpawner(Node):
    def __init__(self):
        super().__init__("turtle_spawner")

        # spawn service
        self.spawn_client = self.create_client(Spawn, "spawn")
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("spawn service not available, waiting again...")

        spawn_period = 3.0
        self.spawn_timer = self.create_timer(spawn_period, self.spawn_turtle)

        # kill service
        self.catch_service = self.create_service(CatchTurtle, "turtle_spawner/catch", self.catch_turtle)
        self.kill_client = self.create_client(Kill, "kill")
        while not self.kill_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("kill service not available, waiting again...")

        # turtle status topic pub
        self.turtles = []
        self.alive_publisher = self.create_publisher(TurtleArray, "turtle_spawner/alive_turtles", 10)

        pub_timer_period = 0.5
        self.pub_timer = self.create_timer(pub_timer_period, self.broadcast_turtles)

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
            response = future.result()
            self.get_logger().info(f"spawned turtle {response.name} @ x={turtle_x} y={turtle_y}")
        except Exception as e:
            self.get_logger().error(f"service call failed: {e}")

        turtle = {
            "x": turtle_x,
            "y": turtle_y,
            "name": response.name
        }
        self.turtles.append(turtle)

    def catch_turtle(self, request, response):
        turtle_name = request.turtle_name
        for turtle in self.turtles:
            if turtle["name"] == turtle_name:
                # remove turtle
                self.turtles.remove(turtle)

                # call turtlesim kill service
                request = Kill.Request()
                request.name = turtle_name
                self.kill_client.call_async(request)
                self.get_logger().info(f"killed turtle: {turtle_name}")

                response.return_code = 1
                return response
        
        # no turtle found with this name
        response.return_code = 0
        return response
    
    def broadcast_turtles(self):
        array_msg = TurtleArray()
        array_msg.turtles = []
        for turtle in self.turtles:
            turtle_msg = Turtle(
                x=turtle["x"],
                y=turtle["y"],
                name=turtle["name"]
            )
            array_msg.turtles.append(turtle_msg)

        self.alive_publisher.publish(array_msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawner()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
