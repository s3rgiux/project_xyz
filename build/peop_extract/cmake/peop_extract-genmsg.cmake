# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "peop_extract: 6 messages, 0 services")

set(MSG_I_FLAGS "-Ipeop_extract:/home/xavier/catkin_ws/src/peop_extract/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(peop_extract_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg" NAME_WE)
add_custom_target(_peop_extract_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "peop_extract" "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg" "geometry_msgs/Twist:geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg" NAME_WE)
add_custom_target(_peop_extract_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "peop_extract" "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg" NAME_WE)
add_custom_target(_peop_extract_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "peop_extract" "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg" "peop_extract/people_box"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg" NAME_WE)
add_custom_target(_peop_extract_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "peop_extract" "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg" "peop_extract/BoundingBox:std_msgs/Header"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg" NAME_WE)
add_custom_target(_peop_extract_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "peop_extract" "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg" NAME_WE)
add_custom_target(_peop_extract_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "peop_extract" "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/peop_extract
)
_generate_msg_cpp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/peop_extract
)
_generate_msg_cpp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/peop_extract
)
_generate_msg_cpp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/peop_extract
)
_generate_msg_cpp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/peop_extract
)
_generate_msg_cpp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/peop_extract
)

### Generating Services

### Generating Module File
_generate_module_cpp(peop_extract
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/peop_extract
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(peop_extract_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(peop_extract_generate_messages peop_extract_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_cpp _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_cpp _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_cpp _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_cpp _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_cpp _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_cpp _peop_extract_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(peop_extract_gencpp)
add_dependencies(peop_extract_gencpp peop_extract_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS peop_extract_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/peop_extract
)
_generate_msg_eus(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/peop_extract
)
_generate_msg_eus(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/peop_extract
)
_generate_msg_eus(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/peop_extract
)
_generate_msg_eus(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/peop_extract
)
_generate_msg_eus(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/peop_extract
)

### Generating Services

### Generating Module File
_generate_module_eus(peop_extract
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/peop_extract
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(peop_extract_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(peop_extract_generate_messages peop_extract_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_eus _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_eus _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_eus _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_eus _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_eus _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_eus _peop_extract_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(peop_extract_geneus)
add_dependencies(peop_extract_geneus peop_extract_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS peop_extract_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/peop_extract
)
_generate_msg_lisp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/peop_extract
)
_generate_msg_lisp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/peop_extract
)
_generate_msg_lisp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/peop_extract
)
_generate_msg_lisp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/peop_extract
)
_generate_msg_lisp(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/peop_extract
)

### Generating Services

### Generating Module File
_generate_module_lisp(peop_extract
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/peop_extract
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(peop_extract_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(peop_extract_generate_messages peop_extract_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_lisp _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_lisp _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_lisp _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_lisp _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_lisp _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_lisp _peop_extract_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(peop_extract_genlisp)
add_dependencies(peop_extract_genlisp peop_extract_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS peop_extract_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/peop_extract
)
_generate_msg_nodejs(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/peop_extract
)
_generate_msg_nodejs(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/peop_extract
)
_generate_msg_nodejs(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/peop_extract
)
_generate_msg_nodejs(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/peop_extract
)
_generate_msg_nodejs(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/peop_extract
)

### Generating Services

### Generating Module File
_generate_module_nodejs(peop_extract
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/peop_extract
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(peop_extract_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(peop_extract_generate_messages peop_extract_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_nodejs _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_nodejs _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_nodejs _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_nodejs _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_nodejs _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_nodejs _peop_extract_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(peop_extract_gennodejs)
add_dependencies(peop_extract_gennodejs peop_extract_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS peop_extract_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/peop_extract
)
_generate_msg_py(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/peop_extract
)
_generate_msg_py(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/peop_extract
)
_generate_msg_py(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/peop_extract
)
_generate_msg_py(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/peop_extract
)
_generate_msg_py(peop_extract
  "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/peop_extract
)

### Generating Services

### Generating Module File
_generate_module_py(peop_extract
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/peop_extract
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(peop_extract_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(peop_extract_generate_messages peop_extract_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/States.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_py _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBox.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_py _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/peoples.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_py _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/BoundingBoxes.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_py _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/ObjectCount.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_py _peop_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/peop_extract/msg/people_box.msg" NAME_WE)
add_dependencies(peop_extract_generate_messages_py _peop_extract_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(peop_extract_genpy)
add_dependencies(peop_extract_genpy peop_extract_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS peop_extract_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/peop_extract)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/peop_extract
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(peop_extract_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(peop_extract_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/peop_extract)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/peop_extract
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(peop_extract_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(peop_extract_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/peop_extract)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/peop_extract
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(peop_extract_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(peop_extract_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/peop_extract)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/peop_extract
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(peop_extract_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(peop_extract_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/peop_extract)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/peop_extract\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/peop_extract
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(peop_extract_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(peop_extract_generate_messages_py geometry_msgs_generate_messages_py)
endif()
