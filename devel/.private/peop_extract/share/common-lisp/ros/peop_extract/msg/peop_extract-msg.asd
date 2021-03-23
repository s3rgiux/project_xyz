
(cl:in-package :asdf)

(defsystem "peop_extract-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BoundingBox" :depends-on ("_package_BoundingBox"))
    (:file "_package_BoundingBox" :depends-on ("_package"))
    (:file "BoundingBoxes" :depends-on ("_package_BoundingBoxes"))
    (:file "_package_BoundingBoxes" :depends-on ("_package"))
    (:file "ObjectCount" :depends-on ("_package_ObjectCount"))
    (:file "_package_ObjectCount" :depends-on ("_package"))
    (:file "people_box" :depends-on ("_package_people_box"))
    (:file "_package_people_box" :depends-on ("_package"))
    (:file "peoples" :depends-on ("_package_peoples"))
    (:file "_package_peoples" :depends-on ("_package"))
  ))