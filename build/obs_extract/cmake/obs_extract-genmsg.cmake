# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "obs_extract: 3 messages, 0 services")

set(MSG_I_FLAGS "-Iobs_extract:/home/xavier/catkin_ws/src/obs_extract/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(obs_extract_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg" NAME_WE)
add_custom_target(_obs_extract_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "obs_extract" "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg" "geometry_msgs/Vector3:geometry_msgs/Point"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg" NAME_WE)
add_custom_target(_obs_extract_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "obs_extract" "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg" "geometry_msgs/Point"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg" NAME_WE)
add_custom_target(_obs_extract_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "obs_extract" "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg" "geometry_msgs/Vector3:obs_extract/CircleObstacle:obs_extract/SegmentObstacle:geometry_msgs/Point:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/obs_extract
)
_generate_msg_cpp(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg;/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/obs_extract
)
_generate_msg_cpp(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/obs_extract
)

### Generating Services

### Generating Module File
_generate_module_cpp(obs_extract
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/obs_extract
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(obs_extract_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(obs_extract_generate_messages obs_extract_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_cpp _obs_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_cpp _obs_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_cpp _obs_extract_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(obs_extract_gencpp)
add_dependencies(obs_extract_gencpp obs_extract_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS obs_extract_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/obs_extract
)
_generate_msg_eus(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg;/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/obs_extract
)
_generate_msg_eus(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/obs_extract
)

### Generating Services

### Generating Module File
_generate_module_eus(obs_extract
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/obs_extract
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(obs_extract_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(obs_extract_generate_messages obs_extract_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_eus _obs_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_eus _obs_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_eus _obs_extract_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(obs_extract_geneus)
add_dependencies(obs_extract_geneus obs_extract_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS obs_extract_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/obs_extract
)
_generate_msg_lisp(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg;/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/obs_extract
)
_generate_msg_lisp(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/obs_extract
)

### Generating Services

### Generating Module File
_generate_module_lisp(obs_extract
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/obs_extract
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(obs_extract_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(obs_extract_generate_messages obs_extract_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_lisp _obs_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_lisp _obs_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_lisp _obs_extract_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(obs_extract_genlisp)
add_dependencies(obs_extract_genlisp obs_extract_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS obs_extract_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/obs_extract
)
_generate_msg_nodejs(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg;/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/obs_extract
)
_generate_msg_nodejs(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/obs_extract
)

### Generating Services

### Generating Module File
_generate_module_nodejs(obs_extract
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/obs_extract
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(obs_extract_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(obs_extract_generate_messages obs_extract_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_nodejs _obs_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_nodejs _obs_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_nodejs _obs_extract_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(obs_extract_gennodejs)
add_dependencies(obs_extract_gennodejs obs_extract_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS obs_extract_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obs_extract
)
_generate_msg_py(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg;/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obs_extract
)
_generate_msg_py(obs_extract
  "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obs_extract
)

### Generating Services

### Generating Module File
_generate_module_py(obs_extract
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obs_extract
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(obs_extract_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(obs_extract_generate_messages obs_extract_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/CircleObstacle.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_py _obs_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/SegmentObstacle.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_py _obs_extract_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/obs_extract/msg/Obstacles.msg" NAME_WE)
add_dependencies(obs_extract_generate_messages_py _obs_extract_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(obs_extract_genpy)
add_dependencies(obs_extract_genpy obs_extract_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS obs_extract_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/obs_extract)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/obs_extract
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(obs_extract_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(obs_extract_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/obs_extract)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/obs_extract
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(obs_extract_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(obs_extract_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/obs_extract)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/obs_extract
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(obs_extract_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(obs_extract_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/obs_extract)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/obs_extract
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(obs_extract_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(obs_extract_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obs_extract)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obs_extract\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/obs_extract
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(obs_extract_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(obs_extract_generate_messages_py geometry_msgs_generate_messages_py)
endif()
