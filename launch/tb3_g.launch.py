#! /usr/bin/python3

import os
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch.actions import IncludeLaunchDescription 
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription


def generate_launch_description():
    
    ld = LaunchDescription()
    
    joy_node = Node(
        name='joy_driver_node',
        package='joy',
        executable='joy_node'
    )
    
    teleop_node = Node(
        name="teleop_twist_joy_node",
        package='teleop_twist_joy',
        executable='teleop_node',
        parameters= [os.path.join(get_package_share_directory("rbtspc_wp_flwr"), 'config', 'joy_params.yaml')],
    )
    
    tb3_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('turtlebot3_gazebo'), 'launch/turtlebot3_house.launch.py'
            ])            
        ]),
    )
    
    ld.add_action(joy_node)
    ld.add_action(teleop_node)
    ld.add_action(tb3_launch)
    
    return ld
    