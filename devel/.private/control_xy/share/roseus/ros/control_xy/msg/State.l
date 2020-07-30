;; Auto-generated. Do not edit!


(when (boundp 'control_xy::State)
  (if (not (find-package "CONTROL_XY"))
    (make-package "CONTROL_XY"))
  (shadow 'State (find-package "CONTROL_XY")))
(unless (find-package "CONTROL_XY::STATE")
  (make-package "CONTROL_XY::STATE"))

(in-package "ROS")
;;//! \htmlinclude State.msg.html


(intern "*STATE_SHUTDOWN*" (find-package "CONTROL_XY::STATE"))
(shadow '*STATE_SHUTDOWN* (find-package "CONTROL_XY::STATE"))
(defconstant control_xy::State::*STATE_SHUTDOWN* "SHUTDOWN")
(intern "*STATE_IDLE*" (find-package "CONTROL_XY::STATE"))
(shadow '*STATE_IDLE* (find-package "CONTROL_XY::STATE"))
(defconstant control_xy::State::*STATE_IDLE* "IDLE")
(intern "*STATE_ACTIVE_KARUGAMO*" (find-package "CONTROL_XY::STATE"))
(shadow '*STATE_ACTIVE_KARUGAMO* (find-package "CONTROL_XY::STATE"))
(defconstant control_xy::State::*STATE_ACTIVE_KARUGAMO* "ACTIVE_KARUGAMO")
(intern "*STATE_ACTIVE_MANUAL*" (find-package "CONTROL_XY::STATE"))
(shadow '*STATE_ACTIVE_MANUAL* (find-package "CONTROL_XY::STATE"))
(defconstant control_xy::State::*STATE_ACTIVE_MANUAL* "ACTIVE_MANUAL")
(intern "*STATE_ERROR_OBSTACLE*" (find-package "CONTROL_XY::STATE"))
(shadow '*STATE_ERROR_OBSTACLE* (find-package "CONTROL_XY::STATE"))
(defconstant control_xy::State::*STATE_ERROR_OBSTACLE* "ERROR_OBSTACLE")
(intern "*STATE_ERROR_COLLISION*" (find-package "CONTROL_XY::STATE"))
(shadow '*STATE_ERROR_COLLISION* (find-package "CONTROL_XY::STATE"))
(defconstant control_xy::State::*STATE_ERROR_COLLISION* "ERROR_COLLISION")
(defclass control_xy::State
  :super ros::object
  :slots (_state ))

(defmethod control_xy::State
  (:init
   (&key
    ((:state __state) "")
    )
   (send-super :init)
   (setq _state (string __state))
   self)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:serialization-length
   ()
   (+
    ;; string _state
    4 (length _state)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _state
       (write-long (length _state) s) (princ _state s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _state
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get control_xy::State :md5sum-) "1d1d2a87dda45fe2cfd2df8cea1145d9")
(setf (get control_xy::State :datatype-) "control_xy/State")
(setf (get control_xy::State :definition-)
      "# シャットダウン（非通電）
string STATE_SHUTDOWN = SHUTDOWN
# アイドル状態
string STATE_IDLE = IDLE
# 動作アクティブ:カルガモ
string STATE_ACTIVE_KARUGAMO = ACTIVE_KARUGAMO
# 動作アクティブ:マニュアル
string STATE_ACTIVE_MANUAL = ACTIVE_MANUAL
# エラー:近傍に障害物あり
string STATE_ERROR_OBSTACLE = ERROR_OBSTACLE
# エラー:ガードバンパー衝突検知
string STATE_ERROR_COLLISION = ERROR_COLLISION

string state
")



(provide :control_xy/State "1d1d2a87dda45fe2cfd2df8cea1145d9")


