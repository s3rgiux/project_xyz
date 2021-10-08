// Auto-generated. Do not edit!

// (in-package segement_obstacle_danger.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class DangerStates {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.state_forward_circle = null;
      this.state_backward_circle = null;
      this.state_forward_segment = null;
      this.state_backward_segment = null;
    }
    else {
      if (initObj.hasOwnProperty('state_forward_circle')) {
        this.state_forward_circle = initObj.state_forward_circle
      }
      else {
        this.state_forward_circle = '';
      }
      if (initObj.hasOwnProperty('state_backward_circle')) {
        this.state_backward_circle = initObj.state_backward_circle
      }
      else {
        this.state_backward_circle = '';
      }
      if (initObj.hasOwnProperty('state_forward_segment')) {
        this.state_forward_segment = initObj.state_forward_segment
      }
      else {
        this.state_forward_segment = '';
      }
      if (initObj.hasOwnProperty('state_backward_segment')) {
        this.state_backward_segment = initObj.state_backward_segment
      }
      else {
        this.state_backward_segment = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DangerStates
    // Serialize message field [state_forward_circle]
    bufferOffset = _serializer.string(obj.state_forward_circle, buffer, bufferOffset);
    // Serialize message field [state_backward_circle]
    bufferOffset = _serializer.string(obj.state_backward_circle, buffer, bufferOffset);
    // Serialize message field [state_forward_segment]
    bufferOffset = _serializer.string(obj.state_forward_segment, buffer, bufferOffset);
    // Serialize message field [state_backward_segment]
    bufferOffset = _serializer.string(obj.state_backward_segment, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DangerStates
    let len;
    let data = new DangerStates(null);
    // Deserialize message field [state_forward_circle]
    data.state_forward_circle = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_backward_circle]
    data.state_backward_circle = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_forward_segment]
    data.state_forward_segment = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [state_backward_segment]
    data.state_backward_segment = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.state_forward_circle.length;
    length += object.state_backward_circle.length;
    length += object.state_forward_segment.length;
    length += object.state_backward_segment.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'segement_obstacle_danger/DangerStates';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '725ae9e90d4c8165163e7e160cab8649';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string state_forward_circle
    string state_backward_circle
    string state_forward_segment
    string state_backward_segment
    
    string DANGER = Danger
    string CLEAR = Clear
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DangerStates(null);
    if (msg.state_forward_circle !== undefined) {
      resolved.state_forward_circle = msg.state_forward_circle;
    }
    else {
      resolved.state_forward_circle = ''
    }

    if (msg.state_backward_circle !== undefined) {
      resolved.state_backward_circle = msg.state_backward_circle;
    }
    else {
      resolved.state_backward_circle = ''
    }

    if (msg.state_forward_segment !== undefined) {
      resolved.state_forward_segment = msg.state_forward_segment;
    }
    else {
      resolved.state_forward_segment = ''
    }

    if (msg.state_backward_segment !== undefined) {
      resolved.state_backward_segment = msg.state_backward_segment;
    }
    else {
      resolved.state_backward_segment = ''
    }

    return resolved;
    }
};

// Constants for message
DangerStates.Constants = {
  DANGER: 'Danger',
  CLEAR: 'Clear',
}

module.exports = DangerStates;
