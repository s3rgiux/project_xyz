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
include sm/CMakeFiles/ld_resample.dir/depend.make

# Include the progress variables for this target.
include sm/CMakeFiles/ld_resample.dir/progress.make

# Include the compile flags for this target's objects.
include sm/CMakeFiles/ld_resample.dir/flags.make

sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o: sm/CMakeFiles/ld_resample.dir/flags.make
sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o: /home/xavier/catkin_ws/src/csm2/sm/apps/ld_resample.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/ld_resample.dir/apps/ld_resample.o   -c /home/xavier/catkin_ws/src/csm2/sm/apps/ld_resample.c

sm/CMakeFiles/ld_resample.dir/apps/ld_resample.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/ld_resample.dir/apps/ld_resample.i"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/xavier/catkin_ws/src/csm2/sm/apps/ld_resample.c > CMakeFiles/ld_resample.dir/apps/ld_resample.i

sm/CMakeFiles/ld_resample.dir/apps/ld_resample.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/ld_resample.dir/apps/ld_resample.s"
	cd /home/xavier/catkin_ws/build/csm/sm && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/xavier/catkin_ws/src/csm2/sm/apps/ld_resample.c -o CMakeFiles/ld_resample.dir/apps/ld_resample.s

sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o.requires:

.PHONY : sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o.requires

sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o.provides: sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o.requires
	$(MAKE) -f sm/CMakeFiles/ld_resample.dir/build.make sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o.provides.build
.PHONY : sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o.provides

sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o.provides.build: sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o


# Object files for target ld_resample
ld_resample_OBJECTS = \
"CMakeFiles/ld_resample.dir/apps/ld_resample.o"

# External object files for target ld_resample
ld_resample_EXTERNAL_OBJECTS =

sm/ld_resample: sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o
sm/ld_resample: sm/CMakeFiles/ld_resample.dir/build.make
sm/ld_resample: sm/libcsm-static.a
sm/ld_resample: sm/CMakeFiles/ld_resample.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xavier/catkin_ws/build/csm/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ld_resample"
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ld_resample.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sm/CMakeFiles/ld_resample.dir/build: sm/ld_resample

.PHONY : sm/CMakeFiles/ld_resample.dir/build

sm/CMakeFiles/ld_resample.dir/requires: sm/CMakeFiles/ld_resample.dir/apps/ld_resample.o.requires

.PHONY : sm/CMakeFiles/ld_resample.dir/requires

sm/CMakeFiles/ld_resample.dir/clean:
	cd /home/xavier/catkin_ws/build/csm/sm && $(CMAKE_COMMAND) -P CMakeFiles/ld_resample.dir/cmake_clean.cmake
.PHONY : sm/CMakeFiles/ld_resample.dir/clean

sm/CMakeFiles/ld_resample.dir/depend:
	cd /home/xavier/catkin_ws/build/csm && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xavier/catkin_ws/src/csm2 /home/xavier/catkin_ws/src/csm2/sm /home/xavier/catkin_ws/build/csm /home/xavier/catkin_ws/build/csm/sm /home/xavier/catkin_ws/build/csm/sm/CMakeFiles/ld_resample.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sm/CMakeFiles/ld_resample.dir/depend

