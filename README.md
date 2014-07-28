ros-phidgets-ir
===============

Send/receive ir data with a phidgets ir board

# Installation
 * Dependencies
   * Phidgets Library
     * Download and unpack the [Phidgets Library for Linux](http://www.phidgets.com/downloads/libraries/libphidget.tar.gz)
     * cd into the newly created `libphidget-[whatever]` directory.
     * Compile and install: `./configure; make; sudo make install`
     * Install the udev rule: `cp udev/99-phidgets.rules /etc/udev/rules.d`
   * Python
     * Download the [Python Phidgets Module](http://www.phidgets.com/downloads/libraries/PhidgetsPython.zip)
     * Unpack the archive, cd into the `PhidgetsPython` directory
     * Run `sudo python setup.py install`
 * ROS Package
   * Clone this repository into as `ir_comm` and add it to your `ROS_PACKAGE_PATH`
