import requests
import json
import timeit

tic = timeit.default_timer()
target = 'http://localhost:5000'
#target = 'https://73.176.245.226'
#target = 'https://podbaydoors.duckdns.org/'
r = requests.get(target)
print r
print r.json()
toc = timeit.default_timer()
print tic-toc

tic = timeit.default_timer()
command = {'ch0':{'deviceOn':True, 'deviceSetting':10}}
r = requests.post(target, data = json.dumps(command), verify=False)
print r
print r.json()
toc = timeit.default_timer()
print tic-toc

tic = timeit.default_timer()
command = {'deviceCh':'ch0'}
target = 'http://localhost:5000'
#target = 'https://73.176.245.226'
#target = 'https://podbaydoors.duckdns.org/'
r = requests.get(target, data= json.dumps(command), verify=False)
print r
print r.json()
toc = timeit.default_timer()
print tic-toc

tic = timeit.default_timer()
command = {'deviceCh':'ch1'}
target = 'http://localhost:5000'
#target = 'https://73.176.245.226'
#target = 'https://podbaydoors.duckdns.org/'
r = requests.get(target, data= json.dumps(command), verify=False)
print r
print r.json()
toc = timeit.default_timer()
print tic-toc

tic = timeit.default_timer()
command = {'ch1':{'deviceOn':True,'deviceAdjust':'up', 'deviceAdjustNum':15}}
r = requests.post(target, data = json.dumps(command), verify=False)
print r
print r.json()
toc = timeit.default_timer()
print tic-toc

tic = timeit.default_timer()
command = {'deviceCh':'ch1'}
target = 'http://localhost:5000'
#target = 'https://73.176.245.226'
#target = 'https://podbaydoors.duckdns.org/'
r = requests.get(target, data= json.dumps(command), verify=False)
print r
print r.json()
toc = timeit.default_timer()
print tic-toc

