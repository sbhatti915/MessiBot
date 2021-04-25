## Notes
*Odometry is not very accurate

## Requirements
Ubuntu 18.04
ROS Melodic

Create a workspace:

    $ mkdir -p catkin_ws/src
    
    $ cd catkin_ws
    
    $ catkin_make
    
    $ cd src

Add Dependencies:

   tf2
    
    $ sudo apt-get install ros-melodic-tf2-sensor-msgs
   
Add all Repositories:

    $ git clone https://github.com/sbhatti915/messibot.git

Rebuild Packages:

    $ cd ../..
    
    $ catkin_make

Add the workspace to your ROS environment:

    $ . ~/catkin_ws/devel/setup.bash
    
## Usage
Launch messibot in the field with:
    
    $ roslaunch messibot field.launch
    
Add AMCL:

    $ roslaunch navigation_params navigation.launch
    
