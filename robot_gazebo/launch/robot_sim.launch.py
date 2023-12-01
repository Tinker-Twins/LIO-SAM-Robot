#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    world_file_name = 'lio_world.model'
    world = os.path.join(get_package_share_directory('robot_gazebo'),'worlds', world_file_name)
    launch_file_dir = os.path.join(get_package_share_directory('robot_gazebo'), 'launch')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_cart_pole_control = get_package_share_directory('robot_control')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
            ),
            launch_arguments={'world': world}.items(),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
            ),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([launch_file_dir, '/robot_state_publisher.launch.py']),
            launch_arguments={'use_sim_time': use_sim_time}.items(),
        ),

        # USE JOYSTICK TELEOP
        
        # Node(
        # package = "joy",
        # executable = "joy_node"
        # ),
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(
        #         os.path.join(pkg_cart_pole_control, 'launch', 'robot_control.launch.py')
        #     ),
        # ),
    ])
