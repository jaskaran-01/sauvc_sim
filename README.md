# Gazebo SAUVC environent

SAUVC environment with ROS2 humble

## Getting started
Install Humble from source :

[ROS HUMBLE SOURCE INSTALL](https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html)


Build the code:

```
colcon build --symlink-install
. install/setup.sh
```

source everything:
```
source /opt/ros/humble/setup.bash
source ~/ros2_humble/install/setup.bash
source ~/sauvc_sim/install/setup.bash
```


Launch the environment

```sh
ros2 launch sauvc_sim sauvc_launch.py
```

Topics:

```sh
# ros2 topic list
/sauvc_sim/bottom_camera/camera_info
/sauvc_sim/bottom_camera/image_raw
/sauvc_sim/front_camera/camera_info
/sauvc_sim/front_camera/depth/camera_info
/sauvc_sim/front_camera/depth/image_raw
/sauvc_sim/front_camera/image_raw
/sauvc_sim/front_camera/points
/sauvc_sim/link_states
/sauvc_sim/model_states
```

Keyboard control:

```
ros2 run sauvc_sim teleop.py
```


#PS: 
if gazebo has odd errors try sourcing gazebo thats worked for me 
```
source /usr/share/gazebo/setup.sh
```
