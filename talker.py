import sys
import time
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

class Talker(Node):

    def __init__(self):
        super().__init__("talker")
        self.left_wheel = self.create_publisher(Int32, "/rp2/left/speed", 10)
        self.right_wheel = self.create_publisher(Int32, "/rp2/right/speed", 10)

        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        lw_msg = Int32()
        lw_msg.data = self.ls
        self.left_wheel.publish(lw_msg)
        
        rw_msg = Int32()
        rw_msg.data = self.rs
        self.right_wheel.publish(rw_msg)
        
        self.get_logger().info(f"Left wheel: {lw_msg.data}")
        self.get_logger().info(f"Right wheel: {rw_msg.data}")

    
    def set_speed(self, ls=0, rs=0):
        self.ls = ls
        self.rs = rs
        rclpy.spin_once(self)
        
    def move_straight(self, speed, delay):
        self.set_speed(speed, speed)
        time.sleep(delay)
        self.set_speed()
        
    def turn_left(self, speed, delay):
        self.set_speed(speed, 0)
        time.sleep(delay)
        self.set_speed()

        
    def turn_right(self, speed, delay):
        self.set_speed(0, speed)
        time.sleep(delay)
        self.set_speed()


    
def main():
    rclpy.init()

    publisher = Talker()
    #publisher.set_speed()
    publisher.move_straight(30, 1)
    publisher.turn_right(20, 4)
    publisher.move_straight(30, 1)
    publisher.turn_right(20, 4)
    publisher.move_straight(30, 1)
    publisher.turn_right(20, 4)
    publisher.move_straight(30, 1)
    
    # Terminate node
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
