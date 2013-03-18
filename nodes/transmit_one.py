#!/usr/bin/env python
import roslib; roslib.load_manifest('ir_comm')
import sys, rospy
from ir_comm.device import ROSIr
from ir_comm.utils import loadIRCode

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Usage: transmit_one.py [filename]'
		sys.exit(1)
	rospy.init_node('ir_transmit_one')
	ir = ROSIr()
	code, info = loadIRCode(sys.argv[1])
	rospy.sleep(1)
	ir.ir.transmit(code, info)
	print 'Transmitted'