from device import device

class deviceController:
	#create device objects for all input IPs
	def __init__(self, devicesInit):
		self.devices = {}
		for deviceID in devicesInit.keys():
			self.devices[deviceID] = device(devicesInit[deviceID])

	#list device objects
	def listDevices(self):
		return self.devices.keys()

	#set device. input arg is of the form {<deviceID> : {deviceCh:<deviceCh>, deviceOn : <deviceOn>, deviceSetting : <deviceSetting>},...}
	def setDevices(self, cmdIn):
		#***add input validation here***
		statusOut = {}
		for deviceID in cmdIn.keys():
			if deviceID in self.devices:
				statusOut[deviceID] = self.devices[deviceID].set(cmdIn[deviceID])
			else:
				statusOut[deviceID] = {'error':'invalid device'}
		return statusOut

	#update devices
	def updateDevices(self):
		print 'updating device'
		deviceList = self.devices.keys()
		statusOut = {}
		for deviceID in deviceList:
			statusOut[deviceID] = self.devices[deviceID].updateStatus()
		return statusOut

