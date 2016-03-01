import requests
import json
import timeit

tic = timeit.default_timer()
key = 'testkey'
target = 'http://localhost:64131'
#target = 'https://73.176.245.226'
#target = 'https://podbaydoors.duckdns.org/'
r = requests.get(target, verify=False)
print r
print r.json()
toc = timeit.default_timer()
print tic-toc

tic = timeit.default_timer()
command = {'key':key, 'deviceList':{'kitchen light':{'deviceOn':True,'deviceSetting':10}}}
r = requests.post(target, data = json.dumps(command), verify=False)
print r
print r.json()
toc = timeit.default_timer()
print tic-toc

tic = timeit.default_timer()
command = {'key':key, 'deviceList':{'kitchen light':{'deviceAdjust':'up','deviceAdjustNum':15}}}
r = requests.post(target, data = json.dumps(command), verify=False)
print r
print r.json()
toc = timeit.default_timer()
print tic-toc

