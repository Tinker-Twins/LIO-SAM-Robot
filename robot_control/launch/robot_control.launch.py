from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='robot_control',
             executable='robot_control.py',
             output='screen'),
    ])