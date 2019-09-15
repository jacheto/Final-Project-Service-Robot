;; Auto-generated. Do not edit!


(when (boundp 'roboserv_description::Sensores)
  (if (not (find-package "ROBOSERV_DESCRIPTION"))
    (make-package "ROBOSERV_DESCRIPTION"))
  (shadow 'Sensores (find-package "ROBOSERV_DESCRIPTION")))
(unless (find-package "ROBOSERV_DESCRIPTION::SENSORES")
  (make-package "ROBOSERV_DESCRIPTION::SENSORES"))

(in-package "ROS")
;;//! \htmlinclude Sensores.msg.html


(defclass roboserv_description::Sensores
  :super ros::object
  :slots (_SensorL _SensorF _SensorR ))

(defmethod roboserv_description::Sensores
  (:init
   (&key
    ((:SensorL __SensorL) 0.0)
    ((:SensorF __SensorF) 0.0)
    ((:SensorR __SensorR) 0.0)
    )
   (send-super :init)
   (setq _SensorL (float __SensorL))
   (setq _SensorF (float __SensorF))
   (setq _SensorR (float __SensorR))
   self)
  (:SensorL
   (&optional __SensorL)
   (if __SensorL (setq _SensorL __SensorL)) _SensorL)
  (:SensorF
   (&optional __SensorF)
   (if __SensorF (setq _SensorF __SensorF)) _SensorF)
  (:SensorR
   (&optional __SensorR)
   (if __SensorR (setq _SensorR __SensorR)) _SensorR)
  (:serialization-length
   ()
   (+
    ;; float32 _SensorL
    4
    ;; float32 _SensorF
    4
    ;; float32 _SensorR
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _SensorL
       (sys::poke _SensorL (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _SensorF
       (sys::poke _SensorF (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _SensorR
       (sys::poke _SensorR (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _SensorL
     (setq _SensorL (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _SensorF
     (setq _SensorF (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _SensorR
     (setq _SensorR (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get roboserv_description::Sensores :md5sum-) "4ab95327ee166468a1f69926574cd811")
(setf (get roboserv_description::Sensores :datatype-) "roboserv_description/Sensores")
(setf (get roboserv_description::Sensores :definition-)
      "float32 SensorL	
float32 SensorF
float32 SensorR

")



(provide :roboserv_description/Sensores "4ab95327ee166468a1f69926574cd811")


