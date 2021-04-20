;; Auto-generated. Do not edit!


(when (boundp 'peop_extract::States)
  (if (not (find-package "PEOP_EXTRACT"))
    (make-package "PEOP_EXTRACT"))
  (shadow 'States (find-package "PEOP_EXTRACT")))
(unless (find-package "PEOP_EXTRACT::STATES")
  (make-package "PEOP_EXTRACT::STATES"))

(in-package "ROS")
;;//! \htmlinclude States.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass peop_extract::States
  :super ros::object
  :slots (_state _state_karugamo _state_collision _state_danger _state_costmap _state_manual _state_scan _state_load _state_shelf _costmap _side_joystick _ctrl_front _ctrl_side _trackeds ))

(defmethod peop_extract::States
  (:init
   (&key
    ((:state __state) "")
    ((:state_karugamo __state_karugamo) "")
    ((:state_collision __state_collision) "")
    ((:state_danger __state_danger) "")
    ((:state_costmap __state_costmap) "")
    ((:state_manual __state_manual) "")
    ((:state_scan __state_scan) "")
    ((:state_load __state_load) "")
    ((:state_shelf __state_shelf) "")
    ((:costmap __costmap) 0.0)
    ((:side_joystick __side_joystick) 0.0)
    ((:ctrl_front __ctrl_front) 0.0)
    ((:ctrl_side __ctrl_side) 0.0)
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
   (setq _state_load (string __state_load))
   (setq _state_shelf (string __state_shelf))
   (setq _costmap (float __costmap))
   (setq _side_joystick (float __side_joystick))
   (setq _ctrl_front (float __ctrl_front))
   (setq _ctrl_side (float __ctrl_side))
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
  (:state_load
   (&optional __state_load)
   (if __state_load (setq _state_load __state_load)) _state_load)
  (:state_shelf
   (&optional __state_shelf)
   (if __state_shelf (setq _state_shelf __state_shelf)) _state_shelf)
  (:costmap
   (&optional __costmap)
   (if __costmap (setq _costmap __costmap)) _costmap)
  (:side_joystick
   (&optional __side_joystick)
   (if __side_joystick (setq _side_joystick __side_joystick)) _side_joystick)
  (:ctrl_front
   (&optional __ctrl_front)
   (if __ctrl_front (setq _ctrl_front __ctrl_front)) _ctrl_front)
  (:ctrl_side
   (&optional __ctrl_side)
   (if __ctrl_side (setq _ctrl_side __ctrl_side)) _ctrl_side)
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
    ;; string _state_load
    4 (length _state_load)
    ;; string _state_shelf
    4 (length _state_shelf)
    ;; float32 _costmap
    4
    ;; float32 _side_joystick
    4
    ;; float32 _ctrl_front
    4
    ;; float32 _ctrl_side
    4
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
     ;; string _state_load
       (write-long (length _state_load) s) (princ _state_load s)
     ;; string _state_shelf
       (write-long (length _state_shelf) s) (princ _state_shelf s)
     ;; float32 _costmap
       (sys::poke _costmap (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _side_joystick
       (sys::poke _side_joystick (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _ctrl_front
       (sys::poke _ctrl_front (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _ctrl_side
       (sys::poke _ctrl_side (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
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
   ;; string _state_load
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_load (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state_shelf
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_shelf (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _costmap
     (setq _costmap (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _side_joystick
     (setq _side_joystick (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _ctrl_front
     (setq _ctrl_front (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _ctrl_side
     (setq _ctrl_side (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; geometry_msgs/Twist _trackeds
     (send _trackeds :deserialize buf ptr-) (incf ptr- (send _trackeds :serialization-length))
   ;;
   self)
  )

(setf (get peop_extract::States :md5sum-) "e365334b2994db104733260f8d214b10")
(setf (get peop_extract::States :datatype-) "peop_extract/States")
(setf (get peop_extract::States :definition-)
      "string state
string state_karugamo
string state_collision
string state_danger
string state_costmap
string state_manual
string state_scan
string state_load
string state_shelf
float32 costmap
float32 side_joystick
float32 ctrl_front
float32 ctrl_side
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



(provide :peop_extract/States "e365334b2994db104733260f8d214b10")


