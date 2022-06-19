# PointOneNav Atlas ROS2 Driver

FusionEngine delivers 10cm location accuracy in any environment using its proprietary sensor fusion algorithm.

### Getting Started

##### Install driver dependencies:
```
$ mkdir -p ~/atlas_ws/src
$ cd ~/atlas_ws/src
$ git clone --recurse-submodules https://github.com/airacingtech/ros2-atlas-driver
$ cd ros2-atlas-driver
$ sudo apt update
$ sudo rosdep update
$ rosdep install -y --ignore-src --from-paths src/
```

##### Run Atlas node

Edit the parameters in `src/atlas_driver/param/atlas_driver.param.yaml`

In `src/atlas_driver/launch/atlas_driver.launch.py` you can change the remappings so that the data gets published in different topics. Otherwise those will be the defaults

```
$ cd ~/atlas_ws
$ source /opt/ros/galactic/setup.bash
$ colcon build
$ source install/local_setup.bash
$ ros2 launch atlas_driver atlas_driver.launch.py
```
