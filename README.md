## Requirements
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
    
    $ cd messibot
    
    $ git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
    
    $ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
    
    $ git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git

Rebuild Packages:

    $ cd ../..
    
    $ catkin_make

Add the workspace to your ROS environment:

    $ . ~/catkin_ws/devel/setup.bash
    
## Usage
Launch turtlebot in an empty world with:
    
    $ roslaunch messibot field.launch
    
