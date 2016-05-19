#!/usr/bin/env python
# Copyright (c) 2013, Oregon State University
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Oregon State University nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL OREGON STATE UNIVERSITY BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Author Dan Lazewatsky/lazewatd@engr.orst.edu

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
		else:
			rospy.logerr("Requested code '%s' not known!" % msg.data)
			print 'available codes:'
			for key in self.codes.keys() :
				print '  ', key

if __name__ == '__main__':
	rospy.init_node('ir_node')
	try:
		transmitter = IRTransmitter(rospy.get_param('~code_dir'))
		rospy.Subscriber('ir_code_name', String, transmitter.code_cb)
		rospy.spin()
	except KeyError:
		rospy.logerr('code_dir parameter is not set')