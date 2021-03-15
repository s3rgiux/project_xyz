# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from control_xy/TriggerAction.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TriggerAction(genpy.Message):
  _md5sum = "529f37831afe7067075cb584db0e391e"
  _type = "control_xy/TriggerAction"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# 非常停止ボタン解除
string TRIGGER_EMERGENCY_BUTTON_OFF = emergency_button_off
# 非常停止ボタン押下
string TRIGGER_EMERGENCY_BUTTON_ON = emergency_button_on
# カルガモボタン押下
string TRIGGER_KARUGAMO_BUTTON_ON = karugamo_button_on
# リモコン:カルガモボタン押下
string TRIGGER_REMOTE_KARUGAMO_BUTTON_ON = remote_karuamo_button_on
# リモコン:マニュアルボタン押下
string TRIGGER_REMOTE_MANUAL_BUTTON_ON = remote_manual_button_on
# リモコン:アイドルボタン押下
string TRIGGER_REMOTE_IDLE_BUTTON_ON = remote_idle_button_on
# アイドルボタン押下
string TRIGGER_IDLE_BUTTON_ON = idle_button_on
# 進行方向 2000 mm 以内に障害物を発見
string TRIGGER_DETECT_OBSTACLE = detect_obstacle
# 前方近傍に障害物を発見（LIDAR進行方向 500 mm以内）
string TRIGGER_DETECT_DANGER_OBSTACLE = detect_danger_obstacle
# ガードバンパー接触
string TRIGGER_COLLISION = collision
# ブレーキ解除ボタン押下
string TRIGGER_BREAK_RELEASE_BUTTON_ON = break_release_button_on
# 対象ロストから10秒経過
string TRIGGER_LONG_LOST = long_lost

string trigger
"""
  # Pseudo-constants
  TRIGGER_EMERGENCY_BUTTON_OFF = 'emergency_button_off'
  TRIGGER_EMERGENCY_BUTTON_ON = 'emergency_button_on'
  TRIGGER_KARUGAMO_BUTTON_ON = 'karugamo_button_on'
  TRIGGER_REMOTE_KARUGAMO_BUTTON_ON = 'remote_karuamo_button_on'
  TRIGGER_REMOTE_MANUAL_BUTTON_ON = 'remote_manual_button_on'
  TRIGGER_REMOTE_IDLE_BUTTON_ON = 'remote_idle_button_on'
  TRIGGER_IDLE_BUTTON_ON = 'idle_button_on'
  TRIGGER_DETECT_OBSTACLE = 'detect_obstacle'
  TRIGGER_DETECT_DANGER_OBSTACLE = 'detect_danger_obstacle'
  TRIGGER_COLLISION = 'collision'
  TRIGGER_BREAK_RELEASE_BUTTON_ON = 'break_release_button_on'
  TRIGGER_LONG_LOST = 'long_lost'

  __slots__ = ['trigger']
  _slot_types = ['string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       trigger

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TriggerAction, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.trigger is None:
        self.trigger = ''
    else:
      self.trigger = ''

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
      _x = self.trigger
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.trigger = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.trigger = str[start:end]
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
      _x = self.trigger
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
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
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.trigger = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.trigger = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
