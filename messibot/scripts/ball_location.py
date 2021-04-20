#!/usr/bin/env python

import rospy
import numpy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from std_msgs.msg import Float64MultiArray
from darknet_ros_msgs.msg import BoundingBoxes

#ToDo
############################
#subscribers (rgb, depth, cam_info, darknet_bounding_boxes, darknet_object_classifications)
############################
#math operation
############################
#publish object x,y,z info
class ball_finder():
    def __init__(self):

        self.bridge=CvBridge()
        self.depth_sub = rospy.Subscriber("/camera/depth/image_raw",Image, self.depth_callback)
        self.info_sub = rospy.Subscriber("/camera/rgb/camera_info",CameraInfo,self.info_callback)
        self.bb_sub = rospy.Subscriber("darknet_ros/bounding_boxes",BoundingBoxes,self.get_center) #change this mabye?
        self.pub = rospy.Publisher("xyz",Float64MultiArray, queue_size=10)
        self.depth_img=None
        self.caminfo=None
        self.u=None
        self.v=None

    def get_center(self,data):
        self.u = (data.bounding_boxes[0].xmin+data.bounding_boxes[0].xmax)/2
        self.v = (data.bounding_boxes[0].ymin+data.bounding_boxes[0].ymax)/2
        self.mainfunc()

    def get_xyz(self,pt,cx,cy,fx,fy,u,v):

        z=pt
        x=(u-cx)*z/fx
        y=(v-cy)*z/fy
        print(pt)
        return x,y,z

    def depth_callback(self,data):
        self.depth_img = self.bridge.imgmsg_to_cv2(data, "passthrough")
        self.mainfunc()

    def info_callback(self,data):
        self.caminfo = data
        self.mainfunc()
        

    def mainfunc(self):
        if self.depth_img is not None and self.caminfo is not None and self.u is not None:

            [x,y,z] = self.get_xyz(self.depth_img[self.v][self.u],self.caminfo.K[2],self.caminfo.K[5],self.caminfo.K[0],self.caminfo.K[4],self.u,self.v)
            output=Float64MultiArray()
            output.data=[x,y,z]
            self.pub.publish(output)
            self.u=None
            self.v=None

if __name__ == '__main__':

    rospy.init_node('ball_location', anonymous=True)
    ballfind = ball_finder()
    ballfind.mainfunc()
    rospy.spin()
