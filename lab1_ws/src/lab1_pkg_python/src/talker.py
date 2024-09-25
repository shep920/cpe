import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        # Declare and get parameters
        self.declare_parameter('v', 1.0)
        self.declare_parameter('d', 0.0)
        self.speed = self.get_parameter('v').value
        self.steering_angle = self.get_parameter('d').value
        
        # Create publisher
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 10)
        self.timer = self.create_timer(0.1, self.publish_drive_message)  # Publish as fast as possible

    def publish_drive_message(self):
        msg = AckermannDriveStamped()
        msg.drive.speed = self.speed
        msg.drive.steering_angle = self.steering_angle
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: speed={self.speed}, steering_angle={self.steering_angle}')

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()