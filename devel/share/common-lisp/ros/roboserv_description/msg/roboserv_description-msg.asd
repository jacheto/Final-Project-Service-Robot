
(cl:in-package :asdf)

(defsystem "roboserv_description-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Motores" :depends-on ("_package_Motores"))
    (:file "_package_Motores" :depends-on ("_package"))
    (:file "Sensores" :depends-on ("_package_Sensores"))
    (:file "_package_Sensores" :depends-on ("_package"))
  ))