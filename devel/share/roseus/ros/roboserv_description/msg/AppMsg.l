;; Auto-generated. Do not edit!


(when (boundp 'roboserv_description::AppMsg)
  (if (not (find-package "ROBOSERV_DESCRIPTION"))
    (make-package "ROBOSERV_DESCRIPTION"))
  (shadow 'AppMsg (find-package "ROBOSERV_DESCRIPTION")))
(unless (find-package "ROBOSERV_DESCRIPTION::APPMSG")
  (make-package "ROBOSERV_DESCRIPTION::APPMSG"))

(in-package "ROS")
;;//! \htmlinclude AppMsg.msg.html


(defclass roboserv_description::AppMsg
  :super ros::object
  :slots (_operation_mode _navigation_mode _button_up _button_down _button_left _button_right _button_up_left _button_up_right _button_down_left _button_down_right _robot_pos_x _robot_pos_y ))

(defmethod roboserv_description::AppMsg
  (:init
   (&key
    ((:operation_mode __operation_mode) 0)
    ((:navigation_mode __navigation_mode) 0)
    ((:button_up __button_up) nil)
    ((:button_down __button_down) nil)
    ((:button_left __button_left) nil)
    ((:button_right __button_right) nil)
    ((:button_up_left __button_up_left) nil)
    ((:button_up_right __button_up_right) nil)
    ((:button_down_left __button_down_left) nil)
    ((:button_down_right __button_down_right) nil)
    ((:robot_pos_x __robot_pos_x) 0.0)
    ((:robot_pos_y __robot_pos_y) 0.0)
    )
   (send-super :init)
   (setq _operation_mode (round __operation_mode))
   (setq _navigation_mode (round __navigation_mode))
   (setq _button_up __button_up)
   (setq _button_down __button_down)
   (setq _button_left __button_left)
   (setq _button_right __button_right)
   (setq _button_up_left __button_up_left)
   (setq _button_up_right __button_up_right)
   (setq _button_down_left __button_down_left)
   (setq _button_down_right __button_down_right)
   (setq _robot_pos_x (float __robot_pos_x))
   (setq _robot_pos_y (float __robot_pos_y))
   self)
  (:operation_mode
   (&optional __operation_mode)
   (if __operation_mode (setq _operation_mode __operation_mode)) _operation_mode)
  (:navigation_mode
   (&optional __navigation_mode)
   (if __navigation_mode (setq _navigation_mode __navigation_mode)) _navigation_mode)
  (:button_up
   (&optional __button_up)
   (if __button_up (setq _button_up __button_up)) _button_up)
  (:button_down
   (&optional __button_down)
   (if __button_down (setq _button_down __button_down)) _button_down)
  (:button_left
   (&optional __button_left)
   (if __button_left (setq _button_left __button_left)) _button_left)
  (:button_right
   (&optional __button_right)
   (if __button_right (setq _button_right __button_right)) _button_right)
  (:button_up_left
   (&optional __button_up_left)
   (if __button_up_left (setq _button_up_left __button_up_left)) _button_up_left)
  (:button_up_right
   (&optional __button_up_right)
   (if __button_up_right (setq _button_up_right __button_up_right)) _button_up_right)
  (:button_down_left
   (&optional __button_down_left)
   (if __button_down_left (setq _button_down_left __button_down_left)) _button_down_left)
  (:button_down_right
   (&optional __button_down_right)
   (if __button_down_right (setq _button_down_right __button_down_right)) _button_down_right)
  (:robot_pos_x
   (&optional __robot_pos_x)
   (if __robot_pos_x (setq _robot_pos_x __robot_pos_x)) _robot_pos_x)
  (:robot_pos_y
   (&optional __robot_pos_y)
   (if __robot_pos_y (setq _robot_pos_y __robot_pos_y)) _robot_pos_y)
  (:serialization-length
   ()
   (+
    ;; uint8 _operation_mode
    1
    ;; uint8 _navigation_mode
    1
    ;; bool _button_up
    1
    ;; bool _button_down
    1
    ;; bool _button_left
    1
    ;; bool _button_right
    1
    ;; bool _button_up_left
    1
    ;; bool _button_up_right
    1
    ;; bool _button_down_left
    1
    ;; bool _button_down_right
    1
    ;; float32 _robot_pos_x
    4
    ;; float32 _robot_pos_y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _operation_mode
       (write-byte _operation_mode s)
     ;; uint8 _navigation_mode
       (write-byte _navigation_mode s)
     ;; bool _button_up
       (if _button_up (write-byte -1 s) (write-byte 0 s))
     ;; bool _button_down
       (if _button_down (write-byte -1 s) (write-byte 0 s))
     ;; bool _button_left
       (if _button_left (write-byte -1 s) (write-byte 0 s))
     ;; bool _button_right
       (if _button_right (write-byte -1 s) (write-byte 0 s))
     ;; bool _button_up_left
       (if _button_up_left (write-byte -1 s) (write-byte 0 s))
     ;; bool _button_up_right
       (if _button_up_right (write-byte -1 s) (write-byte 0 s))
     ;; bool _button_down_left
       (if _button_down_left (write-byte -1 s) (write-byte 0 s))
     ;; bool _button_down_right
       (if _button_down_right (write-byte -1 s) (write-byte 0 s))
     ;; float32 _robot_pos_x
       (sys::poke _robot_pos_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _robot_pos_y
       (sys::poke _robot_pos_y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _operation_mode
     (setq _operation_mode (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _navigation_mode
     (setq _navigation_mode (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; bool _button_up
     (setq _button_up (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _button_down
     (setq _button_down (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _button_left
     (setq _button_left (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _button_right
     (setq _button_right (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _button_up_left
     (setq _button_up_left (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _button_up_right
     (setq _button_up_right (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _button_down_left
     (setq _button_down_left (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _button_down_right
     (setq _button_down_right (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32 _robot_pos_x
     (setq _robot_pos_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _robot_pos_y
     (setq _robot_pos_y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get roboserv_description::AppMsg :md5sum-) "02779d669f715c0c7649d0bb288210ee")
(setf (get roboserv_description::AppMsg :datatype-) "roboserv_description/AppMsg")
(setf (get roboserv_description::AppMsg :definition-)
      "uint8 operation_mode
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

")



(provide :roboserv_description/AppMsg "02779d669f715c0c7649d0bb288210ee")


