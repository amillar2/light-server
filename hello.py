from flask import Flask, request, jsonify
import json
from deviceClasses.deviceController import deviceController

app = Flask(__name__)
#key to authenticate messages
key = 'testkey'

#initialize device controller with known devices
with open('/var/www/devices.json') as json_data:
	devicesInit = json.load(json_data)
	json_data.close()
dc = deviceController(devicesInit)

 
#On POST, handle control request
#***Add selective get_status here with different URIs***
@app.route('/', methods=['POST'])
def control():
    #Check for JSON command    
    try:
	# We use 'force' to skip imetype checking to have shorter curl command.
    	data = request.get_json(force=True) 
    except:
	return jsonify(error='no JSON command sent')
    # Form of command should be {key:<key>, deviceList:{deviceID:{deviceOn:<deviceOn>, deviceSetting:<deviceSetting>},...}}
    #check key
    if 'key' in data:
    	if data['key'] != key:
		return jsonify(error='invalid application key')
    else:
    	return jsonify(error='no application key in request')
    #Check if deviceList is in request
    if 'deviceList' in data:
    	deviceList = data['deviceList']
    else:
    	return jsonify(error='no devices specified in request')
    #Send request to deviceController
    statusOut = dc.setDevices(deviceList)
    return jsonify(**statusOut)

#On GET, return status of all devices
@app.route('/', methods=['GET'])
def get_status():
	statusOut = dc.updateDevices()
	return jsonify(**statusOut)
#'Can I see the server' test
@app.route('/test/')
def test():
	return 'hello world'

#Enable debug testing if run standaloen 
if __name__ == '__main__':
    app.run(port=64131, debug=True)

