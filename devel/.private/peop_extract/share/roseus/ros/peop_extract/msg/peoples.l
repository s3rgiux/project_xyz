;; Auto-generated. Do not edit!


(when (boundp 'peop_extract::peoples)
  (if (not (find-package "PEOP_EXTRACT"))
    (make-package "PEOP_EXTRACT"))
  (shadow 'peoples (find-package "PEOP_EXTRACT")))
(unless (find-package "PEOP_EXTRACT::PEOPLES")
  (make-package "PEOP_EXTRACT::PEOPLES"))

(in-package "ROS")
;;//! \htmlinclude peoples.msg.html


(defclass peop_extract::peoples
  :super ros::object
  :slots (_people ))

(defmethod peop_extract::peoples
  (:init
   (&key
    ((:people __people) (let (r) (dotimes (i 0) (push (instance peop_extract::people_box :init) r)) r))
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
    ;; peop_extract/people_box[] _people
    (apply #'+ (send-all _people :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; peop_extract/people_box[] _people
     (write-long (length _people) s)
     (dolist (elem _people)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; peop_extract/people_box[] _people
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _people (let (r) (dotimes (i n) (push (instance peop_extract::people_box :init) r)) r))
     (dolist (elem- _people)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get peop_extract::peoples :md5sum-) "ac59fff88e12974eb0b8f05308bead2c")
(setf (get peop_extract::peoples :datatype-) "peop_extract/peoples")
(setf (get peop_extract::peoples :definition-)
      "peop_extract/people_box[] people

================================================================================
MSG: peop_extract/people_box
int16 xmin
int16 ymin
int16 xmax
int16 ymax
int16 id
int16 area

")



(provide :peop_extract/peoples "ac59fff88e12974eb0b8f05308bead2c")


