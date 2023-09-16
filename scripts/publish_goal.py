#! /usr/bin/python3

import rclpy
from rclpy.node import Node
from math import sin, cos, pi
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
import time

point1=(-6.59, -2.98,  0)
point2=( 4.02,  0.89,  2.3561944900)

class goal_pub(Node):
    def __init__(self):
        super().__init__('robotspace_goal_publisher')
        
        self.goal_pub=self.create_publisher(PoseStamped, '/goal_pose', 10)
    
    def send_goal(self, goal_point):
        q=quaternion_from_euler(0,0,goal_point[2])
        goal=PoseStamped()
        goal.header.stamp=self.get_clock().now().to_msg()
        goal.header.frame_id='map'
        goal.pose.position.x=goal_point[0]
        goal.pose.position.y=goal_point[1]
        # goal.pose.orientation.x=q[0]
        # goal.pose.orientation.y=q[1]
        goal.pose.orientation.z=q[2]
        goal.pose.orientation.w=q[3]
        
        #QoS issue: publish is not guarenteed
        self.goal_pub.publish(goal)
        time.sleep(1)
        self.goal_pub.publish(goal)
        time.sleep(1)
        self.goal_pub.publish(goal)
        time.sleep(1)
        self.goal_pub.publish(goal)
        time.sleep(1)

                
if __name__ == '__main__':
    rclpy.init()
    try:
        publisher=goal_pub()
        publisher.get_logger().info('publishing goal...')
        publisher.send_goal(point1)
        # rclpy.spin(publisher)
    except KeyboardInterrupt:
        publisher.destroy_node()

    
    