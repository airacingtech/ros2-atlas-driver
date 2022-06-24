from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os

def generate_launch_description():

    bringup_dir = get_package_share_directory('atlas_driver')

    param_file_path = os.path.join(
        bringup_dir,
        'param',
        'atlas_back.param.yaml'
    )
    
    atlas_node = Node(
        package='atlas_driver',
        executable='atlas_driver_node_exe',
        name="atlas_back_node",
        output='screen',
        parameters=[
            param_file_path
        ],
        remappings={
            'fix':'/gps_back/fix',
            'gps_fix': '/gps_back/gps',
            'imu': '/gps_back/imu',
            'pose': '/gps_back/pose'
        }.items()
    )

    ld = LaunchDescription()
    ld.add_action(atlas_node)

    return ld