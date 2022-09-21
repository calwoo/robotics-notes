import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class TurtleStopper(Node):
    def __init__(self):
        super().__init__("turtle_stopper")
        self.subscription = self.create_subscription(
            LaserScan,
            "scan",
            self.listener_callback,
            qos_profile_sensor_data
        )
        self.publisher = self.create_publisher(Twist, "cmd_vel", 10)

    def listener_callback(self, msg):
        if msg.ranges[0] < 1.0:
            stop_msg = Twist()
            self.publisher.publish(stop_msg)
            self.get_logger().info("Sent a stop message!")


def main(args=None):
    rclpy.init(args=args)
    turtle_stopper = TurtleStopper()

    rclpy.spin(turtle_stopper)

    turtle_stopper.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
