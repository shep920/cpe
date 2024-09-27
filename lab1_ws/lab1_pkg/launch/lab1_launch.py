#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Define the parameters for the talker node
    talker_params = {'v': 2.5, 'd': 1.0}

    # Create the talker node
    talker_node = Node(
        package='lab1_pkg',
        executable='talker.py',
        name='talker',
        output='screen',
        parameters=[talker_params]
    )

    # Create the relay node
    relay_node = Node(
        package='lab1_pkg',
        executable='relay.py',
        name='relay',
        output='screen'
    )

    # Return the LaunchDescription object with both nodes
    return LaunchDescription([
        talker_node,
        relay_node
    ])
