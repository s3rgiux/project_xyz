;; Auto-generated. Do not edit!


(when (boundp 'pypro::StateWheels)
  (if (not (find-package "PYPRO"))
    (make-package "PYPRO"))
  (shadow 'StateWheels (find-package "PYPRO")))
(unless (find-package "PYPRO::STATEWHEELS")
  (make-package "PYPRO::STATEWHEELS"))

(in-package "ROS")
;;//! \htmlinclude StateWheels.msg.html


(defclass pypro::StateWheels
  :super ros::object
  :slots (_left_vel _right_vel _left_current _right_current _time_stamp ))

(defmethod pypro::StateWheels
  (:init
   (&key
    ((:left_vel __left_vel) 0.0)
    ((:right_vel __right_vel) 0.0)
    ((:left_current __left_current) 0.0)
    ((:right_current __right_current) 0.0)
    ((:time_stamp __time_stamp) (instance ros::time :init))
    )
   (send-super :init)
   (setq _left_vel (float __left_vel))
   (setq _right_vel (float __right_vel))
   (setq _left_current (float __left_current))
   (setq _right_current (float __right_current))
   (setq _time_stamp __time_stamp)
   self)
  (:left_vel
   (&optional __left_vel)
   (if __left_vel (setq _left_vel __left_vel)) _left_vel)
  (:right_vel
   (&optional __right_vel)
   (if __right_vel (setq _right_vel __right_vel)) _right_vel)
  (:left_current
   (&optional __left_current)
   (if __left_current (setq _left_current __left_current)) _left_current)
  (:right_current
   (&optional __right_current)
   (if __right_current (setq _right_current __right_current)) _right_current)
  (:time_stamp
   (&optional __time_stamp)
   (if __time_stamp (setq _time_stamp __time_stamp)) _time_stamp)
  (:serialization-length
   ()
   (+
    ;; float32 _left_vel
    4
    ;; float32 _right_vel
    4
    ;; float32 _left_current
    4
    ;; float32 _right_current
    4
    ;; time _time_stamp
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _left_vel
       (sys::poke _left_vel (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _right_vel
       (sys::poke _right_vel (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _left_current
       (sys::poke _left_current (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _right_current
       (sys::poke _right_current (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; time _time_stamp
       (write-long (send _time_stamp :sec) s) (write-long (send _time_stamp :nsec) s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _left_vel
     (setq _left_vel (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _right_vel
     (setq _right_vel (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _left_current
     (setq _left_current (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _right_current
     (setq _right_current (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; time _time_stamp
     (send _time_stamp :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _time_stamp :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get pypro::StateWheels :md5sum-) "fe7d42a99505b18a4db3afda942ff08d")
(setf (get pypro::StateWheels :datatype-) "pypro/StateWheels")
(setf (get pypro::StateWheels :definition-)
      "float32 left_vel
float32 right_vel
float32 left_current
float32 right_current
time time_stamp



")



(provide :pypro/StateWheels "fe7d42a99505b18a4db3afda942ff08d")


