## Requirements
Create a workspace:

    $ mkdir -p catkin_ws/src
    
    $ cd catkin_ws
    
    $ catkin_make
    
    $ cd src
    
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

    $ export TURTLEBOT3_MODEL=waffle
    
    $ roslaunch messibot empty_world.launch
    
