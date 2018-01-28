# CMake generated Testfile for 
# Source directory: /home/xavier/catkin_ws/src/move_base_flex/mbf_abstract_nav
# Build directory: /home/xavier/catkin_ws/build/mbf_abstract_nav
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_mbf_abstract_nav_rostest_test_abstract_action_base.launch "/home/xavier/catkin_ws/build/mbf_abstract_nav/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/xavier/catkin_ws/build/mbf_abstract_nav/test_results/mbf_abstract_nav/rostest-test_abstract_action_base.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/xavier/catkin_ws/src/move_base_flex/mbf_abstract_nav --package=mbf_abstract_nav --results-filename test_abstract_action_base.xml --results-base-dir \"/home/xavier/catkin_ws/build/mbf_abstract_nav/test_results\" /home/xavier/catkin_ws/src/move_base_flex/mbf_abstract_nav/test/abstract_action_base.launch ")
subdirs("gtest")
