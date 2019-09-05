; Auto-generated. Do not edit!


(cl:in-package roboserv_description-msg)


;//! \htmlinclude Motores.msg.html

(cl:defclass <Motores> (roslisp-msg-protocol:ros-message)
  ((MotorL
    :reader MotorL
    :initarg :MotorL
    :type cl:integer
    :initform 0)
   (MotorR
    :reader MotorR
    :initarg :MotorR
    :type cl:integer
    :initform 0))
)

(cl:defclass Motores (<Motores>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Motores>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Motores)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name roboserv_description-msg:<Motores> is deprecated: use roboserv_description-msg:Motores instead.")))

(cl:ensure-generic-function 'MotorL-val :lambda-list '(m))
(cl:defmethod MotorL-val ((m <Motores>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:MotorL-val is deprecated.  Use roboserv_description-msg:MotorL instead.")
  (MotorL m))

(cl:ensure-generic-function 'MotorR-val :lambda-list '(m))
(cl:defmethod MotorR-val ((m <Motores>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:MotorR-val is deprecated.  Use roboserv_description-msg:MotorR instead.")
  (MotorR m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Motores>) ostream)
  "Serializes a message object of type '<Motores>"
  (cl:let* ((signed (cl:slot-value msg 'MotorL)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'MotorR)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Motores>) istream)
  "Deserializes a message object of type '<Motores>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'MotorL) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'MotorR) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Motores>)))
  "Returns string type for a message object of type '<Motores>"
  "roboserv_description/Motores")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Motores)))
  "Returns string type for a message object of type 'Motores"
  "roboserv_description/Motores")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Motores>)))
  "Returns md5sum for a message object of type '<Motores>"
  "28ee0bcd94a4539f94474748fbc61333")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Motores)))
  "Returns md5sum for a message object of type 'Motores"
  "28ee0bcd94a4539f94474748fbc61333")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Motores>)))
  "Returns full string definition for message of type '<Motores>"
  (cl:format cl:nil "int32 MotorL~%int32 MotorR~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Motores)))
  "Returns full string definition for message of type 'Motores"
  (cl:format cl:nil "int32 MotorL~%int32 MotorR~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Motores>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Motores>))
  "Converts a ROS message object to a list"
  (cl:list 'Motores
    (cl:cons ':MotorL (MotorL msg))
    (cl:cons ':MotorR (MotorR msg))
))
