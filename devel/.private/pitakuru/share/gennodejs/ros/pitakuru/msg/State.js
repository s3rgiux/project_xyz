// Auto-generated. Do not edit!

// (in-package pitakuru.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class State {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.state = null;
    }
    else {
      if (initObj.hasOwnProperty('state')) {
        this.state = initObj.state
      }
      else {
        this.state = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type State
    // Serialize message field [state]
    bufferOffset = _serializer.string(obj.state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type State
    let len;
    let data = new State(null);
    // Deserialize message field [state]
    data.state = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.state.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pitakuru/State';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1d1d2a87dda45fe2cfd2df8cea1145d9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # シャットダウン（非通電）
    string STATE_SHUTDOWN = SHUTDOWN
    # アイドル状態
    string STATE_IDLE = IDLE
    # 動作アクティブ:カルガモ
    string STATE_ACTIVE_KARUGAMO = ACTIVE_KARUGAMO
    # 動作アクティブ:マニュアル
    string STATE_ACTIVE_MANUAL = ACTIVE_MANUAL
    # エラー:近傍に障害物あり
    string STATE_ERROR_OBSTACLE = ERROR_OBSTACLE
    # エラー:ガードバンパー衝突検知
    string STATE_ERROR_COLLISION = ERROR_COLLISION
    
    string state
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new State(null);
    if (msg.state !== undefined) {
      resolved.state = msg.state;
    }
    else {
      resolved.state = ''
    }

    return resolved;
    }
};

// Constants for message
State.Constants = {
  STATE_SHUTDOWN: 'SHUTDOWN',
  STATE_IDLE: 'IDLE',
  STATE_ACTIVE_KARUGAMO: 'ACTIVE_KARUGAMO',
  STATE_ACTIVE_MANUAL: 'ACTIVE_MANUAL',
  STATE_ERROR_OBSTACLE: 'ERROR_OBSTACLE',
  STATE_ERROR_COLLISION: 'ERROR_COLLISION',
}

module.exports = State;
