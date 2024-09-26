#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        # Declare parameters v and d
        self.declare_parameter('v', 0.0)
        self.declare_parameter('d', 0.0)

        # Create publisher for the drive topic
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 10)

        # Timer to publish as fast as possible
        timer_period = 0.01  # seconds (as fast as possible)
        self.timer = self.create_timer(timer_period, self.publish_drive_message)

    def publish_drive_message(self):
        v = self.get_parameter('v').get_parameter_value().double_value
        d = self.get_parameter('d').get_parameter_value().double_value

        msg = AckermannDriveStamped()
        msg.drive.speed = v
        msg.drive.steering_angle = d

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: speed={v}, steering_angle={d}')

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
