# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from peop_extract/States.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class States(genpy.Message):
  _md5sum = "e365334b2994db104733260f8d214b10"
  _type = "peop_extract/States"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string state
string state_karugamo
string state_collision
string state_danger
string state_costmap
string state_manual
string state_scan
string state_load
string state_shelf
float32 costmap
float32 side_joystick
float32 ctrl_front
float32 ctrl_side
geometry_msgs/Twist trackeds

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
  __slots__ = ['state','state_karugamo','state_collision','state_danger','state_costmap','state_manual','state_scan','state_load','state_shelf','costmap','side_joystick','ctrl_front','ctrl_side','trackeds']
  _slot_types = ['string','string','string','string','string','string','string','string','string','float32','float32','float32','float32','geometry_msgs/Twist']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       state,state_karugamo,state_collision,state_danger,state_costmap,state_manual,state_scan,state_load,state_shelf,costmap,side_joystick,ctrl_front,ctrl_side,trackeds

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(States, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.state is None:
        self.state = ''
      if self.state_karugamo is None:
        self.state_karugamo = ''
      if self.state_collision is None:
        self.state_collision = ''
      if self.state_danger is None:
        self.state_danger = ''
      if self.state_costmap is None:
        self.state_costmap = ''
      if self.state_manual is None:
        self.state_manual = ''
      if self.state_scan is None:
        self.state_scan = ''
      if self.state_load is None:
        self.state_load = ''
      if self.state_shelf is None:
        self.state_shelf = ''
      if self.costmap is None:
        self.costmap = 0.
      if self.side_joystick is None:
        self.side_joystick = 0.
      if self.ctrl_front is None:
        self.ctrl_front = 0.
      if self.ctrl_side is None:
        self.ctrl_side = 0.
      if self.trackeds is None:
        self.trackeds = geometry_msgs.msg.Twist()
    else:
      self.state = ''
      self.state_karugamo = ''
      self.state_collision = ''
      self.state_danger = ''
      self.state_costmap = ''
      self.state_manual = ''
      self.state_scan = ''
      self.state_load = ''
      self.state_shelf = ''
      self.costmap = 0.
      self.side_joystick = 0.
      self.ctrl_front = 0.
      self.ctrl_side = 0.
      self.trackeds = geometry_msgs.msg.Twist()

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
      _x = self.state
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_karugamo
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_collision
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_danger
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_costmap
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_manual
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_scan
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_load
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_shelf
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_4f6d().pack(_x.costmap, _x.side_joystick, _x.ctrl_front, _x.ctrl_side, _x.trackeds.linear.x, _x.trackeds.linear.y, _x.trackeds.linear.z, _x.trackeds.angular.x, _x.trackeds.angular.y, _x.trackeds.angular.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.trackeds is None:
        self.trackeds = geometry_msgs.msg.Twist()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_karugamo = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_karugamo = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_collision = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_collision = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_danger = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_danger = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_costmap = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_costmap = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_manual = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_manual = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_scan = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_scan = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_load = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_load = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_shelf = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_shelf = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.costmap, _x.side_joystick, _x.ctrl_front, _x.ctrl_side, _x.trackeds.linear.x, _x.trackeds.linear.y, _x.trackeds.linear.z, _x.trackeds.angular.x, _x.trackeds.angular.y, _x.trackeds.angular.z,) = _get_struct_4f6d().unpack(str[start:end])
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
      _x = self.state
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_karugamo
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_collision
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_danger
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_costmap
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_manual
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_scan
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_load
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state_shelf
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_4f6d().pack(_x.costmap, _x.side_joystick, _x.ctrl_front, _x.ctrl_side, _x.trackeds.linear.x, _x.trackeds.linear.y, _x.trackeds.linear.z, _x.trackeds.angular.x, _x.trackeds.angular.y, _x.trackeds.angular.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.trackeds is None:
        self.trackeds = geometry_msgs.msg.Twist()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_karugamo = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_karugamo = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_collision = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_collision = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_danger = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_danger = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_costmap = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_costmap = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_manual = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_manual = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_scan = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_scan = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_load = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_load = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_shelf = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state_shelf = str[start:end]
      _x = self
      start = end
      end += 64
      (_x.costmap, _x.side_joystick, _x.ctrl_front, _x.ctrl_side, _x.trackeds.linear.x, _x.trackeds.linear.y, _x.trackeds.linear.z, _x.trackeds.angular.x, _x.trackeds.angular.y, _x.trackeds.angular.z,) = _get_struct_4f6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4f6d = None
def _get_struct_4f6d():
    global _struct_4f6d
    if _struct_4f6d is None:
        _struct_4f6d = struct.Struct("<4f6d")
    return _struct_4f6d
