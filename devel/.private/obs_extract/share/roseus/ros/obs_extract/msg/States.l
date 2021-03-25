;; Auto-generated. Do not edit!


(when (boundp 'obs_extract::States)
  (if (not (find-package "OBS_EXTRACT"))
    (make-package "OBS_EXTRACT"))
  (shadow 'States (find-package "OBS_EXTRACT")))
(unless (find-package "OBS_EXTRACT::STATES")
  (make-package "OBS_EXTRACT::STATES"))

(in-package "ROS")
;;//! \htmlinclude States.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass obs_extract::States
  :super ros::object
  :slots (_state _state_karugamo _state_collision _state_danger _state_costmap _state_manual _state_scan _trackeds ))

(defmethod obs_extract::States
  (:init
   (&key
    ((:state __state) "")
    ((:state_karugamo __state_karugamo) "")
    ((:state_collision __state_collision) "")
    ((:state_danger __state_danger) "")
    ((:state_costmap __state_costmap) "")
    ((:state_manual __state_manual) "")
    ((:state_scan __state_scan) "")
    ((:trackeds __trackeds) (instance geometry_msgs::Twist :init))
    )
   (send-super :init)
   (setq _state (string __state))
   (setq _state_karugamo (string __state_karugamo))
   (setq _state_collision (string __state_collision))
   (setq _state_danger (string __state_danger))
   (setq _state_costmap (string __state_costmap))
   (setq _state_manual (string __state_manual))
   (setq _state_scan (string __state_scan))
   (setq _trackeds __trackeds)
   self)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:state_karugamo
   (&optional __state_karugamo)
   (if __state_karugamo (setq _state_karugamo __state_karugamo)) _state_karugamo)
  (:state_collision
   (&optional __state_collision)
   (if __state_collision (setq _state_collision __state_collision)) _state_collision)
  (:state_danger
   (&optional __state_danger)
   (if __state_danger (setq _state_danger __state_danger)) _state_danger)
  (:state_costmap
   (&optional __state_costmap)
   (if __state_costmap (setq _state_costmap __state_costmap)) _state_costmap)
  (:state_manual
   (&optional __state_manual)
   (if __state_manual (setq _state_manual __state_manual)) _state_manual)
  (:state_scan
   (&optional __state_scan)
   (if __state_scan (setq _state_scan __state_scan)) _state_scan)
  (:trackeds
   (&rest __trackeds)
   (if (keywordp (car __trackeds))
       (send* _trackeds __trackeds)
     (progn
       (if __trackeds (setq _trackeds (car __trackeds)))
       _trackeds)))
  (:serialization-length
   ()
   (+
    ;; string _state
    4 (length _state)
    ;; string _state_karugamo
    4 (length _state_karugamo)
    ;; string _state_collision
    4 (length _state_collision)
    ;; string _state_danger
    4 (length _state_danger)
    ;; string _state_costmap
    4 (length _state_costmap)
    ;; string _state_manual
    4 (length _state_manual)
    ;; string _state_scan
    4 (length _state_scan)
    ;; geometry_msgs/Twist _trackeds
    (send _trackeds :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _state
       (write-long (length _state) s) (princ _state s)
     ;; string _state_karugamo
       (write-long (length _state_karugamo) s) (princ _state_karugamo s)
     ;; string _state_collision
       (write-long (length _state_collision) s) (princ _state_collision s)
     ;; string _state_danger
       (write-long (length _state_danger) s) (princ _state_danger s)
     ;; string _state_costmap
       (write-long (length _state_costmap) s) (princ _state_costmap s)
     ;; string _state_manual
       (write-long (length _state_manual) s) (princ _state_manual s)
     ;; string _state_scan
       (write-long (length _state_scan) s) (princ _state_scan s)
     ;; geometry_msgs/Twist _trackeds
       (send _trackeds :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _state
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state_karugamo
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_karugamo (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state_collision
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_collision (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state_danger
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_danger (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state_costmap
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_costmap (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state_manual
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_manual (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state_scan
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_scan (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Twist _trackeds
     (send _trackeds :deserialize buf ptr-) (incf ptr- (send _trackeds :serialization-length))
   ;;
   self)
  )

(setf (get obs_extract::States :md5sum-) "dfd48cf7701c5d144c13acc5c8b54ec0")
(setf (get obs_extract::States :datatype-) "obs_extract/States")
(setf (get obs_extract::States :definition-)
      "string state
string state_karugamo
string state_collision
string state_danger
string state_costmap
string state_manual
string state_scan
geometry_msgs/Twist trackeds

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
")



(provide :obs_extract/States "dfd48cf7701c5d144c13acc5c8b54ec0")


