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

# Usage
## Learning Codes
    python nodes/learn.py [output file].pkl
    
Point the original remote at the the phidgets device and press the desired button until you see the message `Wrote code to [output file].pkl`. If it isn't working, move the remote closer or farther from the phidgets device.

## Testing Codes
    python nodes/transmit_one.py [code file]
