// Auto-generated. Do not edit!

// (in-package pitakuru.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class States {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.state = null;
      this.state_karugamo = null;
      this.state_collision = null;
      this.state_danger = null;
      this.state_costmap = null;
      this.state_manual = null;
      this.state_scan = null;
      this.state_load = null;
      this.state_shelf = null;
      this.state_navigation = null;
      this.costmap = null;
      this.side_joystick = null;
      this.ctrl_front = null;
      this.ctrl_side = null;
      this.trackeds = null;
    }
    else {
      if (initObj.hasOwnProperty('state')) {
        this.state = initObj.state
      }
      else {
        this.state = '';
      }
      if (initObj.hasOwnProperty('state_karugamo')) {
        this.state_karugamo = initObj.state_karugamo
      }
      else {
        this.state_karugamo = '';
      }
      if (initObj.hasOwnProperty('state_collision')) {
        this.state_collision = initObj.state_collision
      }
      else {
        this.state_collision = '';
      }
      if (initObj.hasOwnProperty('state_danger')) {
        this.state_danger = initObj.state_danger
      }
      else {
        this.state_danger = '';
      }
      if (initObj.hasOwnProperty('state_costmap')) {
        this.state_costmap = initObj.state_costmap
      }
      else {
        this.state_costmap = '';
      }
      if (initObj.hasOwnProperty('state_manual')) {
        this.state_manual = initObj.state_manual
      }
      else {
        this.state_manual = '';
      }
      if (initObj.hasOwnProperty('state_scan')) {
        this.state_scan = initObj.state_scan
      }
      else {
        this.state_scan = '';
      }
      if (initObj.hasOwnProperty('state_load')) {
        this.state_load = initObj.state_load
      }
      else {
        this.state_load = '';
      }
      if (initObj.hasOwnProperty('state_shelf')) {
        this.state_shelf = initObj.state_shelf
      }
      else {
        this.state_shelf = '';
      }
      if (initObj.hasOwnProperty('state_navigation')) {
        this.state_navigation = initObj.state_navigation
      }
      else {
        this.state_navigation = '';
      }
      if (initObj.hasOwnProperty('costmap')) {
        this.costmap = initObj.costmap
      }
      else {
        this.costmap = 0.0;
      }
      if (initObj.hasOwnProperty('side_joystick')) {
        this.side_joystick = initObj.side_joystick
      }
      else {
        this.side_joystick = 0.0;
      }
      if (initObj.hasOwnProperty('ctrl_front')) {
        this.ctrl_front = initObj.ctrl_front
      }
      else {
        this.ctrl_front = 0.0;
      }
      if (initObj.hasOwnProperty('ctrl_side')) {
        this.ctrl_side = initObj.ctrl_side
      }
      else {
        this.ctrl_side = 0.0;
      }
      if (initObj.hasOwnProperty('trackeds')) {
        this.trackeds = initObj.trackeds
      }
      else {
        this.trackeds = new geometry_msgs.msg.Twist();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type States
    // Serialize message field [state]
    bufferOffset = _serializer.string(obj.state, buffer, bufferOffset);
    // Serialize message field [state_karugamo]
    bufferOffset = _serializer.string(obj.state_karugamo, buffer, bufferOffset);
    // Serialize message field [state_collision]
    bufferOffset = _serializer.string(obj.state_collision, buffer, bufferOffset);
    // Serialize message field [state_danger]
    bufferOffset = _serializer.string(obj.state_danger, buffer, bufferOffset);
    // Serialize message field [state_costmap]
    bufferOffset = _serializer.string(obj.state_costmap, buffer, bufferOffset);
    // Serialize message field [state_manual]
    bufferOffset = _serializer.string(obj.state_manual, buffer, bufferOffset);
    // Serialize message field [state_scan]
    bufferOffset = _serializer.string(obj.state_scan, buffer, bufferOffset);
    // Serialize message field [state_load]
    bufferOffset = _serializer.string(obj.state_load, buffer, bufferOffset);
    // Serialize message field [state_shelf]
    bufferOffset = _serializer.string(obj.state_shelf, buffer, bufferOffset);
    // Serialize message field [state_navigation]
    bufferOffset = _serializer.string(obj.state_navigation, buffer, bufferOffset);
    // Serialize message field [costmap]
    bufferOffset = _serializer.float32(obj.costmap, buffer, bufferOffset);
    // Serialize message field [side_joystick]
    bufferOffset = _serializer.float32(obj.side_joystick, buffer, bufferOffset);
    // Serialize message field [ctrl_front]
    bufferOffset = _serializer.float32(obj.ctrl_front, buffer, bufferOffset);
    // Serialize message field [ctrl_side]
    bufferOffset = _serializer.float32(obj.ctrl_side, buffer, bufferOffset);
    // Serialize message field [trackeds]
    bufferOffset = geometry_msgs.msg.Twist.serialize(obj.trackeds, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type States
    let len;
    let data = new States(null);
    // Deserialize message field [state]
    data.state = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_karugamo]
    data.state_karugamo = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_collision]
    data.state_collision = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_danger]
    data.state_danger = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_costmap]
    data.state_costmap = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_manual]
    data.state_manual = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_scan]
    data.state_scan = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_load]
    data.state_load = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_shelf]
    data.state_shelf = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_navigation]
    data.state_navigation = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [costmap]
    data.costmap = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [side_joystick]
    data.side_joystick = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [ctrl_front]
    data.ctrl_front = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [ctrl_side]
    data.ctrl_side = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [trackeds]
    data.trackeds = geometry_msgs.msg.Twist.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.state.length;
    length += object.state_karugamo.length;
    length += object.state_collision.length;
    length += object.state_danger.length;
    length += object.state_costmap.length;
    length += object.state_manual.length;
    length += object.state_scan.length;
    length += object.state_load.length;
    length += object.state_shelf.length;
    length += object.state_navigation.length;
    return length + 104;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pitakuru/States';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '020c7260fce8cdbd7570da53eb117321';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string state
    string state_karugamo
    string state_collision
    string state_danger
    string state_costmap
    string state_manual
    string state_scan
    string state_load
    string state_shelf
    string state_navigation
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
    float64 z
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new States(null);
    if (msg.state !== undefined) {
      resolved.state = msg.state;
    }
    else {
      resolved.state = ''
    }

    if (msg.state_karugamo !== undefined) {
      resolved.state_karugamo = msg.state_karugamo;
    }
    else {
      resolved.state_karugamo = ''
    }

    if (msg.state_collision !== undefined) {
      resolved.state_collision = msg.state_collision;
    }
    else {
      resolved.state_collision = ''
    }

    if (msg.state_danger !== undefined) {
      resolved.state_danger = msg.state_danger;
    }
    else {
      resolved.state_danger = ''
    }

    if (msg.state_costmap !== undefined) {
      resolved.state_costmap = msg.state_costmap;
    }
    else {
      resolved.state_costmap = ''
    }

    if (msg.state_manual !== undefined) {
      resolved.state_manual = msg.state_manual;
    }
    else {
      resolved.state_manual = ''
    }

    if (msg.state_scan !== undefined) {
      resolved.state_scan = msg.state_scan;
    }
    else {
      resolved.state_scan = ''
    }

    if (msg.state_load !== undefined) {
      resolved.state_load = msg.state_load;
    }
    else {
      resolved.state_load = ''
    }

    if (msg.state_shelf !== undefined) {
      resolved.state_shelf = msg.state_shelf;
    }
    else {
      resolved.state_shelf = ''
    }

    if (msg.state_navigation !== undefined) {
      resolved.state_navigation = msg.state_navigation;
    }
    else {
      resolved.state_navigation = ''
    }

    if (msg.costmap !== undefined) {
      resolved.costmap = msg.costmap;
    }
    else {
      resolved.costmap = 0.0
    }

    if (msg.side_joystick !== undefined) {
      resolved.side_joystick = msg.side_joystick;
    }
    else {
      resolved.side_joystick = 0.0
    }

    if (msg.ctrl_front !== undefined) {
      resolved.ctrl_front = msg.ctrl_front;
    }
    else {
      resolved.ctrl_front = 0.0
    }

    if (msg.ctrl_side !== undefined) {
      resolved.ctrl_side = msg.ctrl_side;
    }
    else {
      resolved.ctrl_side = 0.0
    }

    if (msg.trackeds !== undefined) {
      resolved.trackeds = geometry_msgs.msg.Twist.Resolve(msg.trackeds)
    }
    else {
      resolved.trackeds = new geometry_msgs.msg.Twist()
    }

    return resolved;
    }
};

module.exports = States;
