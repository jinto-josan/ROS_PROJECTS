source ./install/setup.bash
cd launch
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:$(pwd)/prop/models
ros2 launch test_robo_launch.py


