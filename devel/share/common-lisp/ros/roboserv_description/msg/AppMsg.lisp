; Auto-generated. Do not edit!


(cl:in-package roboserv_description-msg)


;//! \htmlinclude AppMsg.msg.html

(cl:defclass <AppMsg> (roslisp-msg-protocol:ros-message)
  ((operation_mode
    :reader operation_mode
    :initarg :operation_mode
    :type cl:fixnum
    :initform 0)
   (navigation_mode
    :reader navigation_mode
    :initarg :navigation_mode
    :type cl:fixnum
    :initform 0)
   (button_up
    :reader button_up
    :initarg :button_up
    :type cl:boolean
    :initform cl:nil)
   (button_down
    :reader button_down
    :initarg :button_down
    :type cl:boolean
    :initform cl:nil)
   (button_left
    :reader button_left
    :initarg :button_left
    :type cl:boolean
    :initform cl:nil)
   (button_right
    :reader button_right
    :initarg :button_right
    :type cl:boolean
    :initform cl:nil)
   (button_up_left
    :reader button_up_left
    :initarg :button_up_left
    :type cl:boolean
    :initform cl:nil)
   (button_up_right
    :reader button_up_right
    :initarg :button_up_right
    :type cl:boolean
    :initform cl:nil)
   (button_down_left
    :reader button_down_left
    :initarg :button_down_left
    :type cl:boolean
    :initform cl:nil)
   (button_down_right
    :reader button_down_right
    :initarg :button_down_right
    :type cl:boolean
    :initform cl:nil)
   (robot_pos_x
    :reader robot_pos_x
    :initarg :robot_pos_x
    :type cl:float
    :initform 0.0)
   (robot_pos_y
    :reader robot_pos_y
    :initarg :robot_pos_y
    :type cl:float
    :initform 0.0))
)

(cl:defclass AppMsg (<AppMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AppMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AppMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name roboserv_description-msg:<AppMsg> is deprecated: use roboserv_description-msg:AppMsg instead.")))

(cl:ensure-generic-function 'operation_mode-val :lambda-list '(m))
(cl:defmethod operation_mode-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:operation_mode-val is deprecated.  Use roboserv_description-msg:operation_mode instead.")
  (operation_mode m))

(cl:ensure-generic-function 'navigation_mode-val :lambda-list '(m))
(cl:defmethod navigation_mode-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:navigation_mode-val is deprecated.  Use roboserv_description-msg:navigation_mode instead.")
  (navigation_mode m))

(cl:ensure-generic-function 'button_up-val :lambda-list '(m))
(cl:defmethod button_up-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:button_up-val is deprecated.  Use roboserv_description-msg:button_up instead.")
  (button_up m))

(cl:ensure-generic-function 'button_down-val :lambda-list '(m))
(cl:defmethod button_down-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:button_down-val is deprecated.  Use roboserv_description-msg:button_down instead.")
  (button_down m))

(cl:ensure-generic-function 'button_left-val :lambda-list '(m))
(cl:defmethod button_left-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:button_left-val is deprecated.  Use roboserv_description-msg:button_left instead.")
  (button_left m))

(cl:ensure-generic-function 'button_right-val :lambda-list '(m))
(cl:defmethod button_right-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:button_right-val is deprecated.  Use roboserv_description-msg:button_right instead.")
  (button_right m))

(cl:ensure-generic-function 'button_up_left-val :lambda-list '(m))
(cl:defmethod button_up_left-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:button_up_left-val is deprecated.  Use roboserv_description-msg:button_up_left instead.")
  (button_up_left m))

(cl:ensure-generic-function 'button_up_right-val :lambda-list '(m))
(cl:defmethod button_up_right-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:button_up_right-val is deprecated.  Use roboserv_description-msg:button_up_right instead.")
  (button_up_right m))

(cl:ensure-generic-function 'button_down_left-val :lambda-list '(m))
(cl:defmethod button_down_left-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:button_down_left-val is deprecated.  Use roboserv_description-msg:button_down_left instead.")
  (button_down_left m))

(cl:ensure-generic-function 'button_down_right-val :lambda-list '(m))
(cl:defmethod button_down_right-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:button_down_right-val is deprecated.  Use roboserv_description-msg:button_down_right instead.")
  (button_down_right m))

(cl:ensure-generic-function 'robot_pos_x-val :lambda-list '(m))
(cl:defmethod robot_pos_x-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:robot_pos_x-val is deprecated.  Use roboserv_description-msg:robot_pos_x instead.")
  (robot_pos_x m))

(cl:ensure-generic-function 'robot_pos_y-val :lambda-list '(m))
(cl:defmethod robot_pos_y-val ((m <AppMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader roboserv_description-msg:robot_pos_y-val is deprecated.  Use roboserv_description-msg:robot_pos_y instead.")
  (robot_pos_y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AppMsg>) ostream)
  "Serializes a message object of type '<AppMsg>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'operation_mode)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'navigation_mode)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'button_up) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'button_down) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'button_left) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'button_right) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'button_up_left) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'button_up_right) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'button_down_left) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'button_down_right) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'robot_pos_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'robot_pos_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AppMsg>) istream)
  "Deserializes a message object of type '<AppMsg>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'operation_mode)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'navigation_mode)) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'button_up) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'button_down) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'button_left) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'button_right) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'button_up_left) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'button_up_right) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'button_down_left) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'button_down_right) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'robot_pos_x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'robot_pos_y) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AppMsg>)))
  "Returns string type for a message object of type '<AppMsg>"
  "roboserv_description/AppMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AppMsg)))
  "Returns string type for a message object of type 'AppMsg"
  "roboserv_description/AppMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AppMsg>)))
  "Returns md5sum for a message object of type '<AppMsg>"
  "02779d669f715c0c7649d0bb288210ee")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AppMsg)))
  "Returns md5sum for a message object of type 'AppMsg"
  "02779d669f715c0c7649d0bb288210ee")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AppMsg>)))
  "Returns full string definition for message of type '<AppMsg>"
  (cl:format cl:nil "uint8 operation_mode~%uint8 navigation_mode~%bool button_up~%bool button_down~%bool button_left~%bool button_right~%bool button_up_left~%bool button_up_right~%bool button_down_left~%bool button_down_right~%float32 robot_pos_x~%float32 robot_pos_y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AppMsg)))
  "Returns full string definition for message of type 'AppMsg"
  (cl:format cl:nil "uint8 operation_mode~%uint8 navigation_mode~%bool button_up~%bool button_down~%bool button_left~%bool button_right~%bool button_up_left~%bool button_up_right~%bool button_down_left~%bool button_down_right~%float32 robot_pos_x~%float32 robot_pos_y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AppMsg>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AppMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'AppMsg
    (cl:cons ':operation_mode (operation_mode msg))
    (cl:cons ':navigation_mode (navigation_mode msg))
    (cl:cons ':button_up (button_up msg))
    (cl:cons ':button_down (button_down msg))
    (cl:cons ':button_left (button_left msg))
    (cl:cons ':button_right (button_right msg))
    (cl:cons ':button_up_left (button_up_left msg))
    (cl:cons ':button_up_right (button_up_right msg))
    (cl:cons ':button_down_left (button_down_left msg))
    (cl:cons ':button_down_right (button_down_right msg))
    (cl:cons ':robot_pos_x (robot_pos_x msg))
    (cl:cons ':robot_pos_y (robot_pos_y msg))
))
