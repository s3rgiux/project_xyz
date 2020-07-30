; Auto-generated. Do not edit!


(cl:in-package pitakuru-msg)


;//! \htmlinclude State.msg.html

(cl:defclass <State> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type cl:string
    :initform ""))
)

(cl:defclass State (<State>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <State>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'State)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pitakuru-msg:<State> is deprecated: use pitakuru-msg:State instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <State>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pitakuru-msg:state-val is deprecated.  Use pitakuru-msg:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<State>)))
    "Constants for message type '<State>"
  '((:STATE_SHUTDOWN . SHUTDOWN)
    (:STATE_IDLE . IDLE)
    (:STATE_ACTIVE_KARUGAMO . ACTIVE_KARUGAMO)
    (:STATE_ACTIVE_MANUAL . ACTIVE_MANUAL)
    (:STATE_ERROR_OBSTACLE . ERROR_OBSTACLE)
    (:STATE_ERROR_COLLISION . ERROR_COLLISION))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'State)))
    "Constants for message type 'State"
  '((:STATE_SHUTDOWN . SHUTDOWN)
    (:STATE_IDLE . IDLE)
    (:STATE_ACTIVE_KARUGAMO . ACTIVE_KARUGAMO)
    (:STATE_ACTIVE_MANUAL . ACTIVE_MANUAL)
    (:STATE_ERROR_OBSTACLE . ERROR_OBSTACLE)
    (:STATE_ERROR_COLLISION . ERROR_COLLISION))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <State>) ostream)
  "Serializes a message object of type '<State>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <State>) istream)
  "Deserializes a message object of type '<State>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<State>)))
  "Returns string type for a message object of type '<State>"
  "pitakuru/State")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'State)))
  "Returns string type for a message object of type 'State"
  "pitakuru/State")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<State>)))
  "Returns md5sum for a message object of type '<State>"
  "1d1d2a87dda45fe2cfd2df8cea1145d9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'State)))
  "Returns md5sum for a message object of type 'State"
  "1d1d2a87dda45fe2cfd2df8cea1145d9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<State>)))
  "Returns full string definition for message of type '<State>"
  (cl:format cl:nil "# シャットダウン（非通電）~%string STATE_SHUTDOWN = SHUTDOWN~%# アイドル状態~%string STATE_IDLE = IDLE~%# 動作アクティブ:カルガモ~%string STATE_ACTIVE_KARUGAMO = ACTIVE_KARUGAMO~%# 動作アクティブ:マニュアル~%string STATE_ACTIVE_MANUAL = ACTIVE_MANUAL~%# エラー:近傍に障害物あり~%string STATE_ERROR_OBSTACLE = ERROR_OBSTACLE~%# エラー:ガードバンパー衝突検知~%string STATE_ERROR_COLLISION = ERROR_COLLISION~%~%string state~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'State)))
  "Returns full string definition for message of type 'State"
  (cl:format cl:nil "# シャットダウン（非通電）~%string STATE_SHUTDOWN = SHUTDOWN~%# アイドル状態~%string STATE_IDLE = IDLE~%# 動作アクティブ:カルガモ~%string STATE_ACTIVE_KARUGAMO = ACTIVE_KARUGAMO~%# 動作アクティブ:マニュアル~%string STATE_ACTIVE_MANUAL = ACTIVE_MANUAL~%# エラー:近傍に障害物あり~%string STATE_ERROR_OBSTACLE = ERROR_OBSTACLE~%# エラー:ガードバンパー衝突検知~%string STATE_ERROR_COLLISION = ERROR_COLLISION~%~%string state~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <State>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'state))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <State>))
  "Converts a ROS message object to a list"
  (cl:list 'State
    (cl:cons ':state (state msg))
))
