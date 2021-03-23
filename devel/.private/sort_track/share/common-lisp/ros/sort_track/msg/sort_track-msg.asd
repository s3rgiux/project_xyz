
(cl:in-package :asdf)

(defsystem "sort_track-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "IntList" :depends-on ("_package_IntList"))
    (:file "_package_IntList" :depends-on ("_package"))
    (:file "IntList" :depends-on ("_package_IntList"))
    (:file "_package_IntList" :depends-on ("_package"))
    (:file "people_box" :depends-on ("_package_people_box"))
    (:file "_package_people_box" :depends-on ("_package"))
    (:file "people_box" :depends-on ("_package_people_box"))
    (:file "_package_people_box" :depends-on ("_package"))
    (:file "peoples" :depends-on ("_package_peoples"))
    (:file "_package_peoples" :depends-on ("_package"))
    (:file "peoples" :depends-on ("_package_peoples"))
    (:file "_package_peoples" :depends-on ("_package"))
  ))