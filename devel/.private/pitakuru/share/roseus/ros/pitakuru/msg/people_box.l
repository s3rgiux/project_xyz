;; Auto-generated. Do not edit!


(when (boundp 'pitakuru::people_box)
  (if (not (find-package "PITAKURU"))
    (make-package "PITAKURU"))
  (shadow 'people_box (find-package "PITAKURU")))
(unless (find-package "PITAKURU::PEOPLE_BOX")
  (make-package "PITAKURU::PEOPLE_BOX"))

(in-package "ROS")
;;//! \htmlinclude people_box.msg.html


(defclass pitakuru::people_box
  :super ros::object
  :slots (_xmin _ymin _xmax _ymax _id _area ))

(defmethod pitakuru::people_box
  (:init
   (&key
    ((:xmin __xmin) 0)
    ((:ymin __ymin) 0)
    ((:xmax __xmax) 0)
    ((:ymax __ymax) 0)
    ((:id __id) 0)
    ((:area __area) 0)
    )
   (send-super :init)
   (setq _xmin (round __xmin))
   (setq _ymin (round __ymin))
   (setq _xmax (round __xmax))
   (setq _ymax (round __ymax))
   (setq _id (round __id))
   (setq _area (round __area))
   self)
  (:xmin
   (&optional __xmin)
   (if __xmin (setq _xmin __xmin)) _xmin)
  (:ymin
   (&optional __ymin)
   (if __ymin (setq _ymin __ymin)) _ymin)
  (:xmax
   (&optional __xmax)
   (if __xmax (setq _xmax __xmax)) _xmax)
  (:ymax
   (&optional __ymax)
   (if __ymax (setq _ymax __ymax)) _ymax)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:area
   (&optional __area)
   (if __area (setq _area __area)) _area)
  (:serialization-length
   ()
   (+
    ;; int16 _xmin
    2
    ;; int16 _ymin
    2
    ;; int16 _xmax
    2
    ;; int16 _ymax
    2
    ;; int16 _id
    2
    ;; int16 _area
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _xmin
       (write-word _xmin s)
     ;; int16 _ymin
       (write-word _ymin s)
     ;; int16 _xmax
       (write-word _xmax s)
     ;; int16 _ymax
       (write-word _ymax s)
     ;; int16 _id
       (write-word _id s)
     ;; int16 _area
       (write-word _area s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _xmin
     (setq _xmin (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _ymin
     (setq _ymin (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _xmax
     (setq _xmax (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _ymax
     (setq _ymax (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _id
     (setq _id (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _area
     (setq _area (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get pitakuru::people_box :md5sum-) "a1e020b78ba46ecabab0208c9a5a82d9")
(setf (get pitakuru::people_box :datatype-) "pitakuru/people_box")
(setf (get pitakuru::people_box :definition-)
      "int16 xmin
int16 ymin
int16 xmax
int16 ymax
int16 id
int16 area

")



(provide :pitakuru/people_box "a1e020b78ba46ecabab0208c9a5a82d9")


