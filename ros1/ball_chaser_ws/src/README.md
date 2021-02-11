## **White ball chaser**
---
### **Summary**
> The project is to create a differential drive bot which can identify a white ball and move towards it.
> The workspace contains two packages
	1. my_robot : Contains a differential drive bot with lidar and rgb camera attached.
	2. ball_chaser : Holds the scripts for chasing the white ball
---
### **Folder Contents**
1. my_robot
| Folder      | Contents                                                |
| ----------- | ------------------------------------------------------- |
|   launch    | world.launch and utility.launch(for movement testing)   |
|   scripts   | Scripts to test the motions                             |
|   sdf       | sun,room,ground_plane,ball sdf models and my_world.world|
|   urdf      | my_robot.urdf                                           |
|   meshes    | stl files for the robo material                         |

2. ball_chaser
| Folder      | Contents                                                |
| ----------- | ------------------------------------------------------- |
|   launch    | ball_chaser.launch (to launch chasing algo)             |
|   scripts   | drive_bot.py and process_image.py                       |
|   srv       | goto.srv(to pass angle and get a response)              |

---
### **Building**
1. Clone the project go to workspace and run catkin_make
### **Running**
1. Source the project by going to src of the workspace and running *source devel/setup.bash*
2. In current terminal run *roslaunch my_robot world.launch*, to launch the world in gazebo
3. Open a new terminal run *roslaunch ball_chaser ball_chaser.launch*, to run the chasing system
4. Have fun making the robot move around

