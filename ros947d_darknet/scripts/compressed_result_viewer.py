#!/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
from darknet_ros_msgs.msg import BoundingBox, BoundingBoxes

class ResultViewer:
  def __init__(self):
    self.bbs = BoundingBoxes()
    self.bridge = CvBridge()

    self.sub_bb = rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes, self.bb_callback)
    self.sub_image = rospy.Subscriber('image', CompressedImage, self.image_callback)

  def image_callback(self, msg):
    np_arr = np.fromstring(msg.data, np.uint8)
    cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    for bb in self.bbs.bounding_boxes:
      cv2.rectangle(cv_image, (bb.xmin, bb.ymin), (bb.xmax, bb.ymax), (0, 0, 255), 2)
      cv2.putText(cv_image, bb.Class, (bb.xmin, bb.ymax), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))

    cv2.imshow('Recognition Result', cv_image)
    cv2.waitKey(1)

  def bb_callback(self, msg):
    self.bbs = msg

def main():
  rospy.init_node('result_viewer')
  rv = ResultViewer()
  rospy.spin()

if __name__ == '__main__':
  main()
