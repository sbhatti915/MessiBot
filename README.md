## Requirements
Create a workspace:

    $ mkdir -p catkin_ws/src
    
    $ cd catkin_ws
    
    $ catkin_make
    
    $ cd src
    
Add all Repositories:

    $ git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
    
    $ git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
    
    $ git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
    
    $ git clone

Download the necessary apriltag meshes:

    $ git clone https://github.com/sharif1093/apriltag_gazebo_model_generator.git

    $ cd ~/apriltag_gazebo_model_generator/ar_tags/scripts

    $ ./generate_markers_model.py -i ../36h11_sample -s 200 -w 50


Re-build the packages to configure the workspace:

`$ catkin_make`

Add the workspace to your ROS environment:

`$ . ~/guide/devel/setup.bash`
