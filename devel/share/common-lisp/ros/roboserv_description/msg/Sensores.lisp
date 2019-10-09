; Auto-generated. Do not edit!


(cl:in-package roboserv_description-msg)


;//! \htmlinclude Sensores.msg.html

(cl:defclass <Sensores> (roslisp-msg-protocol:ros-message)
  ((SensorF
    :reader SensorF
    :initarg :SensorF
    :type cl:float
    :initform 0.0)
   (SensorL
    :reader SensorL
    :initarg :SensorL
    :type cl:float
    :initform 0.0)
   (SensorR
    :reader SensorR
    :initarg :SensorR
    :type cl:float
    :initform 0.0)
   (SensorT
    :reader SensorT
    :initarg :SensorT
    :type cl:float
    :initform 0.0))
)

(cl:defclass Sensores (<Sensores>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Sensores>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Sensores)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name roboserv_description-msg:<Sensores> is deprecated: use roboserv_description-msg:Sensores instead.")))

(cl:ensure-generic-function 'SensorF-val :lambda-list '(m))
(cl:defmethod SensorF-val ((m <Sensores>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:SensorF-val is deprecated.  Use roboserv_description-msg:SensorF instead.")
  (SensorF m))

(cl:ensure-generic-function 'SensorL-val :lambda-list '(m))
(cl:defmethod SensorL-val ((m <Sensores>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:SensorL-val is deprecated.  Use roboserv_description-msg:SensorL instead.")
  (SensorL m))

(cl:ensure-generic-function 'SensorR-val :lambda-list '(m))
(cl:defmethod SensorR-val ((m <Sensores>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:SensorR-val is deprecated.  Use roboserv_description-msg:SensorR instead.")
  (SensorR m))

(cl:ensure-generic-function 'SensorT-val :lambda-list '(m))
(cl:defmethod SensorT-val ((m <Sensores>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:SensorT-val is deprecated.  Use roboserv_description-msg:SensorT instead.")
  (SensorT m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Sensores>) ostream)
  "Serializes a message object of type '<Sensores>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'SensorF))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'SensorL))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'SensorR))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'SensorT))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Sensores>) istream)
  "Deserializes a message object of type '<Sensores>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'SensorF) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'SensorL) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'SensorR) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'SensorT) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Sensores>)))
  "Returns string type for a message object of type '<Sensores>"
  "roboserv_description/Sensores")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Sensores)))
  "Returns string type for a message object of type 'Sensores"
  "roboserv_description/Sensores")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Sensores>)))
  "Returns md5sum for a message object of type '<Sensores>"
  "1098e5ac0a1250d94a2ff805714a24fa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Sensores)))
  "Returns md5sum for a message object of type 'Sensores"
  "1098e5ac0a1250d94a2ff805714a24fa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Sensores>)))
  "Returns full string definition for message of type '<Sensores>"
  (cl:format cl:nil "float32 SensorF~%float32 SensorL~%float32 SensorR~%float32 SensorT~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Sensores)))
  "Returns full string definition for message of type 'Sensores"
  (cl:format cl:nil "float32 SensorF~%float32 SensorL~%float32 SensorR~%float32 SensorT~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Sensores>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Sensores>))
  "Converts a ROS message object to a list"
  (cl:list 'Sensores
    (cl:cons ':SensorF (SensorF msg))
    (cl:cons ':SensorL (SensorL msg))
    (cl:cons ':SensorR (SensorR msg))
    (cl:cons ':SensorT (SensorT msg))
))
