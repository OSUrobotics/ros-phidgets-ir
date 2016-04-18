cmake_minimum_required(VERSION 2.8.3)
project(ir_comm)

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
