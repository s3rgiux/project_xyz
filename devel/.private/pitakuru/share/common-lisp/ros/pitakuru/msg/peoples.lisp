; Auto-generated. Do not edit!


(cl:in-package pitakuru-msg)


;//! \htmlinclude peoples.msg.html

(cl:defclass <peoples> (roslisp-msg-protocol:ros-message)
  ((people
    :reader people
    :initarg :people
    :type (cl:vector pitakuru-msg:people_box)
   :initform (cl:make-array 0 :element-type 'pitakuru-msg:people_box :initial-element (cl:make-instance 'pitakuru-msg:people_box))))
)

(cl:defclass peoples (<peoples>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <peoples>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'peoples)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pitakuru-msg:<peoples> is deprecated: use pitakuru-msg:peoples instead.")))

(cl:ensure-generic-function 'people-val :lambda-list '(m))
(cl:defmethod people-val ((m <peoples>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pitakuru-msg:people-val is deprecated.  Use pitakuru-msg:people instead.")
  (people m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <peoples>) ostream)
  "Serializes a message object of type '<peoples>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'people))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'people))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <peoples>) istream)
  "Deserializes a message object of type '<peoples>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'people) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'people)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'pitakuru-msg:people_box))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<peoples>)))
  "Returns string type for a message object of type '<peoples>"
  "pitakuru/peoples")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'peoples)))
  "Returns string type for a message object of type 'peoples"
  "pitakuru/peoples")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<peoples>)))
  "Returns md5sum for a message object of type '<peoples>"
  "ac59fff88e12974eb0b8f05308bead2c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'peoples)))
  "Returns md5sum for a message object of type 'peoples"
  "ac59fff88e12974eb0b8f05308bead2c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<peoples>)))
  "Returns full string definition for message of type '<peoples>"
  (cl:format cl:nil "pitakuru/people_box[] people~%~%================================================================================~%MSG: pitakuru/people_box~%int16 xmin~%int16 ymin~%int16 xmax~%int16 ymax~%int16 id~%int16 area~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'peoples)))
  "Returns full string definition for message of type 'peoples"
  (cl:format cl:nil "pitakuru/people_box[] people~%~%================================================================================~%MSG: pitakuru/people_box~%int16 xmin~%int16 ymin~%int16 xmax~%int16 ymax~%int16 id~%int16 area~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <peoples>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'people) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <peoples>))
  "Converts a ROS message object to a list"
  (cl:list 'peoples
    (cl:cons ':people (people msg))
))
