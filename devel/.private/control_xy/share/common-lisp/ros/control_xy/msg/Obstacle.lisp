; Auto-generated. Do not edit!


(cl:in-package control_xy-msg)


;//! \htmlinclude Obstacle.msg.html

(cl:defclass <Obstacle> (roslisp-msg-protocol:ros-message)
  ((type
    :reader type
    :initarg :type
    :type cl:fixnum
    :initform 0)
   (angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0)
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass Obstacle (<Obstacle>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Obstacle>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Obstacle)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name control_xy-msg:<Obstacle> is deprecated: use control_xy-msg:Obstacle instead.")))

(cl:ensure-generic-function 'type-val :lambda-list '(m))
(cl:defmethod type-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:type-val is deprecated.  Use control_xy-msg:type instead.")
  (type m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:angle-val is deprecated.  Use control_xy-msg:angle instead.")
  (angle m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:distance-val is deprecated.  Use control_xy-msg:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<Obstacle>)))
    "Constants for message type '<Obstacle>"
  '((:TYPE_WARNING . 0)
    (:TYPE_DANGER . 1))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'Obstacle)))
    "Constants for message type 'Obstacle"
  '((:TYPE_WARNING . 0)
    (:TYPE_DANGER . 1))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Obstacle>) ostream)
  "Serializes a message object of type '<Obstacle>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'type)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Obstacle>) istream)
  "Deserializes a message object of type '<Obstacle>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'type)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Obstacle>)))
  "Returns string type for a message object of type '<Obstacle>"
  "control_xy/Obstacle")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Obstacle)))
  "Returns string type for a message object of type 'Obstacle"
  "control_xy/Obstacle")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Obstacle>)))
  "Returns md5sum for a message object of type '<Obstacle>"
  "63d99a9ad294899d03af106edf098ef1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Obstacle)))
  "Returns md5sum for a message object of type 'Obstacle"
  "63d99a9ad294899d03af106edf098ef1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Obstacle>)))
  "Returns full string definition for message of type '<Obstacle>"
  (cl:format cl:nil "uint8 TYPE_WARNING=0~%uint8 TYPE_DANGER=1~%uint8 type~%float32 angle~%float32 distance~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Obstacle)))
  "Returns full string definition for message of type 'Obstacle"
  (cl:format cl:nil "uint8 TYPE_WARNING=0~%uint8 TYPE_DANGER=1~%uint8 type~%float32 angle~%float32 distance~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Obstacle>))
  (cl:+ 0
     1
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Obstacle>))
  "Converts a ROS message object to a list"
  (cl:list 'Obstacle
    (cl:cons ':type (type msg))
    (cl:cons ':angle (angle msg))
    (cl:cons ':distance (distance msg))
))
