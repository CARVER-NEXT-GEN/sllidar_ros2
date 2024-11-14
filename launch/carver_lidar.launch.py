#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    channel_type = LaunchConfiguration('channel_type', default='serial')
    serial_port1 = LaunchConfiguration('serial_port1', default='/dev/ttyUSB0')
    serial_port2 = LaunchConfiguration('serial_port2', default='/dev/ttyUSB1')
    serial_baudrate = LaunchConfiguration('serial_baudrate', default='460800')
    frame_id1 = LaunchConfiguration('frame_id1', default='laser1')
    frame_id2 = LaunchConfiguration('frame_id2', default='laser2')
    inverted = LaunchConfiguration('inverted', default='false')
    angle_compensate = LaunchConfiguration('angle_compensate', default='true')
    scan_mode = LaunchConfiguration('scan_mode', default='Standard')

    return LaunchDescription([
        DeclareLaunchArgument(
            'channel_type',
            default_value=channel_type,
            description='Specifying channel type of lidar'),

        DeclareLaunchArgument(
            'serial_port1',
            default_value=serial_port1,
            description='Specifying usb port for first lidar'),

        DeclareLaunchArgument(
            'serial_port2',
            default_value=serial_port2,
            description='Specifying usb port for second lidar'),

        DeclareLaunchArgument(
            'serial_baudrate',
            default_value=serial_baudrate,
            description='Specifying usb port baudrate for connected lidars'),
        
        DeclareLaunchArgument(
            'frame_id1',
            default_value=frame_id1,
            description='Specifying frame_id of first lidar'),

        DeclareLaunchArgument(
            'frame_id2',
            default_value=frame_id2,
            description='Specifying frame_id of second lidar'),

        DeclareLaunchArgument(
            'inverted',
            default_value=inverted,
            description='Specifying whether or not to invert scan data'),

        DeclareLaunchArgument(
            'angle_compensate',
            default_value=angle_compensate,
            description='Specifying whether or not to enable angle_compensate of scan data'),

        DeclareLaunchArgument(
            'scan_mode',
            default_value=scan_mode,
            description='Specifying scan mode of lidar'),

        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='sllidar_node_1',
            parameters=[{'channel_type': channel_type,
                         'serial_port': serial_port1, 
                         'serial_baudrate': serial_baudrate, 
                         'frame_id': frame_id1,
                         'inverted': inverted, 
                         'angle_compensate': angle_compensate, 
                         'scan_mode': scan_mode}],
            remappings=[('/scan', '/lidar_1/scan')],
            output='screen'),

        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='sllidar_node_2',
            parameters=[{'channel_type': channel_type,
                         'serial_port': serial_port2, 
                         'serial_baudrate': serial_baudrate, 
                         'frame_id': frame_id2,
                         'inverted': inverted, 
                         'angle_compensate': angle_compensate, 
                         'scan_mode': scan_mode}],
            remappings=[('/scan', '/lidar_2/scan')],
            output='screen'),
    ])