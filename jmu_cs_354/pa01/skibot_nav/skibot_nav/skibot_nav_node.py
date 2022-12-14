import math

import rclpy
import rclpy.node

from skibot_interfaces.msg import Pose
from skibot_nav_interfaces.srv import SkibotToPoint
from geometry_msgs.msg import Point
from geometry_msgs.msg import Wrench
from geometry_msgs.msg import Vector3

from .pid import PID


class SkibotNavNode(rclpy.node.Node):
    def __init__(self):
        super().__init__("skibot_nav_node")
        self.create_subscription(Point, "target_point", self.target_callback, 10)
        self.thrust_pub = self.create_publisher(Wrench, "thrust", 10)
        # hardcode initial target
        self.target = Point()
        self.target.x = 3.0
        self.target.y = 3.0

        self.target_pub = self.create_publisher(Point, "target_point", 10)
        self.target_pub.publish(self.target)

        self.at_target = False

        p_gain = 1.0
        i_gain = 0
        d_gain = 0.5
        self.pid_x = PID(p_gain, i_gain, d_gain)
        self.pid_y = PID(p_gain, i_gain, d_gain)
        self.pid_theta = PID(p_gain, i_gain, d_gain)

        self.pid_x.reset()
        self.pid_y.reset()
        self.pid_theta.reset()

        self.create_subscription(Pose, "pose", self.pose_callback, 10)
        
        # add service server
        self.nav_srv = self.create_service(SkibotToPoint, "move_skibot_to_point", self.move_service_callback)

    def move_service_callback(self, request, response):
        if (request.goal_x < 0.0 or request.goal_x > 4.0) or (request.goal_y < 0.0 or request.goal_y > 4.0):
            response.success = False
            return response
        else:
            new_target = Point()
            new_target.x = request.goal_x
            new_target.y = request.goal_y
            self.target = new_target
            self.target_pub.publish(self.target)

            # # wait for goal to be reached
            # while not self.at_target:
            #     continue

            response.success = True
            return response

    def pose_callback(self, msg):
        # test something!
        # get the angle right
        sample_force = Vector3()
        sample_torque = Vector3()
        
        # the skibot code made the error of calling angular momentum torque...
        theta_target = math.atan2(self.target.y - msg.y, self.target.x - msg.x)
        error_theta = min(
            theta_target - msg.theta,
            msg.theta - theta_target
        )
        self.get_logger().info(f"Skibot theta: {msg.theta}, target theta: {theta_target}")
        EPSILON = 0.1
        if abs(error_theta) > EPSILON:
            # cmd_ctrl_theta = self.pid_theta.update_PID(error_theta)
            if abs(msg.theta_velocity) <= 0.25:
                sample_torque.z = error_theta
        else:
            print("move forward!")
            error_x = self.target.x - msg.x
            cmd_ctrl_x = self.pid_x.update_PID(error_x)

            error_y = self.target.y - msg.y
            cmd_ctrl_y = self.pid_y.update_PID(error_y)

            if abs(msg.x_velocity) <= 2.0:
                sample_force.x = cmd_ctrl_x
            if abs(msg.y_velocity) <= 2.0:
                sample_force.y = cmd_ctrl_y

        sample_wrench = Wrench()
        sample_wrench.force = sample_force
        sample_wrench.torque = sample_torque
        self.thrust_pub.publish(sample_wrench)
        # self.get_logger().info(f"Command for thrust-- x: {cmd_ctrl_x}  y: {cmd_ctrl_y}  theta: {cmd_ctrl_theta}")
        self.get_logger().info(f"Skibot location-- x: {msg.x}  y: {msg.y}")

        distance_from_target = math.sqrt((msg.x - self.target.x) ** 2 + (msg.y - self.target.y) ** 2)
        if distance_from_target <= 0.01 and msg.x_velocity < 0.01 and msg.y_velocity < 0.01:
            self.at_target = True
        else:
            self.at_target = False

    def target_callback(self, msg):
        self.target = msg


def main():
    rclpy.init()
    nav_node = SkibotNavNode()
    rclpy.spin(nav_node)

    nav_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
