;; Auto-generated. Do not edit!


(when (boundp 'segement_obstacle_danger::DangerStates)
  (if (not (find-package "SEGEMENT_OBSTACLE_DANGER"))
    (make-package "SEGEMENT_OBSTACLE_DANGER"))
  (shadow 'DangerStates (find-package "SEGEMENT_OBSTACLE_DANGER")))
(unless (find-package "SEGEMENT_OBSTACLE_DANGER::DANGERSTATES")
  (make-package "SEGEMENT_OBSTACLE_DANGER::DANGERSTATES"))

(in-package "ROS")
;;//! \htmlinclude DangerStates.msg.html


(intern "*DANGER*" (find-package "SEGEMENT_OBSTACLE_DANGER::DANGERSTATES"))
(shadow '*DANGER* (find-package "SEGEMENT_OBSTACLE_DANGER::DANGERSTATES"))
(defconstant segement_obstacle_danger::DangerStates::*DANGER* "Danger")
(intern "*CLEAR*" (find-package "SEGEMENT_OBSTACLE_DANGER::DANGERSTATES"))
(shadow '*CLEAR* (find-package "SEGEMENT_OBSTACLE_DANGER::DANGERSTATES"))
(defconstant segement_obstacle_danger::DangerStates::*CLEAR* "Clear")
(defclass segement_obstacle_danger::DangerStates
  :super ros::object
  :slots (_state_forward_circle _state_backward_circle _state_forward_segment _state_backward_segment ))

(defmethod segement_obstacle_danger::DangerStates
  (:init
   (&key
    ((:state_forward_circle __state_forward_circle) "")
    ((:state_backward_circle __state_backward_circle) "")
    ((:state_forward_segment __state_forward_segment) "")
    ((:state_backward_segment __state_backward_segment) "")
    )
   (send-super :init)
   (setq _state_forward_circle (string __state_forward_circle))
   (setq _state_backward_circle (string __state_backward_circle))
   (setq _state_forward_segment (string __state_forward_segment))
   (setq _state_backward_segment (string __state_backward_segment))
   self)
  (:state_forward_circle
   (&optional __state_forward_circle)
   (if __state_forward_circle (setq _state_forward_circle __state_forward_circle)) _state_forward_circle)
  (:state_backward_circle
   (&optional __state_backward_circle)
   (if __state_backward_circle (setq _state_backward_circle __state_backward_circle)) _state_backward_circle)
  (:state_forward_segment
   (&optional __state_forward_segment)
   (if __state_forward_segment (setq _state_forward_segment __state_forward_segment)) _state_forward_segment)
  (:state_backward_segment
   (&optional __state_backward_segment)
   (if __state_backward_segment (setq _state_backward_segment __state_backward_segment)) _state_backward_segment)
  (:serialization-length
   ()
   (+
    ;; string _state_forward_circle
    4 (length _state_forward_circle)
    ;; string _state_backward_circle
    4 (length _state_backward_circle)
    ;; string _state_forward_segment
    4 (length _state_forward_segment)
    ;; string _state_backward_segment
    4 (length _state_backward_segment)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _state_forward_circle
       (write-long (length _state_forward_circle) s) (princ _state_forward_circle s)
     ;; string _state_backward_circle
       (write-long (length _state_backward_circle) s) (princ _state_backward_circle s)
     ;; string _state_forward_segment
       (write-long (length _state_forward_segment) s) (princ _state_forward_segment s)
     ;; string _state_backward_segment
       (write-long (length _state_backward_segment) s) (princ _state_backward_segment s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _state_forward_circle
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_forward_circle (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state_backward_circle
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_backward_circle (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state_forward_segment
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_forward_segment (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _state_backward_segment
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state_backward_segment (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get segement_obstacle_danger::DangerStates :md5sum-) "725ae9e90d4c8165163e7e160cab8649")
(setf (get segement_obstacle_danger::DangerStates :datatype-) "segement_obstacle_danger/DangerStates")
(setf (get segement_obstacle_danger::DangerStates :definition-)
      "string state_forward_circle
string state_backward_circle
string state_forward_segment
string state_backward_segment

string DANGER = Danger
string CLEAR = Clear
")



(provide :segement_obstacle_danger/DangerStates "725ae9e90d4c8165163e7e160cab8649")


