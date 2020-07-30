;; Auto-generated. Do not edit!


(when (boundp 'control_xy::TriggerAction)
  (if (not (find-package "CONTROL_XY"))
    (make-package "CONTROL_XY"))
  (shadow 'TriggerAction (find-package "CONTROL_XY")))
(unless (find-package "CONTROL_XY::TRIGGERACTION")
  (make-package "CONTROL_XY::TRIGGERACTION"))

(in-package "ROS")
;;//! \htmlinclude TriggerAction.msg.html


(intern "*TRIGGER_EMERGENCY_BUTTON_OFF*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_EMERGENCY_BUTTON_OFF* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_EMERGENCY_BUTTON_OFF* "emergency_button_off")
(intern "*TRIGGER_EMERGENCY_BUTTON_ON*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_EMERGENCY_BUTTON_ON* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_EMERGENCY_BUTTON_ON* "emergency_button_on")
(intern "*TRIGGER_KARUGAMO_BUTTON_ON*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_KARUGAMO_BUTTON_ON* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_KARUGAMO_BUTTON_ON* "karugamo_button_on")
(intern "*TRIGGER_REMOTE_KARUGAMO_BUTTON_ON*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_REMOTE_KARUGAMO_BUTTON_ON* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_REMOTE_KARUGAMO_BUTTON_ON* "remote_karuamo_button_on")
(intern "*TRIGGER_REMOTE_MANUAL_BUTTON_ON*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_REMOTE_MANUAL_BUTTON_ON* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_REMOTE_MANUAL_BUTTON_ON* "remote_manual_button_on")
(intern "*TRIGGER_REMOTE_IDLE_BUTTON_ON*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_REMOTE_IDLE_BUTTON_ON* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_REMOTE_IDLE_BUTTON_ON* "remote_idle_button_on")
(intern "*TRIGGER_IDLE_BUTTON_ON*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_IDLE_BUTTON_ON* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_IDLE_BUTTON_ON* "idle_button_on")
(intern "*TRIGGER_DETECT_OBSTACLE*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_DETECT_OBSTACLE* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_DETECT_OBSTACLE* "detect_obstacle")
(intern "*TRIGGER_DETECT_DANGER_OBSTACLE*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_DETECT_DANGER_OBSTACLE* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_DETECT_DANGER_OBSTACLE* "detect_danger_obstacle")
(intern "*TRIGGER_COLLISION*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_COLLISION* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_COLLISION* "collision")
(intern "*TRIGGER_BREAK_RELEASE_BUTTON_ON*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_BREAK_RELEASE_BUTTON_ON* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_BREAK_RELEASE_BUTTON_ON* "break_release_button_on")
(intern "*TRIGGER_LONG_LOST*" (find-package "CONTROL_XY::TRIGGERACTION"))
(shadow '*TRIGGER_LONG_LOST* (find-package "CONTROL_XY::TRIGGERACTION"))
(defconstant control_xy::TriggerAction::*TRIGGER_LONG_LOST* "long_lost")
(defclass control_xy::TriggerAction
  :super ros::object
  :slots (_trigger ))

(defmethod control_xy::TriggerAction
  (:init
   (&key
    ((:trigger __trigger) "")
    )
   (send-super :init)
   (setq _trigger (string __trigger))
   self)
  (:trigger
   (&optional __trigger)
   (if __trigger (setq _trigger __trigger)) _trigger)
  (:serialization-length
   ()
   (+
    ;; string _trigger
    4 (length _trigger)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _trigger
       (write-long (length _trigger) s) (princ _trigger s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _trigger
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _trigger (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get control_xy::TriggerAction :md5sum-) "529f37831afe7067075cb584db0e391e")
(setf (get control_xy::TriggerAction :datatype-) "control_xy/TriggerAction")
(setf (get control_xy::TriggerAction :definition-)
      "# 非常停止ボタン解除
string TRIGGER_EMERGENCY_BUTTON_OFF = emergency_button_off
# 非常停止ボタン押下
string TRIGGER_EMERGENCY_BUTTON_ON = emergency_button_on
# カルガモボタン押下
string TRIGGER_KARUGAMO_BUTTON_ON = karugamo_button_on
# リモコン:カルガモボタン押下
string TRIGGER_REMOTE_KARUGAMO_BUTTON_ON = remote_karuamo_button_on
# リモコン:マニュアルボタン押下
string TRIGGER_REMOTE_MANUAL_BUTTON_ON = remote_manual_button_on
# リモコン:アイドルボタン押下
string TRIGGER_REMOTE_IDLE_BUTTON_ON = remote_idle_button_on
# アイドルボタン押下
string TRIGGER_IDLE_BUTTON_ON = idle_button_on
# 進行方向 2000 mm 以内に障害物を発見
string TRIGGER_DETECT_OBSTACLE = detect_obstacle
# 前方近傍に障害物を発見（LIDAR進行方向 500 mm以内）
string TRIGGER_DETECT_DANGER_OBSTACLE = detect_danger_obstacle
# ガードバンパー接触
string TRIGGER_COLLISION = collision
# ブレーキ解除ボタン押下
string TRIGGER_BREAK_RELEASE_BUTTON_ON = break_release_button_on
# 対象ロストから10秒経過
string TRIGGER_LONG_LOST = long_lost

string trigger

")



(provide :control_xy/TriggerAction "529f37831afe7067075cb584db0e391e")


