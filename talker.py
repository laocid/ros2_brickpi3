import sys
import time
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

class Talker(Node):

    def __init__(self):
        super().__init__("talker")
        self.speed = 0
        self.left_wheel = self.create_publisher(Int32, "/rp2/left/speed", 10)
        self.right_wheel = self.create_publisher(Int32, "/rp2/right/speed", 10)

        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int32()
        msg.data = self.speed
        self.left_wheel.publish(msg)
        self.right_wheel.publish(msg)
        self.i += 1
        self.get_logger().info(f"Publishing: {msg.data}")
    
    def set_speed(self, speed):
        self.speed = speed
        rclpy.spin_once(self)

    
def main():
    rclpy.init()

    publisher = Talker()
    
    # Move forward
    publisher.set_speed(20)
    time.sleep(5)
    
    # Stop movement
    publisher.set_speed(0)
    
    # Reverse movement
    publisher.set_speed(-20)
    
    # Stop movement
    publisher.set_speed(0)

    
    # Terminate node
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
