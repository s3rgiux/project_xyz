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
    return length + 76;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pitakuru/States';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'dfd48cf7701c5d144c13acc5c8b54ec0';
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
