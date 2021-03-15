
(cl:in-package :asdf)

(defsystem "control_xy-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "DriveWheel" :depends-on ("_package_DriveWheel"))
    (:file "_package_DriveWheel" :depends-on ("_package"))
    (:file "Obstacle" :depends-on ("_package_Obstacle"))
    (:file "_package_Obstacle" :depends-on ("_package"))
    (:file "State" :depends-on ("_package_State"))
    (:file "_package_State" :depends-on ("_package"))
    (:file "StateWheels" :depends-on ("_package_StateWheels"))
    (:file "_package_StateWheels" :depends-on ("_package"))
    (:file "States" :depends-on ("_package_States"))
    (:file "_package_States" :depends-on ("_package"))
    (:file "TriggerAction" :depends-on ("_package_TriggerAction"))
    (:file "_package_TriggerAction" :depends-on ("_package"))
  ))