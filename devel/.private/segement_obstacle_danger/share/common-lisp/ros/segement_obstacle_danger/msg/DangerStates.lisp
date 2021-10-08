; Auto-generated. Do not edit!


(cl:in-package segement_obstacle_danger-msg)


;//! \htmlinclude DangerStates.msg.html

(cl:defclass <DangerStates> (roslisp-msg-protocol:ros-message)
  ((state_forward_circle
    :reader state_forward_circle
    :initarg :state_forward_circle
    :type cl:string
    :initform "")
   (state_backward_circle
    :reader state_backward_circle
    :initarg :state_backward_circle
    :type cl:string
    :initform "")
   (state_forward_segment
    :reader state_forward_segment
    :initarg :state_forward_segment
    :type cl:string
    :initform "")
   (state_backward_segment
    :reader state_backward_segment
    :initarg :state_backward_segment
    :type cl:string
    :initform ""))
)

(cl:defclass DangerStates (<DangerStates>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DangerStates>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DangerStates)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name segement_obstacle_danger-msg:<DangerStates> is deprecated: use segement_obstacle_danger-msg:DangerStates instead.")))

(cl:ensure-generic-function 'state_forward_circle-val :lambda-list '(m))
(cl:defmethod state_forward_circle-val ((m <DangerStates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader segement_obstacle_danger-msg:state_forward_circle-val is deprecated.  Use segement_obstacle_danger-msg:state_forward_circle instead.")
  (state_forward_circle m))

(cl:ensure-generic-function 'state_backward_circle-val :lambda-list '(m))
(cl:defmethod state_backward_circle-val ((m <DangerStates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader segement_obstacle_danger-msg:state_backward_circle-val is deprecated.  Use segement_obstacle_danger-msg:state_backward_circle instead.")
  (state_backward_circle m))

(cl:ensure-generic-function 'state_forward_segment-val :lambda-list '(m))
(cl:defmethod state_forward_segment-val ((m <DangerStates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader segement_obstacle_danger-msg:state_forward_segment-val is deprecated.  Use segement_obstacle_danger-msg:state_forward_segment instead.")
  (state_forward_segment m))

(cl:ensure-generic-function 'state_backward_segment-val :lambda-list '(m))
(cl:defmethod state_backward_segment-val ((m <DangerStates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader segement_obstacle_danger-msg:state_backward_segment-val is deprecated.  Use segement_obstacle_danger-msg:state_backward_segment instead.")
  (state_backward_segment m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<DangerStates>)))
    "Constants for message type '<DangerStates>"
  '((:DANGER . Danger)
    (:CLEAR . Clear))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'DangerStates)))
    "Constants for message type 'DangerStates"
  '((:DANGER . Danger)
    (:CLEAR . Clear))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DangerStates>) ostream)
  "Serializes a message object of type '<DangerStates>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_forward_circle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_forward_circle))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_backward_circle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_backward_circle))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_forward_segment))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_forward_segment))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_backward_segment))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_backward_segment))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DangerStates>) istream)
  "Deserializes a message object of type '<DangerStates>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_forward_circle) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_forward_circle) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_backward_circle) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_backward_circle) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_forward_segment) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_forward_segment) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_backward_segment) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_backward_segment) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DangerStates>)))
  "Returns string type for a message object of type '<DangerStates>"
  "segement_obstacle_danger/DangerStates")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DangerStates)))
  "Returns string type for a message object of type 'DangerStates"
  "segement_obstacle_danger/DangerStates")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DangerStates>)))
  "Returns md5sum for a message object of type '<DangerStates>"
  "725ae9e90d4c8165163e7e160cab8649")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DangerStates)))
  "Returns md5sum for a message object of type 'DangerStates"
  "725ae9e90d4c8165163e7e160cab8649")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DangerStates>)))
  "Returns full string definition for message of type '<DangerStates>"
  (cl:format cl:nil "string state_forward_circle~%string state_backward_circle~%string state_forward_segment~%string state_backward_segment~%~%string DANGER = Danger~%string CLEAR = Clear~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DangerStates)))
  "Returns full string definition for message of type 'DangerStates"
  (cl:format cl:nil "string state_forward_circle~%string state_backward_circle~%string state_forward_segment~%string state_backward_segment~%~%string DANGER = Danger~%string CLEAR = Clear~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DangerStates>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'state_forward_circle))
     4 (cl:length (cl:slot-value msg 'state_backward_circle))
     4 (cl:length (cl:slot-value msg 'state_forward_segment))
     4 (cl:length (cl:slot-value msg 'state_backward_segment))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DangerStates>))
  "Converts a ROS message object to a list"
  (cl:list 'DangerStates
    (cl:cons ':state_forward_circle (state_forward_circle msg))
    (cl:cons ':state_backward_circle (state_backward_circle msg))
    (cl:cons ':state_forward_segment (state_forward_segment msg))
    (cl:cons ':state_backward_segment (state_backward_segment msg))
))
