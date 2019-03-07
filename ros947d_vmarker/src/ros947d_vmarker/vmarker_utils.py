# -*- encoding: utf-8 -*-

import rospy
from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3
from visualization_msgs.msg import Marker, MarkerArray

## @brief create visualization_msgs/Marker with initialized members
## @param header std_msgs/Header
## @param ns namespace
## @param id ID
## @param type Type
## @param action Action (default: Marker.ADD)
## @param pose geometry_msgs/Pose (default: (0,0,0), (0,0,0,1))
## @param scale geometry_msgs/Vector3 (default: (1,1,1))
## @param color std_msgs/ColorRGBA (default: (1,1,1,1))
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
