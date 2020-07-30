// Auto-generated. Do not edit!

// (in-package control_xy.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class DriveWheel {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.left_rpm = null;
      this.right_rpm = null;
    }
    else {
      if (initObj.hasOwnProperty('left_rpm')) {
        this.left_rpm = initObj.left_rpm
      }
      else {
        this.left_rpm = 0.0;
      }
      if (initObj.hasOwnProperty('right_rpm')) {
        this.right_rpm = initObj.right_rpm
      }
      else {
        this.right_rpm = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DriveWheel
    // Serialize message field [left_rpm]
    bufferOffset = _serializer.float32(obj.left_rpm, buffer, bufferOffset);
    // Serialize message field [right_rpm]
    bufferOffset = _serializer.float32(obj.right_rpm, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DriveWheel
    let len;
    let data = new DriveWheel(null);
    // Deserialize message field [left_rpm]
    data.left_rpm = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [right_rpm]
    data.right_rpm = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'control_xy/DriveWheel';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fb0186777139ed5386fa80048788f9b4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 left_rpm
    float32 right_rpm
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DriveWheel(null);
    if (msg.left_rpm !== undefined) {
      resolved.left_rpm = msg.left_rpm;
    }
    else {
      resolved.left_rpm = 0.0
    }

    if (msg.right_rpm !== undefined) {
      resolved.right_rpm = msg.right_rpm;
    }
    else {
      resolved.right_rpm = 0.0
    }

    return resolved;
    }
};

module.exports = DriveWheel;
