#!/usr/bin/env python
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