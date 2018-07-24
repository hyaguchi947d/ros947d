#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import rospy

from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3
from visualization_msgs.msg import Marker, MarkerArray

from ros947d_vmarker import create_marker

def main():
  rospy.init_node('vmarker_publisher_node', anonymous=True)
  pub = rospy.Publisher('vmarker', MarkerArray)
  rate = rospy.Rate(10)

  while not rospy.is_shutdown():
    markers = MarkerArray()
    tm = rospy.Time.now()
    marker = create_marker(
      header = Header(stamp = tm, frame_id = 'map'),
      ns = 'vmarker',
      id = 0,
      type = Marker.CUBE,
    )
    markers.markers.append(marker)
    pub.publish(markers)
    rate.sleep()

if __name__ == '__main__':
  main()