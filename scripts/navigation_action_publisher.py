#! /usr/bin/python3

import rclpy
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult # Helper module
from tf_transformations import quaternion_from_euler
from geometry_msgs.msg import PoseStamped
import time


point1=(-6.59, -2.98, -0.7853981634)
point2=( 4.02,  0.89,  2.3561944900)

class wp_pub(BasicNavigator):
    def __init__(self):
        super().__init__('robotspace_nav_act_publisher')
    
    def goto_goal(self, goal):
        g = PoseStamped()
        g.header.frame_id = 'map'
        g.header.stamp = self.get_clock().now().to_msg()
        g.pose.position.x = goal[0]
        g.pose.position.y = goal[1]
        q=quaternion_from_euler(0,0,goal[2])
        g.pose.orientation.x=q[0]
        g.pose.orientation.y=q[1]
        g.pose.orientation.z=q[2]
        g.pose.orientation.w=q[3]
        self.goToPose(g)
        
        i=0
        while not self.isTaskComplete():
            i += 1
            feedback = self.getFeedback()
            if feedback and i % 5 == 0:
                self.get_logger().info('Dist remaining: ' + '{:.2f}'.format(feedback.distance_remaining) + ' m')
                self.get_logger().info('nav time: ' + str(feedback.navigation_time.sec)+' s')       

        res = self.getResult()
        if res == TaskResult.SUCCEEDED:
            self.get_logger().info('Goal succeeded!')
        elif res == TaskResult.CANCELED:
            self.get_logger().info('Goal was canceled!')
        elif res == TaskResult.FAILED:
            self.get_logger().info('Goal failed!')
        else:
            self.get_logger().info('Goal has an invalid return status!')
            

            
if __name__ == '__main__':
    rclpy.init()
    try:
        pub=wp_pub()
        pub.goto_goal(point1)
        pub.get_logger().info('Commencing 2nd goal in 3 seconds') 
        time.sleep(3)
        pub.goto_goal(point2)
    except KeyboardInterrupt:
        pub.destroy_node()

