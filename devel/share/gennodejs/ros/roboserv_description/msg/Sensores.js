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

class Sensores {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.SensorF = null;
      this.SensorL = null;
      this.SensorR = null;
      this.SensorT = null;
    }
    else {
      if (initObj.hasOwnProperty('SensorF')) {
        this.SensorF = initObj.SensorF
      }
      else {
        this.SensorF = 0.0;
      }
      if (initObj.hasOwnProperty('SensorL')) {
        this.SensorL = initObj.SensorL
      }
      else {
        this.SensorL = 0.0;
      }
      if (initObj.hasOwnProperty('SensorR')) {
        this.SensorR = initObj.SensorR
      }
      else {
        this.SensorR = 0.0;
      }
      if (initObj.hasOwnProperty('SensorT')) {
        this.SensorT = initObj.SensorT
      }
      else {
        this.SensorT = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Sensores
    // Serialize message field [SensorF]
    bufferOffset = _serializer.float32(obj.SensorF, buffer, bufferOffset);
    // Serialize message field [SensorL]
    bufferOffset = _serializer.float32(obj.SensorL, buffer, bufferOffset);
    // Serialize message field [SensorR]
    bufferOffset = _serializer.float32(obj.SensorR, buffer, bufferOffset);
    // Serialize message field [SensorT]
    bufferOffset = _serializer.float32(obj.SensorT, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Sensores
    let len;
    let data = new Sensores(null);
    // Deserialize message field [SensorF]
    data.SensorF = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [SensorL]
    data.SensorL = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [SensorR]
    data.SensorR = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [SensorT]
    data.SensorT = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'roboserv_description/Sensores';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1098e5ac0a1250d94a2ff805714a24fa';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 SensorF
    float32 SensorL
    float32 SensorR
    float32 SensorT
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Sensores(null);
    if (msg.SensorF !== undefined) {
      resolved.SensorF = msg.SensorF;
    }
    else {
      resolved.SensorF = 0.0
    }

    if (msg.SensorL !== undefined) {
      resolved.SensorL = msg.SensorL;
    }
    else {
      resolved.SensorL = 0.0
    }

    if (msg.SensorR !== undefined) {
      resolved.SensorR = msg.SensorR;
    }
    else {
      resolved.SensorR = 0.0
    }

    if (msg.SensorT !== undefined) {
      resolved.SensorT = msg.SensorT;
    }
    else {
      resolved.SensorT = 0.0
    }

    return resolved;
    }
};

module.exports = Sensores;
