// Auto-generated. Do not edit!

// (in-package roboserv_description.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class AppMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.operation_mode = null;
      this.navigation_mode = null;
      this.button_up = null;
      this.button_down = null;
      this.button_left = null;
      this.button_right = null;
      this.button_up_left = null;
      this.button_up_right = null;
      this.button_down_left = null;
      this.button_down_right = null;
      this.robot_pos_x = null;
      this.robot_pos_y = null;
    }
    else {
      if (initObj.hasOwnProperty('operation_mode')) {
        this.operation_mode = initObj.operation_mode
      }
      else {
        this.operation_mode = 0;
      }
      if (initObj.hasOwnProperty('navigation_mode')) {
        this.navigation_mode = initObj.navigation_mode
      }
      else {
        this.navigation_mode = 0;
      }
      if (initObj.hasOwnProperty('button_up')) {
        this.button_up = initObj.button_up
      }
      else {
        this.button_up = false;
      }
      if (initObj.hasOwnProperty('button_down')) {
        this.button_down = initObj.button_down
      }
      else {
        this.button_down = false;
      }
      if (initObj.hasOwnProperty('button_left')) {
        this.button_left = initObj.button_left
      }
      else {
        this.button_left = false;
      }
      if (initObj.hasOwnProperty('button_right')) {
        this.button_right = initObj.button_right
      }
      else {
        this.button_right = false;
      }
      if (initObj.hasOwnProperty('button_up_left')) {
        this.button_up_left = initObj.button_up_left
      }
      else {
        this.button_up_left = false;
      }
      if (initObj.hasOwnProperty('button_up_right')) {
        this.button_up_right = initObj.button_up_right
      }
      else {
        this.button_up_right = false;
      }
      if (initObj.hasOwnProperty('button_down_left')) {
        this.button_down_left = initObj.button_down_left
      }
      else {
        this.button_down_left = false;
      }
      if (initObj.hasOwnProperty('button_down_right')) {
        this.button_down_right = initObj.button_down_right
      }
      else {
        this.button_down_right = false;
      }
      if (initObj.hasOwnProperty('robot_pos_x')) {
        this.robot_pos_x = initObj.robot_pos_x
      }
      else {
        this.robot_pos_x = 0.0;
      }
      if (initObj.hasOwnProperty('robot_pos_y')) {
        this.robot_pos_y = initObj.robot_pos_y
      }
      else {
        this.robot_pos_y = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type AppMsg
    // Serialize message field [operation_mode]
    bufferOffset = _serializer.uint8(obj.operation_mode, buffer, bufferOffset);
    // Serialize message field [navigation_mode]
    bufferOffset = _serializer.uint8(obj.navigation_mode, buffer, bufferOffset);
    // Serialize message field [button_up]
    bufferOffset = _serializer.bool(obj.button_up, buffer, bufferOffset);
    // Serialize message field [button_down]
    bufferOffset = _serializer.bool(obj.button_down, buffer, bufferOffset);
    // Serialize message field [button_left]
    bufferOffset = _serializer.bool(obj.button_left, buffer, bufferOffset);
    // Serialize message field [button_right]
    bufferOffset = _serializer.bool(obj.button_right, buffer, bufferOffset);
    // Serialize message field [button_up_left]
    bufferOffset = _serializer.bool(obj.button_up_left, buffer, bufferOffset);
    // Serialize message field [button_up_right]
    bufferOffset = _serializer.bool(obj.button_up_right, buffer, bufferOffset);
    // Serialize message field [button_down_left]
    bufferOffset = _serializer.bool(obj.button_down_left, buffer, bufferOffset);
    // Serialize message field [button_down_right]
    bufferOffset = _serializer.bool(obj.button_down_right, buffer, bufferOffset);
    // Serialize message field [robot_pos_x]
    bufferOffset = _serializer.float32(obj.robot_pos_x, buffer, bufferOffset);
    // Serialize message field [robot_pos_y]
    bufferOffset = _serializer.float32(obj.robot_pos_y, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type AppMsg
    let len;
    let data = new AppMsg(null);
    // Deserialize message field [operation_mode]
    data.operation_mode = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [navigation_mode]
    data.navigation_mode = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [button_up]
    data.button_up = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [button_down]
    data.button_down = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [button_left]
    data.button_left = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [button_right]
    data.button_right = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [button_up_left]
    data.button_up_left = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [button_up_right]
    data.button_up_right = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [button_down_left]
    data.button_down_left = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [button_down_right]
    data.button_down_right = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [robot_pos_x]
    data.robot_pos_x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [robot_pos_y]
    data.robot_pos_y = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 18;
  }

  static datatype() {
    // Returns string type for a message object
    return 'roboserv_description/AppMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '02779d669f715c0c7649d0bb288210ee';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 operation_mode
    uint8 navigation_mode
    bool button_up
    bool button_down
    bool button_left
    bool button_right
    bool button_up_left
    bool button_up_right
    bool button_down_left
    bool button_down_right
    float32 robot_pos_x
    float32 robot_pos_y
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new AppMsg(null);
    if (msg.operation_mode !== undefined) {
      resolved.operation_mode = msg.operation_mode;
    }
    else {
      resolved.operation_mode = 0
    }

    if (msg.navigation_mode !== undefined) {
      resolved.navigation_mode = msg.navigation_mode;
    }
    else {
      resolved.navigation_mode = 0
    }

    if (msg.button_up !== undefined) {
      resolved.button_up = msg.button_up;
    }
    else {
      resolved.button_up = false
    }

    if (msg.button_down !== undefined) {
      resolved.button_down = msg.button_down;
    }
    else {
      resolved.button_down = false
    }

    if (msg.button_left !== undefined) {
      resolved.button_left = msg.button_left;
    }
    else {
      resolved.button_left = false
    }

    if (msg.button_right !== undefined) {
      resolved.button_right = msg.button_right;
    }
    else {
      resolved.button_right = false
    }

    if (msg.button_up_left !== undefined) {
      resolved.button_up_left = msg.button_up_left;
    }
    else {
      resolved.button_up_left = false
    }

    if (msg.button_up_right !== undefined) {
      resolved.button_up_right = msg.button_up_right;
    }
    else {
      resolved.button_up_right = false
    }

    if (msg.button_down_left !== undefined) {
      resolved.button_down_left = msg.button_down_left;
    }
    else {
      resolved.button_down_left = false
    }

    if (msg.button_down_right !== undefined) {
      resolved.button_down_right = msg.button_down_right;
    }
    else {
      resolved.button_down_right = false
    }

    if (msg.robot_pos_x !== undefined) {
      resolved.robot_pos_x = msg.robot_pos_x;
    }
    else {
      resolved.robot_pos_x = 0.0
    }

    if (msg.robot_pos_y !== undefined) {
      resolved.robot_pos_y = msg.robot_pos_y;
    }
    else {
      resolved.robot_pos_y = 0.0
    }

    return resolved;
    }
};

module.exports = AppMsg;
