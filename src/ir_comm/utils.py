import pickle
from Phidgets.Devices.IR import IR, IRCode, IRCodeInfo

def filterObject(obj):
	attrs = [e for e in dir(obj) if not e.startswith('_')]
	return dict(zip(attrs, [getattr(obj, e) for e in attrs]))

def saveIRCode(filename, code, code_info):
	c_dict = filterObject(code)
	del c_dict['toString']
	with open(filename, 'w') as f:
		pickle.dump({'code': c_dict, 'code_info': code_info.toCPhidgetIR_CodeInfo()}, f)

def loadIRCode(filename):
	with open(filename, 'r') as f:
		data = pickle.load(f)
		code = IRCode(data['code']['Data'], data['code']['BitCount'])
		code_info = IRCodeInfo(data['code_info'])
		return code, code_info
