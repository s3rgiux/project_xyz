;; Auto-generated. Do not edit!


(when (boundp 'pitakuru::DriveWheel)
  (if (not (find-package "PITAKURU"))
    (make-package "PITAKURU"))
  (shadow 'DriveWheel (find-package "PITAKURU")))
(unless (find-package "PITAKURU::DRIVEWHEEL")
  (make-package "PITAKURU::DRIVEWHEEL"))

(in-package "ROS")
;;//! \htmlinclude DriveWheel.msg.html


(defclass pitakuru::DriveWheel
  :super ros::object
  :slots (_left_rpm _right_rpm ))

(defmethod pitakuru::DriveWheel
  (:init
   (&key
    ((:left_rpm __left_rpm) 0.0)
    ((:right_rpm __right_rpm) 0.0)
    )
   (send-super :init)
   (setq _left_rpm (float __left_rpm))
   (setq _right_rpm (float __right_rpm))
   self)
  (:left_rpm
   (&optional __left_rpm)
   (if __left_rpm (setq _left_rpm __left_rpm)) _left_rpm)
  (:right_rpm
   (&optional __right_rpm)
   (if __right_rpm (setq _right_rpm __right_rpm)) _right_rpm)
  (:serialization-length
   ()
   (+
    ;; float32 _left_rpm
    4
    ;; float32 _right_rpm
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _left_rpm
       (sys::poke _left_rpm (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _right_rpm
       (sys::poke _right_rpm (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _left_rpm
     (setq _left_rpm (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _right_rpm
     (setq _right_rpm (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get pitakuru::DriveWheel :md5sum-) "fb0186777139ed5386fa80048788f9b4")
(setf (get pitakuru::DriveWheel :datatype-) "pitakuru/DriveWheel")
(setf (get pitakuru::DriveWheel :definition-)
      "float32 left_rpm
float32 right_rpm
")



(provide :pitakuru/DriveWheel "fb0186777139ed5386fa80048788f9b4")


