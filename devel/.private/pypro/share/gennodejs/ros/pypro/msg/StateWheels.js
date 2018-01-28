// Auto-generated. Do not edit!

// (in-package pypro.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class StateWheels {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.left_vel = null;
      this.right_vel = null;
      this.left_current = null;
      this.right_current = null;
      this.time_stamp = null;
    }
    else {
      if (initObj.hasOwnProperty('left_vel')) {
        this.left_vel = initObj.left_vel
      }
      else {
        this.left_vel = 0.0;
      }
      if (initObj.hasOwnProperty('right_vel')) {
        this.right_vel = initObj.right_vel
      }
      else {
        this.right_vel = 0.0;
      }
      if (initObj.hasOwnProperty('left_current')) {
        this.left_current = initObj.left_current
      }
      else {
        this.left_current = 0.0;
      }
      if (initObj.hasOwnProperty('right_current')) {
        this.right_current = initObj.right_current
      }
      else {
        this.right_current = 0.0;
      }
      if (initObj.hasOwnProperty('time_stamp')) {
        this.time_stamp = initObj.time_stamp
      }
      else {
        this.time_stamp = {secs: 0, nsecs: 0};
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type StateWheels
    // Serialize message field [left_vel]
    bufferOffset = _serializer.float32(obj.left_vel, buffer, bufferOffset);
    // Serialize message field [right_vel]
    bufferOffset = _serializer.float32(obj.right_vel, buffer, bufferOffset);
    // Serialize message field [left_current]
    bufferOffset = _serializer.float32(obj.left_current, buffer, bufferOffset);
    // Serialize message field [right_current]
    bufferOffset = _serializer.float32(obj.right_current, buffer, bufferOffset);
    // Serialize message field [time_stamp]
    bufferOffset = _serializer.time(obj.time_stamp, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type StateWheels
    let len;
    let data = new StateWheels(null);
    // Deserialize message field [left_vel]
    data.left_vel = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [right_vel]
    data.right_vel = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [left_current]
    data.left_current = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [right_current]
    data.right_current = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [time_stamp]
    data.time_stamp = _deserializer.time(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pypro/StateWheels';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fe7d42a99505b18a4db3afda942ff08d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 left_vel
    float32 right_vel
    float32 left_current
    float32 right_current
    time time_stamp
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new StateWheels(null);
    if (msg.left_vel !== undefined) {
      resolved.left_vel = msg.left_vel;
    }
    else {
      resolved.left_vel = 0.0
    }

    if (msg.right_vel !== undefined) {
      resolved.right_vel = msg.right_vel;
    }
    else {
      resolved.right_vel = 0.0
    }

    if (msg.left_current !== undefined) {
      resolved.left_current = msg.left_current;
    }
    else {
      resolved.left_current = 0.0
    }

    if (msg.right_current !== undefined) {
      resolved.right_current = msg.right_current;
    }
    else {
      resolved.right_current = 0.0
    }

    if (msg.time_stamp !== undefined) {
      resolved.time_stamp = msg.time_stamp;
    }
    else {
      resolved.time_stamp = {secs: 0, nsecs: 0}
    }

    return resolved;
    }
};

module.exports = StateWheels;
