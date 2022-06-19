# PointOneNav Atlas ROS2 Driver

FusionEngine delivers 10cm location accuracy in any environment using its proprietary sensor fusion algorithm.

### Getting Started

##### Install driver dependencies:
```
$ git clone --recurse-submodules https://github.com/airacingtech/ros2-atlas-driver
$ sudo apt update
$ sudo rosdep update
$ rosdep install -y --ignore-src --from-paths src/
```

##### Run Atlas node
```
$ source /opt/ros/galactic/setup.bash
$ colcon build
$ source install/local_setup.bash
$ ros2 run atlas_driver atlas_driver_node_exe
```
