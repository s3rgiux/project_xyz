
(cl:in-package :asdf)

(defsystem "pypro-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "StateWheels" :depends-on ("_package_StateWheels"))
    (:file "_package_StateWheels" :depends-on ("_package"))
  ))