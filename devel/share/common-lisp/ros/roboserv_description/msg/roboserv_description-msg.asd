
(cl:in-package :asdf)

(defsystem "roboserv_description-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AppMessages" :depends-on ("_package_AppMessages"))
    (:file "_package_AppMessages" :depends-on ("_package"))
    (:file "AppPoint" :depends-on ("_package_AppPoint"))
    (:file "_package_AppPoint" :depends-on ("_package"))
    (:file "Motores" :depends-on ("_package_Motores"))
    (:file "_package_Motores" :depends-on ("_package"))
    (:file "Sensores" :depends-on ("_package_Sensores"))
    (:file "_package_Sensores" :depends-on ("_package"))
  ))