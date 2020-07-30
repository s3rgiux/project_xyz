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

class TriggerAction {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.trigger = null;
    }
    else {
      if (initObj.hasOwnProperty('trigger')) {
        this.trigger = initObj.trigger
      }
      else {
        this.trigger = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TriggerAction
    // Serialize message field [trigger]
    bufferOffset = _serializer.string(obj.trigger, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TriggerAction
    let len;
    let data = new TriggerAction(null);
    // Deserialize message field [trigger]
    data.trigger = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.trigger.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'control_xy/TriggerAction';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '529f37831afe7067075cb584db0e391e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # 非常停止ボタン解除
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TriggerAction(null);
    if (msg.trigger !== undefined) {
      resolved.trigger = msg.trigger;
    }
    else {
      resolved.trigger = ''
    }

    return resolved;
    }
};

// Constants for message
TriggerAction.Constants = {
  TRIGGER_EMERGENCY_BUTTON_OFF: 'emergency_button_off',
  TRIGGER_EMERGENCY_BUTTON_ON: 'emergency_button_on',
  TRIGGER_KARUGAMO_BUTTON_ON: 'karugamo_button_on',
  TRIGGER_REMOTE_KARUGAMO_BUTTON_ON: 'remote_karuamo_button_on',
  TRIGGER_REMOTE_MANUAL_BUTTON_ON: 'remote_manual_button_on',
  TRIGGER_REMOTE_IDLE_BUTTON_ON: 'remote_idle_button_on',
  TRIGGER_IDLE_BUTTON_ON: 'idle_button_on',
  TRIGGER_DETECT_OBSTACLE: 'detect_obstacle',
  TRIGGER_DETECT_DANGER_OBSTACLE: 'detect_danger_obstacle',
  TRIGGER_COLLISION: 'collision',
  TRIGGER_BREAK_RELEASE_BUTTON_ON: 'break_release_button_on',
  TRIGGER_LONG_LOST: 'long_lost',
}

module.exports = TriggerAction;
