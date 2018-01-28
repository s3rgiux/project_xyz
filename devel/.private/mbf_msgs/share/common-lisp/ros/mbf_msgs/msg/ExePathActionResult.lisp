; Auto-generated. Do not edit!


(cl:in-package mbf_msgs-msg)


;//! \htmlinclude ExePathActionResult.msg.html

(cl:defclass <ExePathActionResult> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (status
    :reader status
    :initarg :status
    :type actionlib_msgs-msg:GoalStatus
    :initform (cl:make-instance 'actionlib_msgs-msg:GoalStatus))
   (result
    :reader result
    :initarg :result
    :type mbf_msgs-msg:ExePathResult
    :initform (cl:make-instance 'mbf_msgs-msg:ExePathResult)))
)

(cl:defclass ExePathActionResult (<ExePathActionResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ExePathActionResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ExePathActionResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mbf_msgs-msg:<ExePathActionResult> is deprecated: use mbf_msgs-msg:ExePathActionResult instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ExePathActionResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mbf_msgs-msg:header-val is deprecated.  Use mbf_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <ExePathActionResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mbf_msgs-msg:status-val is deprecated.  Use mbf_msgs-msg:status instead.")
  (status m))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <ExePathActionResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mbf_msgs-msg:result-val is deprecated.  Use mbf_msgs-msg:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ExePathActionResult>) ostream)
  "Serializes a message object of type '<ExePathActionResult>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'status) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'result) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ExePathActionResult>) istream)
  "Deserializes a message object of type '<ExePathActionResult>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'status) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'result) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ExePathActionResult>)))
  "Returns string type for a message object of type '<ExePathActionResult>"
  "mbf_msgs/ExePathActionResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ExePathActionResult)))
  "Returns string type for a message object of type 'ExePathActionResult"
  "mbf_msgs/ExePathActionResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ExePathActionResult>)))
  "Returns md5sum for a message object of type '<ExePathActionResult>"
  "c0c371e6e71c834fcf0eea1b2ae047b5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ExePathActionResult)))
  "Returns md5sum for a message object of type 'ExePathActionResult"
  "c0c371e6e71c834fcf0eea1b2ae047b5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ExePathActionResult>)))
  "Returns full string definition for message of type '<ExePathActionResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%ExePathResult result~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: mbf_msgs/ExePathResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%# Predefined success codes:~%uint8 SUCCESS         = 0~%# 1..9 are reserved as plugin specific non-error results~%~%# Predefined error codes:~%uint8 FAILURE         = 100  # Unspecified failure, only used for old, non-mfb_core based plugins~%uint8 CANCELED        = 101~%uint8 NO_VALID_CMD    = 102~%uint8 PAT_EXCEEDED    = 103~%uint8 COLLISION       = 104~%uint8 OSCILLATION     = 105~%uint8 ROBOT_STUCK     = 106~%uint8 MISSED_GOAL     = 107~%uint8 MISSED_PATH     = 108~%uint8 BLOCKED_PATH    = 109~%uint8 INVALID_PATH    = 110~%uint8 TF_ERROR        = 111~%uint8 NOT_INITIALIZED = 112~%uint8 INVALID_PLUGIN  = 113~%uint8 INTERNAL_ERROR  = 114~%uint8 OUT_OF_MAP      = 115  # The start and / or the goal are outside the map~%uint8 MAP_ERROR       = 116  # The map is not running properly~%uint8 STOPPED         = 117  # The controller execution has been stopped rigorously.~%~%# 121..149 are reserved as plugin specific errors~%~%uint32 outcome~%string message~%~%geometry_msgs/PoseStamped  final_pose~%float32 dist_to_goal~%float32 angle_to_goal~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ExePathActionResult)))
  "Returns full string definition for message of type 'ExePathActionResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%ExePathResult result~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: mbf_msgs/ExePathResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%# Predefined success codes:~%uint8 SUCCESS         = 0~%# 1..9 are reserved as plugin specific non-error results~%~%# Predefined error codes:~%uint8 FAILURE         = 100  # Unspecified failure, only used for old, non-mfb_core based plugins~%uint8 CANCELED        = 101~%uint8 NO_VALID_CMD    = 102~%uint8 PAT_EXCEEDED    = 103~%uint8 COLLISION       = 104~%uint8 OSCILLATION     = 105~%uint8 ROBOT_STUCK     = 106~%uint8 MISSED_GOAL     = 107~%uint8 MISSED_PATH     = 108~%uint8 BLOCKED_PATH    = 109~%uint8 INVALID_PATH    = 110~%uint8 TF_ERROR        = 111~%uint8 NOT_INITIALIZED = 112~%uint8 INVALID_PLUGIN  = 113~%uint8 INTERNAL_ERROR  = 114~%uint8 OUT_OF_MAP      = 115  # The start and / or the goal are outside the map~%uint8 MAP_ERROR       = 116  # The map is not running properly~%uint8 STOPPED         = 117  # The controller execution has been stopped rigorously.~%~%# 121..149 are reserved as plugin specific errors~%~%uint32 outcome~%string message~%~%geometry_msgs/PoseStamped  final_pose~%float32 dist_to_goal~%float32 angle_to_goal~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ExePathActionResult>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'status))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'result))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ExePathActionResult>))
  "Converts a ROS message object to a list"
  (cl:list 'ExePathActionResult
    (cl:cons ':header (header msg))
    (cl:cons ':status (status msg))
    (cl:cons ':result (result msg))
))
