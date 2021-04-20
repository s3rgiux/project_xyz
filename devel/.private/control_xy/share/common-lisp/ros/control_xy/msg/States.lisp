; Auto-generated. Do not edit!


(cl:in-package control_xy-msg)


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
   (state_load
    :reader state_load
    :initarg :state_load
    :type cl:string
    :initform "")
   (state_shelf
    :reader state_shelf
    :initarg :state_shelf
    :type cl:string
    :initform "")
   (costmap
    :reader costmap
    :initarg :costmap
    :type cl:float
    :initform 0.0)
   (side_joystick
    :reader side_joystick
    :initarg :side_joystick
    :type cl:float
    :initform 0.0)
   (ctrl_front
    :reader ctrl_front
    :initarg :ctrl_front
    :type cl:float
    :initform 0.0)
   (ctrl_side
    :reader ctrl_side
    :initarg :ctrl_side
    :type cl:float
    :initform 0.0)
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
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name control_xy-msg:<States> is deprecated: use control_xy-msg:States instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:state-val is deprecated.  Use control_xy-msg:state instead.")
  (state m))

(cl:ensure-generic-function 'state_karugamo-val :lambda-list '(m))
(cl:defmethod state_karugamo-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:state_karugamo-val is deprecated.  Use control_xy-msg:state_karugamo instead.")
  (state_karugamo m))

(cl:ensure-generic-function 'state_collision-val :lambda-list '(m))
(cl:defmethod state_collision-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:state_collision-val is deprecated.  Use control_xy-msg:state_collision instead.")
  (state_collision m))

(cl:ensure-generic-function 'state_danger-val :lambda-list '(m))
(cl:defmethod state_danger-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:state_danger-val is deprecated.  Use control_xy-msg:state_danger instead.")
  (state_danger m))

(cl:ensure-generic-function 'state_costmap-val :lambda-list '(m))
(cl:defmethod state_costmap-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:state_costmap-val is deprecated.  Use control_xy-msg:state_costmap instead.")
  (state_costmap m))

(cl:ensure-generic-function 'state_manual-val :lambda-list '(m))
(cl:defmethod state_manual-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:state_manual-val is deprecated.  Use control_xy-msg:state_manual instead.")
  (state_manual m))

(cl:ensure-generic-function 'state_scan-val :lambda-list '(m))
(cl:defmethod state_scan-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:state_scan-val is deprecated.  Use control_xy-msg:state_scan instead.")
  (state_scan m))

(cl:ensure-generic-function 'state_load-val :lambda-list '(m))
(cl:defmethod state_load-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:state_load-val is deprecated.  Use control_xy-msg:state_load instead.")
  (state_load m))

(cl:ensure-generic-function 'state_shelf-val :lambda-list '(m))
(cl:defmethod state_shelf-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:state_shelf-val is deprecated.  Use control_xy-msg:state_shelf instead.")
  (state_shelf m))

(cl:ensure-generic-function 'costmap-val :lambda-list '(m))
(cl:defmethod costmap-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:costmap-val is deprecated.  Use control_xy-msg:costmap instead.")
  (costmap m))

(cl:ensure-generic-function 'side_joystick-val :lambda-list '(m))
(cl:defmethod side_joystick-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:side_joystick-val is deprecated.  Use control_xy-msg:side_joystick instead.")
  (side_joystick m))

(cl:ensure-generic-function 'ctrl_front-val :lambda-list '(m))
(cl:defmethod ctrl_front-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:ctrl_front-val is deprecated.  Use control_xy-msg:ctrl_front instead.")
  (ctrl_front m))

(cl:ensure-generic-function 'ctrl_side-val :lambda-list '(m))
(cl:defmethod ctrl_side-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:ctrl_side-val is deprecated.  Use control_xy-msg:ctrl_side instead.")
  (ctrl_side m))

(cl:ensure-generic-function 'trackeds-val :lambda-list '(m))
(cl:defmethod trackeds-val ((m <States>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader control_xy-msg:trackeds-val is deprecated.  Use control_xy-msg:trackeds instead.")
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
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_load))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_load))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_shelf))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_shelf))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'costmap))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'side_joystick))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'ctrl_front))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'ctrl_side))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
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
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_load) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_load) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_shelf) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_shelf) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'costmap) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'side_joystick) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ctrl_front) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ctrl_side) (roslisp-utils:decode-single-float-bits bits)))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'trackeds) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<States>)))
  "Returns string type for a message object of type '<States>"
  "control_xy/States")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'States)))
  "Returns string type for a message object of type 'States"
  "control_xy/States")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<States>)))
  "Returns md5sum for a message object of type '<States>"
  "e365334b2994db104733260f8d214b10")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'States)))
  "Returns md5sum for a message object of type 'States"
  "e365334b2994db104733260f8d214b10")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<States>)))
  "Returns full string definition for message of type '<States>"
  (cl:format cl:nil "string state~%string state_karugamo~%string state_collision~%string state_danger~%string state_costmap~%string state_manual~%string state_scan~%string state_load~%string state_shelf~%float32 costmap~%float32 side_joystick~%float32 ctrl_front~%float32 ctrl_side~%geometry_msgs/Twist trackeds~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'States)))
  "Returns full string definition for message of type 'States"
  (cl:format cl:nil "string state~%string state_karugamo~%string state_collision~%string state_danger~%string state_costmap~%string state_manual~%string state_scan~%string state_load~%string state_shelf~%float32 costmap~%float32 side_joystick~%float32 ctrl_front~%float32 ctrl_side~%geometry_msgs/Twist trackeds~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <States>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'state))
     4 (cl:length (cl:slot-value msg 'state_karugamo))
     4 (cl:length (cl:slot-value msg 'state_collision))
     4 (cl:length (cl:slot-value msg 'state_danger))
     4 (cl:length (cl:slot-value msg 'state_costmap))
     4 (cl:length (cl:slot-value msg 'state_manual))
     4 (cl:length (cl:slot-value msg 'state_scan))
     4 (cl:length (cl:slot-value msg 'state_load))
     4 (cl:length (cl:slot-value msg 'state_shelf))
     4
     4
     4
     4
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
    (cl:cons ':state_load (state_load msg))
    (cl:cons ':state_shelf (state_shelf msg))
    (cl:cons ':costmap (costmap msg))
    (cl:cons ':side_joystick (side_joystick msg))
    (cl:cons ':ctrl_front (ctrl_front msg))
    (cl:cons ':ctrl_side (ctrl_side msg))
    (cl:cons ':trackeds (trackeds msg))
))
