import requests, json


class device:
	#load default status values and update status
	def __init__(self, deviceData):
		self.params = {'deviceTarget':deviceData['ip']+':'+str(deviceData['port']), 'deviceCh':deviceData['ch']}
		self.updateStatus()
	#get status from device and update status variables
	def updateStatus(self):
		try:
			r = requests.get(self.params['deviceTarget'])
			returnStatus = r.json()
			if self.params['deviceCh'] in returnStatus.keys():
				deviceStatus = returnStatus[self.params['deviceCh']]
				for returnParam in deviceStatus.keys():
					self.params[returnParam] = deviceStatus[returnParam]
				self.params['deviceStatus'] = 'Online'
			
		except:
			self.params['deviceStatus'] = 'Offline'
		return self.params
	#write command to device
	def set(self, cmdIn):
		cmdOut = {self.params['deviceCh']:{}}
		statusOut = {}
		for validParam in cmdIn.keys(): #loop through cmd keys
			if validParam in self.params.keys():	#check if cmd is valid
				cmdOut[self.params['deviceCh']][validParam] = cmdIn[validParam] #if valid, load cmd into output cmd dict			
		#try to post cmd
		#print 'device.py sending' #debug json command sent
		#print cmdOut
		try:
			r = requests.post(self.params['deviceTarget'], data = json.dumps(cmdOut))
			data = r.json()
			setResult = data['setResult']
		except:
			statusOut['error'] = 'invalid JSON response from device'
			return statusOut
		if setResult == 'success':
			statusOut = self.updateStatus()
		elif setResult == 'fail':
			statusOut['error'] = 'device reported an error'
		else:
			statusOut['error'] = 'invalid result response from device'
		return statusOut

