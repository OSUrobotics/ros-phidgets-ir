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

import roslib; roslib.load_manifest('ir_comm')
import sys, rospy
from ir_comm.device import ROSIr
from ir_comm.utils import saveIRCode

from threading import Thread
from functools import wraps

def thread(func):
        @wraps(func)
        def wrap(*args, **kwargs):
                t = Thread(target=func, args=args, kwargs=kwargs)
                t.start()
                return t     
        return wrap

@thread
def recv_learn_handler(e):
	import pdb; pdb.set_trace()
	# self.code_read = False


if __name__ == '__main__':
	# if len(sys.argv) != 2:
	# 	print 'Usage: learn.py [filename]'
		# sys.exit(1)
	rospy.init_node('ir_learn')
	ir = ROSIr()
	ir.ir.setOnIRCodeHandler(recv_learn_handler)
	print 'Waiting for code...'
	# code, info = ir.learn()
	# saveIRCode(sys.argv[1], code, info)
	# print 'Wrote code to', sys.argv[1]
	rospy.spin()