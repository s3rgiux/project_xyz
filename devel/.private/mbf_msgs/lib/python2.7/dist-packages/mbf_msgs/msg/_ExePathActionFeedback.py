# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mbf_msgs/ExePathActionFeedback.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import actionlib_msgs.msg
import genpy
import geometry_msgs.msg
import mbf_msgs.msg
import std_msgs.msg

class ExePathActionFeedback(genpy.Message):
  _md5sum = "41e5119fe263f5296a0eba2eff692cd2"
  _type = "mbf_msgs/ExePathActionFeedback"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalStatus status
ExePathFeedback feedback

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: actionlib_msgs/GoalStatus
GoalID goal_id
uint8 status
uint8 PENDING         = 0   # The goal has yet to be processed by the action server
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing
                            #   and has since completed its execution (Terminal State)
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due
                            #    to some failure (Terminal State)
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,
                            #    because the goal was unattainable or invalid (Terminal State)
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing
                            #    and has not yet completed execution
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,
                            #    but the action server has not yet confirmed that the goal is canceled
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing
                            #    and was successfully cancelled (Terminal State)
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be
                            #    sent over the wire by an action server

#Allow for the user to associate a string with GoalStatus for debugging
string text


================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: mbf_msgs/ExePathFeedback
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

# Outcome of most recent controller cycle. Same values as in result
uint32 outcome
string message

float32 dist_to_goal
float32 angle_to_goal
geometry_msgs/PoseStamped  current_pose
geometry_msgs/TwistStamped last_cmd_vel  # last command calculated by the controller


================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/TwistStamped
# A twist with reference coordinate frame and timestamp
Header header
Twist twist

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['header','status','feedback']
  _slot_types = ['std_msgs/Header','actionlib_msgs/GoalStatus','mbf_msgs/ExePathFeedback']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,status,feedback

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ExePathActionFeedback, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.feedback is None:
        self.feedback = mbf_msgs.msg.ExePathFeedback()
    else:
      self.header = std_msgs.msg.Header()
      self.status = actionlib_msgs.msg.GoalStatus()
      self.feedback = mbf_msgs.msg.ExePathFeedback()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs))
      _x = self.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.status.status
      buff.write(_get_struct_B().pack(_x))
      _x = self.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.feedback.outcome
      buff.write(_get_struct_I().pack(_x))
      _x = self.feedback.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2f3I().pack(_x.feedback.dist_to_goal, _x.feedback.angle_to_goal, _x.feedback.current_pose.header.seq, _x.feedback.current_pose.header.stamp.secs, _x.feedback.current_pose.header.stamp.nsecs))
      _x = self.feedback.current_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.feedback.current_pose.pose.position.x, _x.feedback.current_pose.pose.position.y, _x.feedback.current_pose.pose.position.z, _x.feedback.current_pose.pose.orientation.x, _x.feedback.current_pose.pose.orientation.y, _x.feedback.current_pose.pose.orientation.z, _x.feedback.current_pose.pose.orientation.w, _x.feedback.last_cmd_vel.header.seq, _x.feedback.last_cmd_vel.header.stamp.secs, _x.feedback.last_cmd_vel.header.stamp.nsecs))
      _x = self.feedback.last_cmd_vel.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_6d().pack(_x.feedback.last_cmd_vel.twist.linear.x, _x.feedback.last_cmd_vel.twist.linear.y, _x.feedback.last_cmd_vel.twist.linear.z, _x.feedback.last_cmd_vel.twist.angular.x, _x.feedback.last_cmd_vel.twist.angular.y, _x.feedback.last_cmd_vel.twist.angular.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.feedback is None:
        self.feedback = mbf_msgs.msg.ExePathFeedback()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.status.status,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.text = str[start:end].decode('utf-8')
      else:
        self.status.text = str[start:end]
      start = end
      end += 4
      (self.feedback.outcome,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.message = str[start:end].decode('utf-8')
      else:
        self.feedback.message = str[start:end]
      _x = self
      start = end
      end += 20
      (_x.feedback.dist_to_goal, _x.feedback.angle_to_goal, _x.feedback.current_pose.header.seq, _x.feedback.current_pose.header.stamp.secs, _x.feedback.current_pose.header.stamp.nsecs,) = _get_struct_2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.current_pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.feedback.current_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.feedback.current_pose.pose.position.x, _x.feedback.current_pose.pose.position.y, _x.feedback.current_pose.pose.position.z, _x.feedback.current_pose.pose.orientation.x, _x.feedback.current_pose.pose.orientation.y, _x.feedback.current_pose.pose.orientation.z, _x.feedback.current_pose.pose.orientation.w, _x.feedback.last_cmd_vel.header.seq, _x.feedback.last_cmd_vel.header.stamp.secs, _x.feedback.last_cmd_vel.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.last_cmd_vel.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.feedback.last_cmd_vel.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.feedback.last_cmd_vel.twist.linear.x, _x.feedback.last_cmd_vel.twist.linear.y, _x.feedback.last_cmd_vel.twist.linear.z, _x.feedback.last_cmd_vel.twist.angular.x, _x.feedback.last_cmd_vel.twist.angular.y, _x.feedback.last_cmd_vel.twist.angular.z,) = _get_struct_6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs))
      _x = self.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.status.status
      buff.write(_get_struct_B().pack(_x))
      _x = self.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.feedback.outcome
      buff.write(_get_struct_I().pack(_x))
      _x = self.feedback.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2f3I().pack(_x.feedback.dist_to_goal, _x.feedback.angle_to_goal, _x.feedback.current_pose.header.seq, _x.feedback.current_pose.header.stamp.secs, _x.feedback.current_pose.header.stamp.nsecs))
      _x = self.feedback.current_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.feedback.current_pose.pose.position.x, _x.feedback.current_pose.pose.position.y, _x.feedback.current_pose.pose.position.z, _x.feedback.current_pose.pose.orientation.x, _x.feedback.current_pose.pose.orientation.y, _x.feedback.current_pose.pose.orientation.z, _x.feedback.current_pose.pose.orientation.w, _x.feedback.last_cmd_vel.header.seq, _x.feedback.last_cmd_vel.header.stamp.secs, _x.feedback.last_cmd_vel.header.stamp.nsecs))
      _x = self.feedback.last_cmd_vel.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_6d().pack(_x.feedback.last_cmd_vel.twist.linear.x, _x.feedback.last_cmd_vel.twist.linear.y, _x.feedback.last_cmd_vel.twist.linear.z, _x.feedback.last_cmd_vel.twist.angular.x, _x.feedback.last_cmd_vel.twist.angular.y, _x.feedback.last_cmd_vel.twist.angular.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.feedback is None:
        self.feedback = mbf_msgs.msg.ExePathFeedback()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.status.status,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.text = str[start:end].decode('utf-8')
      else:
        self.status.text = str[start:end]
      start = end
      end += 4
      (self.feedback.outcome,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.message = str[start:end].decode('utf-8')
      else:
        self.feedback.message = str[start:end]
      _x = self
      start = end
      end += 20
      (_x.feedback.dist_to_goal, _x.feedback.angle_to_goal, _x.feedback.current_pose.header.seq, _x.feedback.current_pose.header.stamp.secs, _x.feedback.current_pose.header.stamp.nsecs,) = _get_struct_2f3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.current_pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.feedback.current_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.feedback.current_pose.pose.position.x, _x.feedback.current_pose.pose.position.y, _x.feedback.current_pose.pose.position.z, _x.feedback.current_pose.pose.orientation.x, _x.feedback.current_pose.pose.orientation.y, _x.feedback.current_pose.pose.orientation.z, _x.feedback.current_pose.pose.orientation.w, _x.feedback.last_cmd_vel.header.seq, _x.feedback.last_cmd_vel.header.stamp.secs, _x.feedback.last_cmd_vel.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.last_cmd_vel.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.feedback.last_cmd_vel.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.feedback.last_cmd_vel.twist.linear.x, _x.feedback.last_cmd_vel.twist.linear.y, _x.feedback.last_cmd_vel.twist.linear.z, _x.feedback.last_cmd_vel.twist.angular.x, _x.feedback.last_cmd_vel.twist.angular.y, _x.feedback.last_cmd_vel.twist.angular.z,) = _get_struct_6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_2f3I = None
def _get_struct_2f3I():
    global _struct_2f3I
    if _struct_2f3I is None:
        _struct_2f3I = struct.Struct("<2f3I")
    return _struct_2f3I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_6d = None
def _get_struct_6d():
    global _struct_6d
    if _struct_6d is None:
        _struct_6d = struct.Struct("<6d")
    return _struct_6d
_struct_7d3I = None
def _get_struct_7d3I():
    global _struct_7d3I
    if _struct_7d3I is None:
        _struct_7d3I = struct.Struct("<7d3I")
    return _struct_7d3I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
