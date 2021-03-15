;; Auto-generated. Do not edit!


(when (boundp 'control_xy::States)
  (if (not (find-package "CONTROL_XY"))
    (make-package "CONTROL_XY"))
  (shadow 'States (find-package "CONTROL_XY")))
(unless (find-package "CONTROL_XY::STATES")
  (make-package "CONTROL_XY::STATES"))

(in-package "ROS")
;;//! \htmlinclude States.msg.html


(defclass control_xy::States
  :super ros::object
  :slots (_state _state_karugamo _state_collision _state_danger _state_costmap ))

(defmethod control_xy::States
  (:init
   (&key
    ((:state __state) "")
    ((:state_karugamo __state_karugamo) "")
    ((:state_collision __state_collision) "")
    ((:state_danger __state_danger) "")
    ((:state_costmap __state_costmap) "")
    )
   (send-super :init)
   (setq _state (string __state))
   (setq _state_karugamo (string __state_karugamo))
   (setq _state_collision (string __state_collision))
   (setq _state_danger (string __state_danger))
   (setq _state_costmap (string __state_costmap))
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
   ;;
   self)
  )

(setf (get control_xy::States :md5sum-) "a970e58c537add5954e8c37ff3305a1c")
(setf (get control_xy::States :datatype-) "control_xy/States")
(setf (get control_xy::States :definition-)
      "string state
string state_karugamo
string state_collision
string state_danger
string state_costmap


")



(provide :control_xy/States "a970e58c537add5954e8c37ff3305a1c")


