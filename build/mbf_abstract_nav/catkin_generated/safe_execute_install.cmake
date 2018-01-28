execute_process(COMMAND "/home/xavier/catkin_ws/build/mbf_abstract_nav/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/xavier/catkin_ws/build/mbf_abstract_nav/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
