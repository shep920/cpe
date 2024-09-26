#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Relay(Node):
    def __init__(self):
        super().__init__('relay')

        # Subscriber to the drive topic
        self.subscription = self.create_subscription(
            AckermannDriveStamped,
            'drive',
            self.listener_callback,
            10
        )

        # Publisher to the drive_relay topic
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive_relay', 10)

    def listener_callback(self, msg):
        # Multiply speed and steering_angle by 3
        new_msg = AckermannDriveStamped()
        new_msg.drive.speed = msg.drive.speed * 3
        new_msg.drive.steering_angle = msg.drive.steering_angle * 3

        # Publish to drive_relay
        self.publisher_.publish(new_msg)
        self.get_logger().info(f'Relayed: speed={new_msg.drive.speed}, steering_angle={new_msg.drive.steering_angle}')

def main(args=None):
    rclpy.init(args=args)
    node = Relay()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
