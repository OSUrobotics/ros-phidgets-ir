cmake_minimum_required(VERSION 2.8.3)
project(ir_comm)

find_library(PHIDGET_LIB NAMES phidget21 PATHS /usr/lib NO_DEFAULT_PATH)
if(PHIDGET_LIB)
  message(STATUS "Found library phidget21: " ${PHIDGET_LIB})
else()
  message(FATAL_ERROR "phidget21 not found! Please read the readme.")
endif()

find_package(catkin REQUIRED COMPONENTS rospy)

catkin_python_setup()

catkin_package()

install(PROGRAMS
  nodes/ir_node.py
  nodes/learn.py
  nodes/retransmit.py
  nodes/transmit_one.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
