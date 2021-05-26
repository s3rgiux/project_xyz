# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "transfo: 1 messages, 0 services")

set(MSG_I_FLAGS "-Itransfo:/home/xavier/catkin_ws/src/transfo/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(transfo_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg" NAME_WE)
add_custom_target(_transfo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "transfo" "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(transfo
  "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/transfo
)

### Generating Services

### Generating Module File
_generate_module_cpp(transfo
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/transfo
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(transfo_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(transfo_generate_messages transfo_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg" NAME_WE)
add_dependencies(transfo_generate_messages_cpp _transfo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(transfo_gencpp)
add_dependencies(transfo_gencpp transfo_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS transfo_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(transfo
  "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/transfo
)

### Generating Services

### Generating Module File
_generate_module_eus(transfo
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/transfo
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(transfo_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(transfo_generate_messages transfo_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg" NAME_WE)
add_dependencies(transfo_generate_messages_eus _transfo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(transfo_geneus)
add_dependencies(transfo_geneus transfo_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS transfo_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(transfo
  "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/transfo
)

### Generating Services

### Generating Module File
_generate_module_lisp(transfo
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/transfo
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(transfo_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(transfo_generate_messages transfo_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg" NAME_WE)
add_dependencies(transfo_generate_messages_lisp _transfo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(transfo_genlisp)
add_dependencies(transfo_genlisp transfo_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS transfo_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(transfo
  "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/transfo
)

### Generating Services

### Generating Module File
_generate_module_nodejs(transfo
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/transfo
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(transfo_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(transfo_generate_messages transfo_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg" NAME_WE)
add_dependencies(transfo_generate_messages_nodejs _transfo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(transfo_gennodejs)
add_dependencies(transfo_gennodejs transfo_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS transfo_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(transfo
  "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/transfo
)

### Generating Services

### Generating Module File
_generate_module_py(transfo
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/transfo
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(transfo_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(transfo_generate_messages transfo_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/transfo/msg/Frame.msg" NAME_WE)
add_dependencies(transfo_generate_messages_py _transfo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(transfo_genpy)
add_dependencies(transfo_genpy transfo_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS transfo_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/transfo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/transfo
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(transfo_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(transfo_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/transfo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/transfo
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(transfo_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(transfo_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/transfo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/transfo
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(transfo_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(transfo_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/transfo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/transfo
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(transfo_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(transfo_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/transfo)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/transfo\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/transfo
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(transfo_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(transfo_generate_messages_py geometry_msgs_generate_messages_py)
endif()
