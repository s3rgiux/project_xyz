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
include sm/CMakeFiles/test_json_ld.dir/depend.make

# Include the progress variables for this target.
include sm/CMakeFiles/test_json_ld.dir/progress.make

# Include the compile flags for this target's objects.
include sm/CMakeFiles/test_json_ld.dir/flags.make

sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o: sm/CMakeFiles/test_json_ld.dir/flags.make
sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o: /home/xavier/catkin_ws/src/csm2/sm/apps/test_json_ld.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/test_json_ld.dir/apps/test_json_ld.o   -c /home/xavier/catkin_ws/src/csm2/sm/apps/test_json_ld.c

sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_json_ld.dir/apps/test_json_ld.i"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/xavier/catkin_ws/src/csm2/sm/apps/test_json_ld.c > CMakeFiles/test_json_ld.dir/apps/test_json_ld.i

sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_json_ld.dir/apps/test_json_ld.s"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/xavier/catkin_ws/src/csm2/sm/apps/test_json_ld.c -o CMakeFiles/test_json_ld.dir/apps/test_json_ld.s

sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o.requires:

.PHONY : sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o.requires

sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o.provides: sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o.requires
	$(MAKE) -f sm/CMakeFiles/test_json_ld.dir/build.make sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o.provides.build
.PHONY : sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o.provides

sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o.provides.build: sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o


# Object files for target test_json_ld
test_json_ld_OBJECTS = \
"CMakeFiles/test_json_ld.dir/apps/test_json_ld.o"

# External object files for target test_json_ld
test_json_ld_EXTERNAL_OBJECTS =

sm/test_json_ld: sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o
sm/test_json_ld: sm/CMakeFiles/test_json_ld.dir/build.make
sm/test_json_ld: sm/libcsm-static.a
sm/test_json_ld: sm/CMakeFiles/test_json_ld.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable test_json_ld"
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_json_ld.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sm/CMakeFiles/test_json_ld.dir/build: sm/test_json_ld

.PHONY : sm/CMakeFiles/test_json_ld.dir/build

sm/CMakeFiles/test_json_ld.dir/requires: sm/CMakeFiles/test_json_ld.dir/apps/test_json_ld.o.requires

.PHONY : sm/CMakeFiles/test_json_ld.dir/requires

sm/CMakeFiles/test_json_ld.dir/clean:
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -P CMakeFiles/test_json_ld.dir/cmake_clean.cmake
.PHONY : sm/CMakeFiles/test_json_ld.dir/clean

sm/CMakeFiles/test_json_ld.dir/depend:
	cd /home/xavier/catkin_ws/build/csm && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xavier/catkin_ws/src/csm2 /home/xavier/catkin_ws/src/csm2/sm /home/xavier/catkin_ws/build/csm /home/xavier/catkin_ws/build/csm/sm /home/xavier/catkin_ws/build/csm/sm/CMakeFiles/test_json_ld.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sm/CMakeFiles/test_json_ld.dir/depend

