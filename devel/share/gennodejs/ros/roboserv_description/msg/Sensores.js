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
      this.SensorL = null;
      this.SensorF = null;
      this.SensorR = null;
    }
    else {
      if (initObj.hasOwnProperty('SensorL')) {
        this.SensorL = initObj.SensorL
      }
      else {
        this.SensorL = 0.0;
      }
      if (initObj.hasOwnProperty('SensorF')) {
        this.SensorF = initObj.SensorF
      }
      else {
        this.SensorF = 0.0;
      }
      if (initObj.hasOwnProperty('SensorR')) {
        this.SensorR = initObj.SensorR
      }
      else {
        this.SensorR = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Sensores
    // Serialize message field [SensorL]
    bufferOffset = _serializer.float32(obj.SensorL, buffer, bufferOffset);
    // Serialize message field [SensorF]
    bufferOffset = _serializer.float32(obj.SensorF, buffer, bufferOffset);
    // Serialize message field [SensorR]
    bufferOffset = _serializer.float32(obj.SensorR, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Sensores
    let len;
    let data = new Sensores(null);
    // Deserialize message field [SensorL]
    data.SensorL = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [SensorF]
    data.SensorF = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [SensorR]
    data.SensorR = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'roboserv_description/Sensores';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4ab95327ee166468a1f69926574cd811';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 SensorL	
    float32 SensorF
    float32 SensorR
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Sensores(null);
    if (msg.SensorL !== undefined) {
      resolved.SensorL = msg.SensorL;
    }
    else {
      resolved.SensorL = 0.0
    }

    if (msg.SensorF !== undefined) {
      resolved.SensorF = msg.SensorF;
    }
    else {
      resolved.SensorF = 0.0
    }

    if (msg.SensorR !== undefined) {
      resolved.SensorR = msg.SensorR;
    }
    else {
      resolved.SensorR = 0.0
    }

    return resolved;
    }
};

module.exports = Sensores;
