; Auto-generated. Do not edit!


(cl:in-package control_xy-msg)


;//! \htmlinclude StateWheels.msg.html

(cl:defclass <StateWheels> (roslisp-msg-protocol:ros-message)
  ((left_vel
    :reader left_vel
    :initarg :left_vel
    :type cl:float
    :initform 0.0)
   (right_vel
    :reader right_vel
    :initarg :right_vel
    :type cl:float
    :initform 0.0)
   (left_current
    :reader left_current
    :initarg :left_current
    :type cl:float
    :initform 0.0)
   (right_current
    :reader right_current
    :initarg :right_current
    :type cl:float
    :initform 0.0)
   (time_stamp
    :reader time_stamp
    :initarg :time_stamp
    :type cl:real
    :initform 0))
)

(cl:defclass StateWheels (<StateWheels>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StateWheels>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StateWheels)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name control_xy-msg:<StateWheels> is deprecated: use control_xy-msg:StateWheels instead.")))

(cl:ensure-generic-function 'left_vel-val :lambda-list '(m))
(cl:defmethod left_vel-val ((m <StateWheels>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:left_vel-val is deprecated.  Use control_xy-msg:left_vel instead.")
  (left_vel m))

(cl:ensure-generic-function 'right_vel-val :lambda-list '(m))
(cl:defmethod right_vel-val ((m <StateWheels>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:right_vel-val is deprecated.  Use control_xy-msg:right_vel instead.")
  (right_vel m))

(cl:ensure-generic-function 'left_current-val :lambda-list '(m))
(cl:defmethod left_current-val ((m <StateWheels>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:left_current-val is deprecated.  Use control_xy-msg:left_current instead.")
  (left_current m))

(cl:ensure-generic-function 'right_current-val :lambda-list '(m))
(cl:defmethod right_current-val ((m <StateWheels>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:right_current-val is deprecated.  Use control_xy-msg:right_current instead.")
  (right_current m))

(cl:ensure-generic-function 'time_stamp-val :lambda-list '(m))
(cl:defmethod time_stamp-val ((m <StateWheels>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:time_stamp-val is deprecated.  Use control_xy-msg:time_stamp instead.")
  (time_stamp m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StateWheels>) ostream)
  "Serializes a message object of type '<StateWheels>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'left_vel))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'right_vel))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'left_current))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'right_current))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'time_stamp)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'time_stamp) (cl:floor (cl:slot-value msg 'time_stamp)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StateWheels>) istream)
  "Deserializes a message object of type '<StateWheels>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'left_vel) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'right_vel) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'left_current) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'right_current) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'time_stamp) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StateWheels>)))
  "Returns string type for a message object of type '<StateWheels>"
  "control_xy/StateWheels")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StateWheels)))
  "Returns string type for a message object of type 'StateWheels"
  "control_xy/StateWheels")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StateWheels>)))
  "Returns md5sum for a message object of type '<StateWheels>"
  "fe7d42a99505b18a4db3afda942ff08d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StateWheels)))
  "Returns md5sum for a message object of type 'StateWheels"
  "fe7d42a99505b18a4db3afda942ff08d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StateWheels>)))
  "Returns full string definition for message of type '<StateWheels>"
  (cl:format cl:nil "float32 left_vel~%float32 right_vel~%float32 left_current~%float32 right_current~%time time_stamp~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StateWheels)))
  "Returns full string definition for message of type 'StateWheels"
  (cl:format cl:nil "float32 left_vel~%float32 right_vel~%float32 left_current~%float32 right_current~%time time_stamp~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StateWheels>))
  (cl:+ 0
     4
     4
     4
     4
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StateWheels>))
  "Converts a ROS message object to a list"
  (cl:list 'StateWheels
    (cl:cons ':left_vel (left_vel msg))
    (cl:cons ':right_vel (right_vel msg))
    (cl:cons ':left_current (left_current msg))
    (cl:cons ':right_current (right_current msg))
    (cl:cons ':time_stamp (time_stamp msg))
))
