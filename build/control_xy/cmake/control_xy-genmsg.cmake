# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "control_xy: 6 messages, 0 services")

set(MSG_I_FLAGS "-Icontrol_xy:/home/xavier/catkin_ws/src/control_xy/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/melodic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(control_xy_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg" NAME_WE)
add_custom_target(_control_xy_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "control_xy" "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg" NAME_WE)
add_custom_target(_control_xy_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "control_xy" "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg" NAME_WE)
add_custom_target(_control_xy_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "control_xy" "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg" NAME_WE)
add_custom_target(_control_xy_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "control_xy" "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/States.msg" NAME_WE)
add_custom_target(_control_xy_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "control_xy" "/home/xavier/catkin_ws/src/control_xy/msg/States.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/State.msg" NAME_WE)
add_custom_target(_control_xy_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "control_xy" "/home/xavier/catkin_ws/src/control_xy/msg/State.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_xy
)
_generate_msg_cpp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_xy
)
_generate_msg_cpp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_xy
)
_generate_msg_cpp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_xy
)
_generate_msg_cpp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/States.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_xy
)
_generate_msg_cpp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/State.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_xy
)

### Generating Services

### Generating Module File
_generate_module_cpp(control_xy
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_xy
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(control_xy_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(control_xy_generate_messages control_xy_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_cpp _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_cpp _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_cpp _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_cpp _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/States.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_cpp _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/State.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_cpp _control_xy_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(control_xy_gencpp)
add_dependencies(control_xy_gencpp control_xy_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS control_xy_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_xy
)
_generate_msg_eus(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_xy
)
_generate_msg_eus(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_xy
)
_generate_msg_eus(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_xy
)
_generate_msg_eus(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/States.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_xy
)
_generate_msg_eus(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/State.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_xy
)

### Generating Services

### Generating Module File
_generate_module_eus(control_xy
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_xy
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(control_xy_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(control_xy_generate_messages control_xy_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_eus _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_eus _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_eus _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_eus _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/States.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_eus _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/State.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_eus _control_xy_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(control_xy_geneus)
add_dependencies(control_xy_geneus control_xy_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS control_xy_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_xy
)
_generate_msg_lisp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_xy
)
_generate_msg_lisp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_xy
)
_generate_msg_lisp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_xy
)
_generate_msg_lisp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/States.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_xy
)
_generate_msg_lisp(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/State.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_xy
)

### Generating Services

### Generating Module File
_generate_module_lisp(control_xy
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_xy
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(control_xy_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(control_xy_generate_messages control_xy_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_lisp _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_lisp _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_lisp _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_lisp _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/States.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_lisp _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/State.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_lisp _control_xy_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(control_xy_genlisp)
add_dependencies(control_xy_genlisp control_xy_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS control_xy_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_xy
)
_generate_msg_nodejs(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_xy
)
_generate_msg_nodejs(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_xy
)
_generate_msg_nodejs(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_xy
)
_generate_msg_nodejs(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/States.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_xy
)
_generate_msg_nodejs(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/State.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_xy
)

### Generating Services

### Generating Module File
_generate_module_nodejs(control_xy
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_xy
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(control_xy_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(control_xy_generate_messages control_xy_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_nodejs _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_nodejs _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_nodejs _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_nodejs _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/States.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_nodejs _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/State.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_nodejs _control_xy_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(control_xy_gennodejs)
add_dependencies(control_xy_gennodejs control_xy_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS control_xy_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_xy
)
_generate_msg_py(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_xy
)
_generate_msg_py(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_xy
)
_generate_msg_py(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_xy
)
_generate_msg_py(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/States.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_xy
)
_generate_msg_py(control_xy
  "/home/xavier/catkin_ws/src/control_xy/msg/State.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_xy
)

### Generating Services

### Generating Module File
_generate_module_py(control_xy
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_xy
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(control_xy_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(control_xy_generate_messages control_xy_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/DriveWheel.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_py _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/Obstacle.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_py _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/StateWheels.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_py _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/TriggerAction.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_py _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/States.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_py _control_xy_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/control_xy/msg/State.msg" NAME_WE)
add_dependencies(control_xy_generate_messages_py _control_xy_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(control_xy_genpy)
add_dependencies(control_xy_genpy control_xy_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS control_xy_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_xy)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/control_xy
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(control_xy_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(control_xy_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_xy)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/control_xy
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(control_xy_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(control_xy_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_xy)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/control_xy
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(control_xy_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(control_xy_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_xy)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/control_xy
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(control_xy_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(control_xy_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_xy)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_xy\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/control_xy
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(control_xy_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(control_xy_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
