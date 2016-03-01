import sys
from flask import Flask, request, jsonify
#params includes device state variables and other available inputs
params = {'ch0':{'deviceOn':False, 'deviceSetting':0, 'deviceAdjust':'','deviceAdjustNum':''}, 'ch1':{'deviceOn':False, 'deviceSetting':0, 'deviceAdjust':'', 'deviceAdjustNum':''}}
portArg = sys.argv[1]

app = Flask(__name__)
#status method using GET. no JSON input. returns device and setting
@app.route('/', methods=['GET'])
def status():
	return jsonify(**params)

#control method using POST. deviceSetting is only required JSON input. returns device and setting
#may want to add more input validation (e.g. check deviceID)
@app.route('/', methods=['POST'])
def controlDevices():
        try:
		data = request.get_json(force=True)
		#print 'remoteserver received' #debug received json
		#print data
		ch = data.keys()[0]
	except:
		return jsonify(setResult = 'fail')
        result = 'success'
	adjustValue = 10
	global params
	cmd = data[ch]
        if 'deviceSetting' in cmd.keys():
		try:                
			params[ch]['deviceSetting'] = int(cmd['deviceSetting'])
		except:
			result = 'fail'
	elif 'deviceAdjust' in cmd.keys():
		if 'deviceAdjustNum' in cmd.keys():
			try:
				adjustValue = int(cmd['deviceAdjustNum'])
			except:
				result = 'fail'
		if cmd['deviceAdjust'] == 'up':
			params[ch]['deviceSetting'] += adjustValue
		elif cmd['deviceAdjust'] == 'down':
			params[ch]['deviceSetting'] -= adjustValue
        if 'deviceOn' in cmd:
		if isinstance(cmd['deviceOn'],bool):
			params[ch]['deviceOn'] = cmd['deviceOn']
		else:
                	result = 'fail'
        #print (on, setting)
	return jsonify(setResult=result)

if __name__ == '__main__':
    app.run(debug=True, port=int(portArg))

