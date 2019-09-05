;; Auto-generated. Do not edit!


(when (boundp 'roboserv_description::Motores)
  (if (not (find-package "ROBOSERV_DESCRIPTION"))
    (make-package "ROBOSERV_DESCRIPTION"))
  (shadow 'Motores (find-package "ROBOSERV_DESCRIPTION")))
(unless (find-package "ROBOSERV_DESCRIPTION::MOTORES")
  (make-package "ROBOSERV_DESCRIPTION::MOTORES"))

(in-package "ROS")
;;//! \htmlinclude Motores.msg.html


(defclass roboserv_description::Motores
  :super ros::object
  :slots (_MotorL _MotorR ))

(defmethod roboserv_description::Motores
  (:init
   (&key
    ((:MotorL __MotorL) 0)
    ((:MotorR __MotorR) 0)
    )
   (send-super :init)
   (setq _MotorL (round __MotorL))
   (setq _MotorR (round __MotorR))
   self)
  (:MotorL
   (&optional __MotorL)
   (if __MotorL (setq _MotorL __MotorL)) _MotorL)
  (:MotorR
   (&optional __MotorR)
   (if __MotorR (setq _MotorR __MotorR)) _MotorR)
  (:serialization-length
   ()
   (+
    ;; int32 _MotorL
    4
    ;; int32 _MotorR
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _MotorL
       (write-long _MotorL s)
     ;; int32 _MotorR
       (write-long _MotorR s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _MotorL
     (setq _MotorL (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _MotorR
     (setq _MotorR (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get roboserv_description::Motores :md5sum-) "28ee0bcd94a4539f94474748fbc61333")
(setf (get roboserv_description::Motores :datatype-) "roboserv_description/Motores")
(setf (get roboserv_description::Motores :definition-)
      "int32 MotorL
int32 MotorR

")



(provide :roboserv_description/Motores "28ee0bcd94a4539f94474748fbc61333")


