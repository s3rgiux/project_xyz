;; Auto-generated. Do not edit!


(when (boundp 'sort_track::peoples)
  (if (not (find-package "SORT_TRACK"))
    (make-package "SORT_TRACK"))
  (shadow 'peoples (find-package "SORT_TRACK")))
(unless (find-package "SORT_TRACK::PEOPLES")
  (make-package "SORT_TRACK::PEOPLES"))

(in-package "ROS")
;;//! \htmlinclude peoples.msg.html


(defclass sort_track::peoples
  :super ros::object
  :slots (_people ))

(defmethod sort_track::peoples
  (:init
   (&key
    ((:people __people) (let (r) (dotimes (i 0) (push (instance sort_track::people_box :init) r)) r))
    )
   (send-super :init)
   (setq _people __people)
   self)
  (:people
   (&rest __people)
   (if (keywordp (car __people))
       (send* _people __people)
     (progn
       (if __people (setq _people (car __people)))
       _people)))
  (:serialization-length
   ()
   (+
    ;; sort_track/people_box[] _people
    (apply #'+ (send-all _people :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sort_track/people_box[] _people
     (write-long (length _people) s)
     (dolist (elem _people)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sort_track/people_box[] _people
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _people (let (r) (dotimes (i n) (push (instance sort_track::people_box :init) r)) r))
     (dolist (elem- _people)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get sort_track::peoples :md5sum-) "ac59fff88e12974eb0b8f05308bead2c")
(setf (get sort_track::peoples :datatype-) "sort_track/peoples")
(setf (get sort_track::peoples :definition-)
      "sort_track/people_box[] people

================================================================================
MSG: sort_track/people_box
int16 xmin
int16 ymin
int16 xmax
int16 ymax
int16 id
int16 area

")



(provide :sort_track/peoples "ac59fff88e12974eb0b8f05308bead2c")


