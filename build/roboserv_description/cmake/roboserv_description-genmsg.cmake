# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "roboserv_description: 3 messages, 0 services")

set(MSG_I_FLAGS "-Iroboserv_description:/home/felipe/roboserv_ws/src/roboserv_description/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(roboserv_description_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg" NAME_WE)
add_custom_target(_roboserv_description_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "roboserv_description" "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg" ""
)

get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg" NAME_WE)
add_custom_target(_roboserv_description_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "roboserv_description" "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg" ""
)

get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg" NAME_WE)
add_custom_target(_roboserv_description_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "roboserv_description" "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/roboserv_description
)
_generate_msg_cpp(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/roboserv_description
)
_generate_msg_cpp(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/roboserv_description
)

### Generating Services

### Generating Module File
_generate_module_cpp(roboserv_description
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/roboserv_description
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(roboserv_description_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(roboserv_description_generate_messages roboserv_description_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_cpp _roboserv_description_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_cpp _roboserv_description_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_cpp _roboserv_description_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(roboserv_description_gencpp)
add_dependencies(roboserv_description_gencpp roboserv_description_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS roboserv_description_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/roboserv_description
)
_generate_msg_eus(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/roboserv_description
)
_generate_msg_eus(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/roboserv_description
)

### Generating Services

### Generating Module File
_generate_module_eus(roboserv_description
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/roboserv_description
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(roboserv_description_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(roboserv_description_generate_messages roboserv_description_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_eus _roboserv_description_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_eus _roboserv_description_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_eus _roboserv_description_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(roboserv_description_geneus)
add_dependencies(roboserv_description_geneus roboserv_description_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS roboserv_description_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/roboserv_description
)
_generate_msg_lisp(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/roboserv_description
)
_generate_msg_lisp(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/roboserv_description
)

### Generating Services

### Generating Module File
_generate_module_lisp(roboserv_description
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/roboserv_description
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(roboserv_description_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(roboserv_description_generate_messages roboserv_description_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_lisp _roboserv_description_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_lisp _roboserv_description_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_lisp _roboserv_description_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(roboserv_description_genlisp)
add_dependencies(roboserv_description_genlisp roboserv_description_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS roboserv_description_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/roboserv_description
)
_generate_msg_nodejs(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/roboserv_description
)
_generate_msg_nodejs(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/roboserv_description
)

### Generating Services

### Generating Module File
_generate_module_nodejs(roboserv_description
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/roboserv_description
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(roboserv_description_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(roboserv_description_generate_messages roboserv_description_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_nodejs _roboserv_description_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_nodejs _roboserv_description_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_nodejs _roboserv_description_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(roboserv_description_gennodejs)
add_dependencies(roboserv_description_gennodejs roboserv_description_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS roboserv_description_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/roboserv_description
)
_generate_msg_py(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/roboserv_description
)
_generate_msg_py(roboserv_description
  "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/roboserv_description
)

### Generating Services

### Generating Module File
_generate_module_py(roboserv_description
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/roboserv_description
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(roboserv_description_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(roboserv_description_generate_messages roboserv_description_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Motores.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_py _roboserv_description_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/AppMsg.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_py _roboserv_description_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/felipe/roboserv_ws/src/roboserv_description/msg/Sensores.msg" NAME_WE)
add_dependencies(roboserv_description_generate_messages_py _roboserv_description_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(roboserv_description_genpy)
add_dependencies(roboserv_description_genpy roboserv_description_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS roboserv_description_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/roboserv_description)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/roboserv_description
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(roboserv_description_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/roboserv_description)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/roboserv_description
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(roboserv_description_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/roboserv_description)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/roboserv_description
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(roboserv_description_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/roboserv_description)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/roboserv_description
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(roboserv_description_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/roboserv_description)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/roboserv_description\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/roboserv_description
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(roboserv_description_generate_messages_py std_msgs_generate_messages_py)
endif()
