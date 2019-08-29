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
  :slots (_SensorL _SensorFL _SensorF _SensorFR _SensorR ))

(defmethod roboserv_description::Sensores
  (:init
   (&key
    ((:SensorL __SensorL) 0.0)
    ((:SensorFL __SensorFL) 0.0)
    ((:SensorF __SensorF) 0.0)
    ((:SensorFR __SensorFR) 0.0)
    ((:SensorR __SensorR) 0.0)
    )
   (send-super :init)
   (setq _SensorL (float __SensorL))
   (setq _SensorFL (float __SensorFL))
   (setq _SensorF (float __SensorF))
   (setq _SensorFR (float __SensorFR))
   (setq _SensorR (float __SensorR))
   self)
  (:SensorL
   (&optional __SensorL)
   (if __SensorL (setq _SensorL __SensorL)) _SensorL)
  (:SensorFL
   (&optional __SensorFL)
   (if __SensorFL (setq _SensorFL __SensorFL)) _SensorFL)
  (:SensorF
   (&optional __SensorF)
   (if __SensorF (setq _SensorF __SensorF)) _SensorF)
  (:SensorFR
   (&optional __SensorFR)
   (if __SensorFR (setq _SensorFR __SensorFR)) _SensorFR)
  (:SensorR
   (&optional __SensorR)
   (if __SensorR (setq _SensorR __SensorR)) _SensorR)
  (:serialization-length
   ()
   (+
    ;; float32 _SensorL
    4
    ;; float32 _SensorFL
    4
    ;; float32 _SensorF
    4
    ;; float32 _SensorFR
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
     ;; float32 _SensorFL
       (sys::poke _SensorFL (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _SensorF
       (sys::poke _SensorF (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _SensorFR
       (sys::poke _SensorFR (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _SensorR
       (sys::poke _SensorR (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _SensorL
     (setq _SensorL (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _SensorFL
     (setq _SensorFL (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _SensorF
     (setq _SensorF (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _SensorFR
     (setq _SensorFR (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _SensorR
     (setq _SensorR (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get roboserv_description::Sensores :md5sum-) "4e7e993f2ad894e38becbb76ebb5ec09")
(setf (get roboserv_description::Sensores :datatype-) "roboserv_description/Sensores")
(setf (get roboserv_description::Sensores :definition-)
      "float32 SensorL
float32 SensorFL
float32 SensorF
float32 SensorFR
float32 SensorR

")



(provide :roboserv_description/Sensores "4e7e993f2ad894e38becbb76ebb5ec09")


