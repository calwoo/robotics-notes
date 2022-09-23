#!/usr/bin/env python
"""
Process scan messages to detect intruders.

Subscribes to: /scan
Publishes to:  /intruder

Author: Nathan Sprague && 
Version: 

"""
import rclpy
import rclpy.node
from rclpy.qos import qos_profile_sensor_data

from geometry_msgs.msg import PointStamped
from sensor_msgs.msg import LaserScan

import numpy as np

class DetectorNode(rclpy.node.Node):

    def __init__(self):
        super().__init__('wander')

        self.prev_scan = None # Stores recently received scan messages.
        self.scan = None 

        self.intruder_pub = self.create_publisher(PointStamped, 'intruder', 10)
        self.create_timer(.1, self.timer_callback)

        self.create_subscription(LaserScan,'scan',
                                 self.scan_callback,
                                 qos_profile_sensor_data)

    def scan_callback(self, scan_msg):
        """Store the LaserScan msg."""
        self.prev_scan = self.scan
        self.scan = scan_msg

    def timer_callback(self):
        """Periodically check for intruders"""
        
        point = PointStamped()
        point.header.frame_id = "base_link"
        # point.point.x = 1.0

        intruder_threshold = 0.1

        if self.prev_scan is not None:
            prev_scan_ranges = np.array(self.prev_scan.ranges)
            scan_ranges = np.array(self.scan.ranges)

            # zero out unbounded ranges
            prev_scan_ranges[np.isinf(prev_scan_ranges)] = 0
            scan_ranges[np.isinf(scan_ranges)] = 0

            range_diffs = np.abs(prev_scan_ranges - scan_ranges)
            intruder_mask = range_diffs >= intruder_threshold
            scan_idx_intruder = np.argmax(intruder_mask)

            angle_intruder = self.scan.angle_min + self.scan.angle_increment * scan_idx_intruder
            distance_intruder = range_diffs[scan_idx_intruder]

            point.point.x = distance_intruder * np.cos(angle_intruder)
            point.point.y = distance_intruder * np.sin(angle_intruder)

        self.intruder_pub.publish(point)

def main():
    rclpy.init()
    detector_node = DetectorNode()
    rclpy.spin(detector_node)

    thruster_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
