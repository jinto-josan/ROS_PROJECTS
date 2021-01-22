export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:$(pwd)/build
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:$(pwd)/model
#ros2 launch gazebo_launch.py 
gzserver world/my_world.world --verbose
