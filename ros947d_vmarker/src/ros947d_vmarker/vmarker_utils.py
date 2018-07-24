# -*- encoding: utf-8 -*-

import rospy
from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3
from visualization_msgs.msg import Marker, MarkerArray

def create_marker(
  header, ns, id, type, action = Marker.ADD,
  pose = Pose(Point(0, 0, 0), Quaternion(0, 0, 0, 1)),
  scale = Vector3(1, 1, 1),
  color = ColorRGBA(1, 1, 1, 1)
):
  marker = Marker(
    header = header,
    ns = ns,
    id = id,
    type = type,
    action = action,
    pose = pose,
    scale = scale,
    color = color
  )
  return marker
