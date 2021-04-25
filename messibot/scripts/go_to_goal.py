#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from math import pow, atan2, sqrt
from tf.transformations import euler_from_quaternion


class messibot:

    def __init__(self):

        # Creates a node with name 'messibot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('messibot_controller', anonymous=True)

        # Publisher which will publish to the topic '/four_wheel_steering_controller/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/four_wheel_steering_controller/cmd_vel',
                                                        Twist, queue_size=10)

        # A subscriber to the topic '/four_wheel_steering_controller/odom'. self.update_pose is called
        # when a message of type Odometry is received.
        self.pose_subscriber = rospy.Subscriber('/four_wheel_steering_controller/odom',
                                                        Odometry, self.update_pose)
        
        self.pose = Odometry
        self.rate = rospy.Rate(200)
    
    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.loc = data
        self.loc.pose.pose.position.x = round(self.loc.pose.pose.position.x, 4)
        self.loc.pose.pose.position.y = round(self.loc.pose.pose.position.y, 4)
 
    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.loc.pose.pose.position.x), 2) + pow((goal_pose.y - self.loc.pose.pose.position.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.loc.pose.pose.position.y, goal_pose.x - self.loc.pose.pose.position.x)

    def angular_vel(self, goal_pose, constant=6):

        rot_q = self.loc.pose.pose.orientation
        (roll, pitch, yaw) = euler_from_quaternion([rot_q.x,rot_q.y,rot_q.z,rot_q.w])

        return constant * (self.steering_angle(goal_pose) - yaw)

    def move2goal(self):

        goal_pose = Point()

        # Get the input from the user.
        goal_pose.x = float(input("Set your x goal: "))
        goal_pose.y = float(input("Set your y goal: "))

        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        distance_tolerance = input("Set your tolerance: ")

        vel_msg = Twist()

        while self.euclidean_distance(goal_pose) >= distance_tolerance:

            # Porportional controller.
            # https://en.wikipedia.org/wiki/Proportional_control

            # Linear velocity in the x-axis.
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose)

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        # If we press control + C, the node will stop.
        rospy.spin()
 
if __name__ == '__main__':
    try:
        x = messibot()
        x.move2goal()
    except rospy.ROSInterruptException:
        pass