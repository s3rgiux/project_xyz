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
include sm/CMakeFiles/sm_animate.dir/depend.make

# Include the progress variables for this target.
include sm/CMakeFiles/sm_animate.dir/progress.make

# Include the compile flags for this target's objects.
include sm/CMakeFiles/sm_animate.dir/flags.make

sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o: sm/CMakeFiles/sm_animate.dir/flags.make
sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o: /home/xavier/catkin_ws/src/csm/sm/apps/sm_animate.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sm_animate.dir/apps/sm_animate.o   -c /home/xavier/catkin_ws/src/csm/sm/apps/sm_animate.c

sm/CMakeFiles/sm_animate.dir/apps/sm_animate.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sm_animate.dir/apps/sm_animate.i"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/xavier/catkin_ws/src/csm/sm/apps/sm_animate.c > CMakeFiles/sm_animate.dir/apps/sm_animate.i

sm/CMakeFiles/sm_animate.dir/apps/sm_animate.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sm_animate.dir/apps/sm_animate.s"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/xavier/catkin_ws/src/csm/sm/apps/sm_animate.c -o CMakeFiles/sm_animate.dir/apps/sm_animate.s

sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o.requires:

.PHONY : sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o.requires

sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o.provides: sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o.requires
	$(MAKE) -f sm/CMakeFiles/sm_animate.dir/build.make sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o.provides.build
.PHONY : sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o.provides

sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o.provides.build: sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o


# Object files for target sm_animate
sm_animate_OBJECTS = \
"CMakeFiles/sm_animate.dir/apps/sm_animate.o"

# External object files for target sm_animate
sm_animate_EXTERNAL_OBJECTS =

sm/sm_animate: sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o
sm/sm_animate: sm/CMakeFiles/sm_animate.dir/build.make
sm/sm_animate: sm/libcsm-static.a
sm/sm_animate: sm/CMakeFiles/sm_animate.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable sm_animate"
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sm_animate.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sm/CMakeFiles/sm_animate.dir/build: sm/sm_animate

.PHONY : sm/CMakeFiles/sm_animate.dir/build

sm/CMakeFiles/sm_animate.dir/requires: sm/CMakeFiles/sm_animate.dir/apps/sm_animate.o.requires

.PHONY : sm/CMakeFiles/sm_animate.dir/requires

sm/CMakeFiles/sm_animate.dir/clean:
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -P CMakeFiles/sm_animate.dir/cmake_clean.cmake
.PHONY : sm/CMakeFiles/sm_animate.dir/clean

sm/CMakeFiles/sm_animate.dir/depend:
	cd /home/xavier/catkin_ws/build/csm && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xavier/catkin_ws/src/csm /home/xavier/catkin_ws/src/csm/sm /home/xavier/catkin_ws/build/csm /home/xavier/catkin_ws/build/csm/sm /home/xavier/catkin_ws/build/csm/sm/CMakeFiles/sm_animate.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sm/CMakeFiles/sm_animate.dir/depend

