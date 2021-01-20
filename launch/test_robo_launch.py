import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_test_robo = get_package_share_directory('test_robo')

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
        )
    )

    # Follow node
    robo = Node(
        package='test_robo',
        executable='driver',
        output='screen',
        remappings=[
            ('cmd_vel', '/test_robo/cmd_vel'),
        ]
    )
   #print(os.path.join(os.getcwd(),'prop','worlds'))

    return LaunchDescription([
        DeclareLaunchArgument(
          'world',
          default_value=[os.path.join(os.getcwd(),'prop','worlds', 'my_world.world')],
          description='SDF world file'),
        gazebo,
        robo
    ])
