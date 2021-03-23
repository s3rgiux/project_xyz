# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "pitakuru: 14 messages, 0 services")

set(MSG_I_FLAGS "-Ipitakuru:/home/xavier/catkin_ws/src/pitakuru/msg;-Ipitakuru:/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/melodic/share/actionlib_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(pitakuru_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg" "actionlib_msgs/GoalID:pitakuru/SoundGoal:std_msgs/Header"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg" "geometry_msgs/Twist:geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg" "actionlib_msgs/GoalID:pitakuru/SoundGoal:actionlib_msgs/GoalStatus:pitakuru/SoundResult:pitakuru/SoundActionGoal:pitakuru/SoundFeedback:pitakuru/SoundActionFeedback:std_msgs/Header:pitakuru/SoundActionResult"
)

get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg" "actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:pitakuru/SoundFeedback:std_msgs/Header"
)

get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg" "actionlib_msgs/GoalID:actionlib_msgs/GoalStatus:pitakuru/SoundResult:std_msgs/Header"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg" "pitakuru/people_box"
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg" ""
)

get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg" NAME_WE)
add_custom_target(_pitakuru_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "pitakuru" "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)
_generate_msg_cpp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
)

### Generating Services

### Generating Module File
_generate_module_cpp(pitakuru
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(pitakuru_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(pitakuru_generate_messages pitakuru_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_cpp _pitakuru_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pitakuru_gencpp)
add_dependencies(pitakuru_gencpp pitakuru_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pitakuru_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)
_generate_msg_eus(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
)

### Generating Services

### Generating Module File
_generate_module_eus(pitakuru
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(pitakuru_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(pitakuru_generate_messages pitakuru_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_eus _pitakuru_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pitakuru_geneus)
add_dependencies(pitakuru_geneus pitakuru_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pitakuru_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)
_generate_msg_lisp(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
)

### Generating Services

### Generating Module File
_generate_module_lisp(pitakuru
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(pitakuru_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(pitakuru_generate_messages pitakuru_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_lisp _pitakuru_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pitakuru_genlisp)
add_dependencies(pitakuru_genlisp pitakuru_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pitakuru_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)
_generate_msg_nodejs(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
)

### Generating Services

### Generating Module File
_generate_module_nodejs(pitakuru
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(pitakuru_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(pitakuru_generate_messages pitakuru_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_nodejs _pitakuru_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pitakuru_gennodejs)
add_dependencies(pitakuru_gennodejs pitakuru_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pitakuru_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/melodic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg"
  "${MSG_I_FLAGS}"
  "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)
_generate_msg_py(pitakuru
  "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
)

### Generating Services

### Generating Module File
_generate_module_py(pitakuru
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(pitakuru_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(pitakuru_generate_messages pitakuru_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionGoal.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/TriggerAction.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundResult.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundFeedback.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/States.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundGoal.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/State.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundAction.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionFeedback.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/devel/.private/pitakuru/share/pitakuru/msg/SoundActionResult.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/Obstacle.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/peoples.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/people_box.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xavier/catkin_ws/src/pitakuru/msg/DriveWheel.msg" NAME_WE)
add_dependencies(pitakuru_generate_messages_py _pitakuru_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(pitakuru_genpy)
add_dependencies(pitakuru_genpy pitakuru_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS pitakuru_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/pitakuru
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(pitakuru_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(pitakuru_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(pitakuru_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/pitakuru
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(pitakuru_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(pitakuru_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(pitakuru_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/pitakuru
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(pitakuru_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(pitakuru_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(pitakuru_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/pitakuru
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(pitakuru_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(pitakuru_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(pitakuru_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/pitakuru
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(pitakuru_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(pitakuru_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(pitakuru_generate_messages_py geometry_msgs_generate_messages_py)
endif()
