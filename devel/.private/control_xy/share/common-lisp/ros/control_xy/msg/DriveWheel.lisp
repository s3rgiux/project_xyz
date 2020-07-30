; Auto-generated. Do not edit!


(cl:in-package control_xy-msg)


;//! \htmlinclude DriveWheel.msg.html

(cl:defclass <DriveWheel> (roslisp-msg-protocol:ros-message)
  ((left_rpm
    :reader left_rpm
    :initarg :left_rpm
    :type cl:float
    :initform 0.0)
   (right_rpm
    :reader right_rpm
    :initarg :right_rpm
    :type cl:float
    :initform 0.0))
)

(cl:defclass DriveWheel (<DriveWheel>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DriveWheel>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DriveWheel)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name control_xy-msg:<DriveWheel> is deprecated: use control_xy-msg:DriveWheel instead.")))

(cl:ensure-generic-function 'left_rpm-val :lambda-list '(m))
(cl:defmethod left_rpm-val ((m <DriveWheel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:left_rpm-val is deprecated.  Use control_xy-msg:left_rpm instead.")
  (left_rpm m))

(cl:ensure-generic-function 'right_rpm-val :lambda-list '(m))
(cl:defmethod right_rpm-val ((m <DriveWheel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:right_rpm-val is deprecated.  Use control_xy-msg:right_rpm instead.")
  (right_rpm m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DriveWheel>) ostream)
  "Serializes a message object of type '<DriveWheel>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'left_rpm))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'right_rpm))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DriveWheel>) istream)
  "Deserializes a message object of type '<DriveWheel>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'left_rpm) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'right_rpm) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DriveWheel>)))
  "Returns string type for a message object of type '<DriveWheel>"
  "control_xy/DriveWheel")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DriveWheel)))
  "Returns string type for a message object of type 'DriveWheel"
  "control_xy/DriveWheel")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DriveWheel>)))
  "Returns md5sum for a message object of type '<DriveWheel>"
  "fb0186777139ed5386fa80048788f9b4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DriveWheel)))
  "Returns md5sum for a message object of type 'DriveWheel"
  "fb0186777139ed5386fa80048788f9b4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DriveWheel>)))
  "Returns full string definition for message of type '<DriveWheel>"
  (cl:format cl:nil "float32 left_rpm~%float32 right_rpm~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DriveWheel)))
  "Returns full string definition for message of type 'DriveWheel"
  (cl:format cl:nil "float32 left_rpm~%float32 right_rpm~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DriveWheel>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DriveWheel>))
  "Converts a ROS message object to a list"
  (cl:list 'DriveWheel
    (cl:cons ':left_rpm (left_rpm msg))
    (cl:cons ':right_rpm (right_rpm msg))
))
