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
CMAKE_SOURCE_DIR = /home/xavier/catkin_ws/src/csm2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xavier/catkin_ws/build/csm

# Include any dependencies generated for this target.
include sm/CMakeFiles/sm1.dir/depend.make

# Include the progress variables for this target.
include sm/CMakeFiles/sm1.dir/progress.make

# Include the compile flags for this target's objects.
include sm/CMakeFiles/sm1.dir/flags.make

sm/CMakeFiles/sm1.dir/apps/sm1.o: sm/CMakeFiles/sm1.dir/flags.make
sm/CMakeFiles/sm1.dir/apps/sm1.o: /home/xavier/catkin_ws/src/csm2/sm/apps/sm1.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object sm/CMakeFiles/sm1.dir/apps/sm1.o"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sm1.dir/apps/sm1.o   -c /home/xavier/catkin_ws/src/csm2/sm/apps/sm1.c

sm/CMakeFiles/sm1.dir/apps/sm1.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sm1.dir/apps/sm1.i"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/xavier/catkin_ws/src/csm2/sm/apps/sm1.c > CMakeFiles/sm1.dir/apps/sm1.i

sm/CMakeFiles/sm1.dir/apps/sm1.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sm1.dir/apps/sm1.s"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/xavier/catkin_ws/src/csm2/sm/apps/sm1.c -o CMakeFiles/sm1.dir/apps/sm1.s

sm/CMakeFiles/sm1.dir/apps/sm1.o.requires:

.PHONY : sm/CMakeFiles/sm1.dir/apps/sm1.o.requires

sm/CMakeFiles/sm1.dir/apps/sm1.o.provides: sm/CMakeFiles/sm1.dir/apps/sm1.o.requires
	$(MAKE) -f sm/CMakeFiles/sm1.dir/build.make sm/CMakeFiles/sm1.dir/apps/sm1.o.provides.build
.PHONY : sm/CMakeFiles/sm1.dir/apps/sm1.o.provides

sm/CMakeFiles/sm1.dir/apps/sm1.o.provides.build: sm/CMakeFiles/sm1.dir/apps/sm1.o


# Object files for target sm1
sm1_OBJECTS = \
"CMakeFiles/sm1.dir/apps/sm1.o"

# External object files for target sm1
sm1_EXTERNAL_OBJECTS =

sm/sm1: sm/CMakeFiles/sm1.dir/apps/sm1.o
sm/sm1: sm/CMakeFiles/sm1.dir/build.make
sm/sm1: sm/libcsm-static.a
sm/sm1: sm/CMakeFiles/sm1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable sm1"
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sm1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sm/CMakeFiles/sm1.dir/build: sm/sm1

.PHONY : sm/CMakeFiles/sm1.dir/build

sm/CMakeFiles/sm1.dir/requires: sm/CMakeFiles/sm1.dir/apps/sm1.o.requires

.PHONY : sm/CMakeFiles/sm1.dir/requires

sm/CMakeFiles/sm1.dir/clean:
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -P CMakeFiles/sm1.dir/cmake_clean.cmake
.PHONY : sm/CMakeFiles/sm1.dir/clean

sm/CMakeFiles/sm1.dir/depend:
	cd /home/xavier/catkin_ws/build/csm && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xavier/catkin_ws/src/csm2 /home/xavier/catkin_ws/src/csm2/sm /home/xavier/catkin_ws/build/csm /home/xavier/catkin_ws/build/csm/sm /home/xavier/catkin_ws/build/csm/sm/CMakeFiles/sm1.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sm/CMakeFiles/sm1.dir/depend

