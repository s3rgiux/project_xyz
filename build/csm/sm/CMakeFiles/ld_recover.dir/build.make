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
include sm/CMakeFiles/ld_recover.dir/depend.make

# Include the progress variables for this target.
include sm/CMakeFiles/ld_recover.dir/progress.make

# Include the compile flags for this target's objects.
include sm/CMakeFiles/ld_recover.dir/flags.make

sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o: sm/CMakeFiles/ld_recover.dir/flags.make
sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o: /home/xavier/catkin_ws/src/csm/sm/apps/ld_recover.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/ld_recover.dir/apps/ld_recover.o   -c /home/xavier/catkin_ws/src/csm/sm/apps/ld_recover.c

sm/CMakeFiles/ld_recover.dir/apps/ld_recover.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/ld_recover.dir/apps/ld_recover.i"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/xavier/catkin_ws/src/csm/sm/apps/ld_recover.c > CMakeFiles/ld_recover.dir/apps/ld_recover.i

sm/CMakeFiles/ld_recover.dir/apps/ld_recover.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/ld_recover.dir/apps/ld_recover.s"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/xavier/catkin_ws/src/csm/sm/apps/ld_recover.c -o CMakeFiles/ld_recover.dir/apps/ld_recover.s

sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o.requires:

.PHONY : sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o.requires

sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o.provides: sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o.requires
	$(MAKE) -f sm/CMakeFiles/ld_recover.dir/build.make sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o.provides.build
.PHONY : sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o.provides

sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o.provides.build: sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o


# Object files for target ld_recover
ld_recover_OBJECTS = \
"CMakeFiles/ld_recover.dir/apps/ld_recover.o"

# External object files for target ld_recover
ld_recover_EXTERNAL_OBJECTS =

sm/ld_recover: sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o
sm/ld_recover: sm/CMakeFiles/ld_recover.dir/build.make
sm/ld_recover: sm/libcsm-static.a
sm/ld_recover: sm/CMakeFiles/ld_recover.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ld_recover"
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ld_recover.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sm/CMakeFiles/ld_recover.dir/build: sm/ld_recover

.PHONY : sm/CMakeFiles/ld_recover.dir/build

sm/CMakeFiles/ld_recover.dir/requires: sm/CMakeFiles/ld_recover.dir/apps/ld_recover.o.requires

.PHONY : sm/CMakeFiles/ld_recover.dir/requires

sm/CMakeFiles/ld_recover.dir/clean:
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -P CMakeFiles/ld_recover.dir/cmake_clean.cmake
.PHONY : sm/CMakeFiles/ld_recover.dir/clean

sm/CMakeFiles/ld_recover.dir/depend:
	cd /home/xavier/catkin_ws/build/csm && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xavier/catkin_ws/src/csm /home/xavier/catkin_ws/src/csm/sm /home/xavier/catkin_ws/build/csm /home/xavier/catkin_ws/build/csm/sm /home/xavier/catkin_ws/build/csm/sm/CMakeFiles/ld_recover.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sm/CMakeFiles/ld_recover.dir/depend

