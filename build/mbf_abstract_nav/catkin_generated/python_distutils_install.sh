#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/xavier/catkin_ws/src/move_base_flex/mbf_abstract_nav"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/xavier/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/xavier/catkin_ws/install/lib/python2.7/dist-packages:/home/xavier/catkin_ws/build/mbf_abstract_nav/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/xavier/catkin_ws/build/mbf_abstract_nav" \
    "/usr/bin/python2" \
    "/home/xavier/catkin_ws/src/move_base_flex/mbf_abstract_nav/setup.py" \
     \
    build --build-base "/home/xavier/catkin_ws/build/mbf_abstract_nav" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/xavier/catkin_ws/install" --install-scripts="/home/xavier/catkin_ws/install/bin"
