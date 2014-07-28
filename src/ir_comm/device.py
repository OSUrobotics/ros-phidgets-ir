from Phidgets.Manager import Manager
from Phidgets.Devices.IR import IR, IRCode, IRCodeInfo
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs, IRCodeEventArgs, IRLearnEventArgs, IRRawDataEventArgs
import time

class ROSIr(object): 
	code_read = False
	def __init__(self):
		self.attach()

	def attach(self):
		m = Manager()
		m.openManager()
		time.sleep(1)
		# print 'There are', len(m.getAttachedDevices()), 'device(s) attached'
		d = m.getAttachedDevices()[0]
		self.ir = IR()
		self.ir.openPhidget(d.getSerialNum())
		# ir.setOnIRCodeHandler(recv)
		# return ir

	def recv_learn_handler(self, e):
		self.code_read = False

	def learn(self):
		self.ir.setOnIRCodeHandler(self.recv_learn_handler)
		while not self.code_read:
			try:
				learned_code = self.ir.getLastLearnedCode()
				self.code_read = True
				return learned_code.Code, learned_code.CodeInfo
			except KeyboardInterrupt:
				return None, None
				break
			except:
				pass
			time.sleep(0.1)