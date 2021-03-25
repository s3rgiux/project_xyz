; Auto-generated. Do not edit!


(cl:in-package obs_extract-msg)


;//! \htmlinclude States.msg.html

(cl:defclass <States> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type cl:string
    :initform "")
   (state_karugamo
    :reader state_karugamo
    :initarg :state_karugamo
    :type cl:string
    :initform "")
   (state_collision
    :reader state_collision
    :initarg :state_collision
    :type cl:string
    :initform "")
   (state_danger
    :reader state_danger
    :initarg :state_danger
    :type cl:string
    :initform "")
   (state_costmap
    :reader state_costmap
    :initarg :state_costmap
    :type cl:string
    :initform "")
   (state_manual
    :reader state_manual
    :initarg :state_manual
    :type cl:string
    :initform "")
   (state_scan
    :reader state_scan
    :initarg :state_scan
    :type cl:string
    :initform "")
   (trackeds
    :reader trackeds
    :initarg :trackeds
    :type geometry_msgs-msg:Twist
    :initform (cl:make-instance 'geometry_msgs-msg:Twist)))
)

(cl:defclass States (<States>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <States>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'States)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name obs_extract-msg:<States> is deprecated: use obs_extract-msg:States instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obs_extract-msg:state-val is deprecated.  Use obs_extract-msg:state instead.")
  (state m))

(cl:ensure-generic-function 'state_karugamo-val :lambda-list '(m))
(cl:defmethod state_karugamo-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obs_extract-msg:state_karugamo-val is deprecated.  Use obs_extract-msg:state_karugamo instead.")
  (state_karugamo m))

(cl:ensure-generic-function 'state_collision-val :lambda-list '(m))
(cl:defmethod state_collision-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obs_extract-msg:state_collision-val is deprecated.  Use obs_extract-msg:state_collision instead.")
  (state_collision m))

(cl:ensure-generic-function 'state_danger-val :lambda-list '(m))
(cl:defmethod state_danger-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obs_extract-msg:state_danger-val is deprecated.  Use obs_extract-msg:state_danger instead.")
  (state_danger m))

(cl:ensure-generic-function 'state_costmap-val :lambda-list '(m))
(cl:defmethod state_costmap-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obs_extract-msg:state_costmap-val is deprecated.  Use obs_extract-msg:state_costmap instead.")
  (state_costmap m))

(cl:ensure-generic-function 'state_manual-val :lambda-list '(m))
(cl:defmethod state_manual-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obs_extract-msg:state_manual-val is deprecated.  Use obs_extract-msg:state_manual instead.")
  (state_manual m))

(cl:ensure-generic-function 'state_scan-val :lambda-list '(m))
(cl:defmethod state_scan-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obs_extract-msg:state_scan-val is deprecated.  Use obs_extract-msg:state_scan instead.")
  (state_scan m))

(cl:ensure-generic-function 'trackeds-val :lambda-list '(m))
(cl:defmethod trackeds-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader obs_extract-msg:trackeds-val is deprecated.  Use obs_extract-msg:trackeds instead.")
  (trackeds m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <States>) ostream)
  "Serializes a message object of type '<States>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_karugamo))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_karugamo))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_collision))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_collision))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_danger))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_danger))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_costmap))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_costmap))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_manual))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_manual))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_scan))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_scan))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'trackeds) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <States>) istream)
  "Deserializes a message object of type '<States>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_karugamo) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_karugamo) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_collision) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_collision) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_danger) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_danger) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_costmap) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_costmap) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_manual) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_manual) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_scan) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_scan) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'trackeds) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<States>)))
  "Returns string type for a message object of type '<States>"
  "obs_extract/States")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'States)))
  "Returns string type for a message object of type 'States"
  "obs_extract/States")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<States>)))
  "Returns md5sum for a message object of type '<States>"
  "dfd48cf7701c5d144c13acc5c8b54ec0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'States)))
  "Returns md5sum for a message object of type 'States"
  "dfd48cf7701c5d144c13acc5c8b54ec0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<States>)))
  "Returns full string definition for message of type '<States>"
  (cl:format cl:nil "string state~%string state_karugamo~%string state_collision~%string state_danger~%string state_costmap~%string state_manual~%string state_scan~%geometry_msgs/Twist trackeds~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'States)))
  "Returns full string definition for message of type 'States"
  (cl:format cl:nil "string state~%string state_karugamo~%string state_collision~%string state_danger~%string state_costmap~%string state_manual~%string state_scan~%geometry_msgs/Twist trackeds~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <States>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'state))
     4 (cl:length (cl:slot-value msg 'state_karugamo))
     4 (cl:length (cl:slot-value msg 'state_collision))
     4 (cl:length (cl:slot-value msg 'state_danger))
     4 (cl:length (cl:slot-value msg 'state_costmap))
     4 (cl:length (cl:slot-value msg 'state_manual))
     4 (cl:length (cl:slot-value msg 'state_scan))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'trackeds))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <States>))
  "Converts a ROS message object to a list"
  (cl:list 'States
    (cl:cons ':state (state msg))
    (cl:cons ':state_karugamo (state_karugamo msg))
    (cl:cons ':state_collision (state_collision msg))
    (cl:cons ':state_danger (state_danger msg))
    (cl:cons ':state_costmap (state_costmap msg))
    (cl:cons ':state_manual (state_manual msg))
    (cl:cons ':state_scan (state_scan msg))
    (cl:cons ':trackeds (trackeds msg))
))
