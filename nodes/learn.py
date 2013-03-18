#!/usr/bin/env python
import roslib; roslib.load_manifest('ir_comm')
import sys, rospy
from ir_comm.device import ROSIr
from ir_comm.utils import saveIRCode

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Usage: learn.py [filename]'
		sys.exit(1)
	rospy.init_node('ir_learn')
	ir = ROSIr()
	print 'Waiting for code...'
	code, info = ir.learn()
	if info.MinRepeat == 1: info.MinRepeat = 2
	saveIRCode(sys.argv[1], code, info)
	print 'Wrote code to', sys.argv[1]