# Autonomous Ground Vehicle


## Requirements

- ROS Melodic
- Python 2.7
- Opencv 4
- LLvm-7-runtime
- numba 0.45
- imutils
- gfortran
- scikit-learn
- colorama0.3.9
- filterpy
- uvc camera

## How to use

With ROS meolic installed and configured and seted up to workpace, clone this project and
name as desired workspace(catkin_ws), then inside workspace folder install dependencies.

```
rosdep install from src 
```

- On cv bridge is nedded to refernce the folder for tha actual opencv installatiosn if its needed.
- Add user to dialout to have acces to the usb.

```
sudo apt-get -y install libllvm-7-ocaml-dev libllvm7 llvm-7 llvm-7-dev llvm-7-doc llvm-7-examples
```

## install llvm

extracted from (https://github.com/jefflgaol/Install-Packages-Jetson-ARM-Family
)

```

$ wget http://releases.llvm.org/7.0.1/llvm-7.0.1.src.tar.xz
$ tar -xvf llvm-7.0.1.src.tar.xz
$ cd llvm-7.0.1.src
$ mkdir llvm_build_dir
$ cd llvm_build_dir/
$ cmake ../ -DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD="ARM;X86;AArch64"
$ make -j4
$ sudo make install

```
if a problem occurs

```
make ocaml_doc
sudo make install
```

then 

```
$ cd bin/
$ echo "export LLVM_CONFIG=\""`pwd`"/llvm-config\"" >> ~/.bashrc
$ echo "alias llvm='"`pwd`"/llvm-lit'" >> ~/.bashrc
$ source ~/.bashrc
$ sudo pip install llvmlite==0.30.0

```


## install needed modules

```
sudo pip install numba==0.45
pip install imutils
sudo apt install -y gfortran
pip install scikit-learn
pip install colorama==0.3.9
pip install filterpy
install uvc camera
```


### COMPILE

On Workspace just use

```
catkin build 
``` 

or 

```
catkin_make 
```


## List of functions
- [X] Manual control using PS4 controller
- [X] IDLE mode
- [X] People Follow
- [X] Mapping
- [X] Localization