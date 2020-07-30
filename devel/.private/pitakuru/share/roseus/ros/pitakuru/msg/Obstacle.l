;; Auto-generated. Do not edit!


(when (boundp 'pitakuru::Obstacle)
  (if (not (find-package "PITAKURU"))
    (make-package "PITAKURU"))
  (shadow 'Obstacle (find-package "PITAKURU")))
(unless (find-package "PITAKURU::OBSTACLE")
  (make-package "PITAKURU::OBSTACLE"))

(in-package "ROS")
;;//! \htmlinclude Obstacle.msg.html


(intern "*TYPE_WARNING*" (find-package "PITAKURU::OBSTACLE"))
(shadow '*TYPE_WARNING* (find-package "PITAKURU::OBSTACLE"))
(defconstant pitakuru::Obstacle::*TYPE_WARNING* 0)
(intern "*TYPE_DANGER*" (find-package "PITAKURU::OBSTACLE"))
(shadow '*TYPE_DANGER* (find-package "PITAKURU::OBSTACLE"))
(defconstant pitakuru::Obstacle::*TYPE_DANGER* 1)
(defclass pitakuru::Obstacle
  :super ros::object
  :slots (_type _angle _distance ))

(defmethod pitakuru::Obstacle
  (:init
   (&key
    ((:type __type) 0)
    ((:angle __angle) 0.0)
    ((:distance __distance) 0.0)
    )
   (send-super :init)
   (setq _type (round __type))
   (setq _angle (float __angle))
   (setq _distance (float __distance))
   self)
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:distance
   (&optional __distance)
   (if __distance (setq _distance __distance)) _distance)
  (:serialization-length
   ()
   (+
    ;; uint8 _type
    1
    ;; float32 _angle
    4
    ;; float32 _distance
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _type
       (write-byte _type s)
     ;; float32 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _distance
       (sys::poke _distance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _type
     (setq _type (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _angle
     (setq _angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _distance
     (setq _distance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get pitakuru::Obstacle :md5sum-) "63d99a9ad294899d03af106edf098ef1")
(setf (get pitakuru::Obstacle :datatype-) "pitakuru/Obstacle")
(setf (get pitakuru::Obstacle :definition-)
      "uint8 TYPE_WARNING=0
uint8 TYPE_DANGER=1
uint8 type
float32 angle
float32 distance
")



(provide :pitakuru/Obstacle "63d99a9ad294899d03af106edf098ef1")


