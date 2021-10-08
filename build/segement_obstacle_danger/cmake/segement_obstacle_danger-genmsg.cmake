# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "segement_obstacle_danger: 5 messages, 0 services")

set(MSG_I_FLAGS "-Isegement_obstacle_danger:/home/xavier/catkin_ws/src/segement_obstacle_danger/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(segement_obstacle_danger_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg" NAME_WE)
add_custom_target(_segement_obstacle_danger_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "segement_obstacle_danger" "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg" "geometry_msgs/Vector3:geometry_msgs/Point"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg" NAME_WE)
add_custom_target(_segement_obstacle_danger_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "segement_obstacle_danger" "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg" NAME_WE)
add_custom_target(_segement_obstacle_danger_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "segement_obstacle_danger" "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg" "geometry_msgs/Twist:geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg" NAME_WE)
add_custom_target(_segement_obstacle_danger_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "segement_obstacle_danger" "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg" "geometry_msgs/Point"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg" NAME_WE)
add_custom_target(_segement_obstacle_danger_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "segement_obstacle_danger" "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg" "geometry_msgs/Vector3:segement_obstacle_danger/CircleObstacle:segement_obstacle_danger/SegmentObstacle:geometry_msgs/Point:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_cpp(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_cpp(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_cpp(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_cpp(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg;/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/segement_obstacle_danger
)

### Generating Services

### Generating Module File
_generate_module_cpp(segement_obstacle_danger
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/segement_obstacle_danger
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(segement_obstacle_danger_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(segement_obstacle_danger_generate_messages segement_obstacle_danger_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_cpp _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_cpp _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_cpp _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_cpp _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_cpp _segement_obstacle_danger_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(segement_obstacle_danger_gencpp)
add_dependencies(segement_obstacle_danger_gencpp segement_obstacle_danger_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS segement_obstacle_danger_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_eus(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_eus(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_eus(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_eus(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg;/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/segement_obstacle_danger
)

### Generating Services

### Generating Module File
_generate_module_eus(segement_obstacle_danger
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/segement_obstacle_danger
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(segement_obstacle_danger_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(segement_obstacle_danger_generate_messages segement_obstacle_danger_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_eus _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_eus _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_eus _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_eus _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_eus _segement_obstacle_danger_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(segement_obstacle_danger_geneus)
add_dependencies(segement_obstacle_danger_geneus segement_obstacle_danger_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS segement_obstacle_danger_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_lisp(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_lisp(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_lisp(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_lisp(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg;/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/segement_obstacle_danger
)

### Generating Services

### Generating Module File
_generate_module_lisp(segement_obstacle_danger
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/segement_obstacle_danger
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(segement_obstacle_danger_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(segement_obstacle_danger_generate_messages segement_obstacle_danger_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_lisp _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_lisp _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_lisp _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_lisp _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_lisp _segement_obstacle_danger_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(segement_obstacle_danger_genlisp)
add_dependencies(segement_obstacle_danger_genlisp segement_obstacle_danger_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS segement_obstacle_danger_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_nodejs(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_nodejs(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_nodejs(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_nodejs(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg;/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/segement_obstacle_danger
)

### Generating Services

### Generating Module File
_generate_module_nodejs(segement_obstacle_danger
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/segement_obstacle_danger
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(segement_obstacle_danger_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(segement_obstacle_danger_generate_messages segement_obstacle_danger_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_nodejs _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_nodejs _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_nodejs _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_nodejs _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_nodejs _segement_obstacle_danger_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(segement_obstacle_danger_gennodejs)
add_dependencies(segement_obstacle_danger_gennodejs segement_obstacle_danger_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS segement_obstacle_danger_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_py(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_py(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_py(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/segement_obstacle_danger
)
_generate_msg_py(segement_obstacle_danger
  "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg;/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/segement_obstacle_danger
)

### Generating Services

### Generating Module File
_generate_module_py(segement_obstacle_danger
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/segement_obstacle_danger
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(segement_obstacle_danger_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(segement_obstacle_danger_generate_messages segement_obstacle_danger_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/CircleObstacle.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_py _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/DangerStates.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_py _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/States.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_py _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/SegmentObstacle.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_py _segement_obstacle_danger_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/segement_obstacle_danger/msg/Obstacles.msg" NAME_WE)
add_dependencies(segement_obstacle_danger_generate_messages_py _segement_obstacle_danger_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(segement_obstacle_danger_genpy)
add_dependencies(segement_obstacle_danger_genpy segement_obstacle_danger_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS segement_obstacle_danger_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/segement_obstacle_danger)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/segement_obstacle_danger
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(segement_obstacle_danger_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(segement_obstacle_danger_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/segement_obstacle_danger)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/segement_obstacle_danger
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(segement_obstacle_danger_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(segement_obstacle_danger_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/segement_obstacle_danger)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/segement_obstacle_danger
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(segement_obstacle_danger_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(segement_obstacle_danger_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/segement_obstacle_danger)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/segement_obstacle_danger
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(segement_obstacle_danger_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(segement_obstacle_danger_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/segement_obstacle_danger)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/segement_obstacle_danger\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/segement_obstacle_danger
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(segement_obstacle_danger_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(segement_obstacle_danger_generate_messages_py geometry_msgs_generate_messages_py)
endif()
