#!/usr/bin/env python
import roslib; roslib.load_manifest('ir_comm')
import sys, rospy
from ir_comm.device import ROSIr
from ir_comm.utils import loadIRCode
import glob, os
from std_msgs.msg import String

class IRTransmitter(object):
	codes = {}
	def __init__(self, code_dir):
		self.code_dir = code_dir
		self.ir = ROSIr()
		self.load_codes()

	def load_codes(self):
		print 'Loading...'
		for path in glob.glob(self.code_dir + '/*.pkl'):
			name = '_'.join(os.path.split(path)[-1].split('.')[:-1])
			self.codes[name] = loadIRCode(path)
			print '  ', name

	def code_cb(self, msg):
		if msg.data in self.codes:
			self.ir.ir.transmit(*self.codes[msg.data])
			rospy.loginfo('Transmitted %s' % msg.data)

if __name__ == '__main__':
	rospy.init_node('ir_node')
	try:
		transmitter = IRTransmitter(rospy.get_param('~code_dir'))
		rospy.Subscriber('ir_code_name', String, transmitter.code_cb)
		rospy.spin()
	except KeyError:
		rospy.logerr('code_dir parameter is not set')