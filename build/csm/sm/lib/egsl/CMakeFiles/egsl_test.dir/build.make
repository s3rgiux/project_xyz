# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/xavier/catkin_ws/src/csm

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xavier/catkin_ws/build/csm

# Include any dependencies generated for this target.
include sm/lib/egsl/CMakeFiles/egsl_test.dir/depend.make

# Include the progress variables for this target.
include sm/lib/egsl/CMakeFiles/egsl_test.dir/progress.make

# Include the compile flags for this target's objects.
include sm/lib/egsl/CMakeFiles/egsl_test.dir/flags.make

sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o: sm/lib/egsl/CMakeFiles/egsl_test.dir/flags.make
sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o: /home/xavier/catkin_ws/src/csm/sm/lib/egsl/egsl_test.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o"
	cd /home/xavier/catkin_ws/build/csm/sm/lib/egsl && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/egsl_test.dir/egsl_test.o   -c /home/xavier/catkin_ws/src/csm/sm/lib/egsl/egsl_test.c

sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/egsl_test.dir/egsl_test.i"
	cd /home/xavier/catkin_ws/build/csm/sm/lib/egsl && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/xavier/catkin_ws/src/csm/sm/lib/egsl/egsl_test.c > CMakeFiles/egsl_test.dir/egsl_test.i

sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/egsl_test.dir/egsl_test.s"
	cd /home/xavier/catkin_ws/build/csm/sm/lib/egsl && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/xavier/catkin_ws/src/csm/sm/lib/egsl/egsl_test.c -o CMakeFiles/egsl_test.dir/egsl_test.s

sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o.requires:

.PHONY : sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o.requires

sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o.provides: sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o.requires
	$(MAKE) -f sm/lib/egsl/CMakeFiles/egsl_test.dir/build.make sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o.provides.build
.PHONY : sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o.provides

sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o.provides.build: sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o


# Object files for target egsl_test
egsl_test_OBJECTS = \
"CMakeFiles/egsl_test.dir/egsl_test.o"

# External object files for target egsl_test
egsl_test_EXTERNAL_OBJECTS =

sm/lib/egsl/egsl_test: sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o
sm/lib/egsl/egsl_test: sm/lib/egsl/CMakeFiles/egsl_test.dir/build.make
sm/lib/egsl/egsl_test: sm/lib/egsl/libegsl.a
sm/lib/egsl/egsl_test: sm/lib/egsl/CMakeFiles/egsl_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable egsl_test"
	cd /home/xavier/catkin_ws/build/csm/sm/lib/egsl && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/egsl_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sm/lib/egsl/CMakeFiles/egsl_test.dir/build: sm/lib/egsl/egsl_test

.PHONY : sm/lib/egsl/CMakeFiles/egsl_test.dir/build

sm/lib/egsl/CMakeFiles/egsl_test.dir/requires: sm/lib/egsl/CMakeFiles/egsl_test.dir/egsl_test.o.requires

.PHONY : sm/lib/egsl/CMakeFiles/egsl_test.dir/requires

sm/lib/egsl/CMakeFiles/egsl_test.dir/clean:
	cd /home/xavier/catkin_ws/build/csm/sm/lib/egsl && $(CMAKE_COMMAND) -P CMakeFiles/egsl_test.dir/cmake_clean.cmake
.PHONY : sm/lib/egsl/CMakeFiles/egsl_test.dir/clean

sm/lib/egsl/CMakeFiles/egsl_test.dir/depend:
	cd /home/xavier/catkin_ws/build/csm && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xavier/catkin_ws/src/csm /home/xavier/catkin_ws/src/csm/sm/lib/egsl /home/xavier/catkin_ws/build/csm /home/xavier/catkin_ws/build/csm/sm/lib/egsl /home/xavier/catkin_ws/build/csm/sm/lib/egsl/CMakeFiles/egsl_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sm/lib/egsl/CMakeFiles/egsl_test.dir/depend

