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
include sm/CMakeFiles/json_decimate.dir/depend.make

# Include the progress variables for this target.
include sm/CMakeFiles/json_decimate.dir/progress.make

# Include the compile flags for this target's objects.
include sm/CMakeFiles/json_decimate.dir/flags.make

sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o: sm/CMakeFiles/json_decimate.dir/flags.make
sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o: /home/xavier/catkin_ws/src/csm/sm/apps/json_decimate.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/json_decimate.dir/apps/json_decimate.o   -c /home/xavier/catkin_ws/src/csm/sm/apps/json_decimate.c

sm/CMakeFiles/json_decimate.dir/apps/json_decimate.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/json_decimate.dir/apps/json_decimate.i"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/xavier/catkin_ws/src/csm/sm/apps/json_decimate.c > CMakeFiles/json_decimate.dir/apps/json_decimate.i

sm/CMakeFiles/json_decimate.dir/apps/json_decimate.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/json_decimate.dir/apps/json_decimate.s"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/xavier/catkin_ws/src/csm/sm/apps/json_decimate.c -o CMakeFiles/json_decimate.dir/apps/json_decimate.s

sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o.requires:

.PHONY : sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o.requires

sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o.provides: sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o.requires
	$(MAKE) -f sm/CMakeFiles/json_decimate.dir/build.make sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o.provides.build
.PHONY : sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o.provides

sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o.provides.build: sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o


# Object files for target json_decimate
json_decimate_OBJECTS = \
"CMakeFiles/json_decimate.dir/apps/json_decimate.o"

# External object files for target json_decimate
json_decimate_EXTERNAL_OBJECTS =

sm/json_decimate: sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o
sm/json_decimate: sm/CMakeFiles/json_decimate.dir/build.make
sm/json_decimate: sm/libcsm-static.a
sm/json_decimate: sm/CMakeFiles/json_decimate.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable json_decimate"
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/json_decimate.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sm/CMakeFiles/json_decimate.dir/build: sm/json_decimate

.PHONY : sm/CMakeFiles/json_decimate.dir/build

sm/CMakeFiles/json_decimate.dir/requires: sm/CMakeFiles/json_decimate.dir/apps/json_decimate.o.requires

.PHONY : sm/CMakeFiles/json_decimate.dir/requires

sm/CMakeFiles/json_decimate.dir/clean:
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -P CMakeFiles/json_decimate.dir/cmake_clean.cmake
.PHONY : sm/CMakeFiles/json_decimate.dir/clean

sm/CMakeFiles/json_decimate.dir/depend:
	cd /home/xavier/catkin_ws/build/csm && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xavier/catkin_ws/src/csm /home/xavier/catkin_ws/src/csm/sm /home/xavier/catkin_ws/build/csm /home/xavier/catkin_ws/build/csm/sm /home/xavier/catkin_ws/build/csm/sm/CMakeFiles/json_decimate.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sm/CMakeFiles/json_decimate.dir/depend

