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

class Motores {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.MotorL = null;
      this.MotorR = null;
    }
    else {
      if (initObj.hasOwnProperty('MotorL')) {
        this.MotorL = initObj.MotorL
      }
      else {
        this.MotorL = 0;
      }
      if (initObj.hasOwnProperty('MotorR')) {
        this.MotorR = initObj.MotorR
      }
      else {
        this.MotorR = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Motores
    // Serialize message field [MotorL]
    bufferOffset = _serializer.int32(obj.MotorL, buffer, bufferOffset);
    // Serialize message field [MotorR]
    bufferOffset = _serializer.int32(obj.MotorR, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Motores
    let len;
    let data = new Motores(null);
    // Deserialize message field [MotorL]
    data.MotorL = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [MotorR]
    data.MotorR = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'roboserv_description/Motores';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '28ee0bcd94a4539f94474748fbc61333';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 MotorL
    int32 MotorR
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Motores(null);
    if (msg.MotorL !== undefined) {
      resolved.MotorL = msg.MotorL;
    }
    else {
      resolved.MotorL = 0
    }

    if (msg.MotorR !== undefined) {
      resolved.MotorR = msg.MotorR;
    }
    else {
      resolved.MotorR = 0
    }

    return resolved;
    }
};

module.exports = Motores;
