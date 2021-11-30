# CMake generated Testfile for 
# Source directory: /home/xavier/catkin_ws/src/csm2/sm
# Build directory: /home/xavier/catkin_ws/build/csm/sm
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_math_utils_sanity "test_math_utils_sanity")
subdirs("lib/options")
subdirs("lib/json-c")
subdirs("lib/egsl")
subdirs("lib/gpc")
subdirs("csm")
subdirs("pkg-config")
