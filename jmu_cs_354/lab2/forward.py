import rclpy
import rclpy.node

from geometry_msgs.msg import Twist


class TurtleForward(rclpy.node.Node):
    def __init__(self):
        super().__init__("turtle_forwarder")
        self.speed = 0.2
        self.publisher = self.create_publisher(Twist, "cmd_vel", 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.speed
        self.publisher.publish(msg)
        self.get_logger().info(f"Publishing: {msg}")


def main(args=None):
    rclpy.init(args=args)
    forward_publisher = TurtleForward()

    rclpy.spin(forward_publisher)

    forward_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
