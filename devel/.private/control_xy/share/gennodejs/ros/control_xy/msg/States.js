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

class States {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.state = null;
      this.state_karugamo = null;
      this.state_collision = null;
      this.state_danger = null;
      this.state_costmap = null;
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
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.state.length;
    length += object.state_karugamo.length;
    length += object.state_collision.length;
    length += object.state_danger.length;
    length += object.state_costmap.length;
    return length + 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'control_xy/States';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a970e58c537add5954e8c37ff3305a1c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string state
    string state_karugamo
    string state_collision
    string state_danger
    string state_costmap
    
    
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

    return resolved;
    }
};

module.exports = States;
