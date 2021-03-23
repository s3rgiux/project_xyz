; Auto-generated. Do not edit!


(cl:in-package sort_track-msg)


;//! \htmlinclude people_box.msg.html

(cl:defclass <people_box> (roslisp-msg-protocol:ros-message)
  ((xmin
    :reader xmin
    :initarg :xmin
    :type cl:fixnum
    :initform 0)
   (ymin
    :reader ymin
    :initarg :ymin
    :type cl:fixnum
    :initform 0)
   (xmax
    :reader xmax
    :initarg :xmax
    :type cl:fixnum
    :initform 0)
   (ymax
    :reader ymax
    :initarg :ymax
    :type cl:fixnum
    :initform 0)
   (id
    :reader id
    :initarg :id
    :type cl:fixnum
    :initform 0)
   (area
    :reader area
    :initarg :area
    :type cl:fixnum
    :initform 0))
)

(cl:defclass people_box (<people_box>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <people_box>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'people_box)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sort_track-msg:<people_box> is deprecated: use sort_track-msg:people_box instead.")))

(cl:ensure-generic-function 'xmin-val :lambda-list '(m))
(cl:defmethod xmin-val ((m <people_box>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sort_track-msg:xmin-val is deprecated.  Use sort_track-msg:xmin instead.")
  (xmin m))

(cl:ensure-generic-function 'ymin-val :lambda-list '(m))
(cl:defmethod ymin-val ((m <people_box>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sort_track-msg:ymin-val is deprecated.  Use sort_track-msg:ymin instead.")
  (ymin m))

(cl:ensure-generic-function 'xmax-val :lambda-list '(m))
(cl:defmethod xmax-val ((m <people_box>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sort_track-msg:xmax-val is deprecated.  Use sort_track-msg:xmax instead.")
  (xmax m))

(cl:ensure-generic-function 'ymax-val :lambda-list '(m))
(cl:defmethod ymax-val ((m <people_box>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sort_track-msg:ymax-val is deprecated.  Use sort_track-msg:ymax instead.")
  (ymax m))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <people_box>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sort_track-msg:id-val is deprecated.  Use sort_track-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'area-val :lambda-list '(m))
(cl:defmethod area-val ((m <people_box>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sort_track-msg:area-val is deprecated.  Use sort_track-msg:area instead.")
  (area m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <people_box>) ostream)
  "Serializes a message object of type '<people_box>"
  (cl:let* ((signed (cl:slot-value msg 'xmin)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ymin)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'xmax)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'ymax)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'area)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <people_box>) istream)
  "Deserializes a message object of type '<people_box>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'xmin) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ymin) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'xmax) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ymax) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'area) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<people_box>)))
  "Returns string type for a message object of type '<people_box>"
  "sort_track/people_box")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'people_box)))
  "Returns string type for a message object of type 'people_box"
  "sort_track/people_box")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<people_box>)))
  "Returns md5sum for a message object of type '<people_box>"
  "a1e020b78ba46ecabab0208c9a5a82d9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'people_box)))
  "Returns md5sum for a message object of type 'people_box"
  "a1e020b78ba46ecabab0208c9a5a82d9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<people_box>)))
  "Returns full string definition for message of type '<people_box>"
  (cl:format cl:nil "int16 xmin~%int16 ymin~%int16 xmax~%int16 ymax~%int16 id~%int16 area~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'people_box)))
  "Returns full string definition for message of type 'people_box"
  (cl:format cl:nil "int16 xmin~%int16 ymin~%int16 xmax~%int16 ymax~%int16 id~%int16 area~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <people_box>))
  (cl:+ 0
     2
     2
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <people_box>))
  "Converts a ROS message object to a list"
  (cl:list 'people_box
    (cl:cons ':xmin (xmin msg))
    (cl:cons ':ymin (ymin msg))
    (cl:cons ':xmax (xmax msg))
    (cl:cons ':ymax (ymax msg))
    (cl:cons ':id (id msg))
    (cl:cons ':area (area msg))
))
