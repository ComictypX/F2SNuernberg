import json
import sys
import os
import subprocess
import base64

server_key = "/var/www/html/scripts/RESTTEST_key.pem"
server_cert = "/var/www/html/scripts/RESTTEST_cert.pem"

import urllib.parse

#def urlencode(str):
#return urllib.parse.quote(str)

def passer(time, number):
    batch = []
    datagroup = ["gps_query", "accgyr_query", "vehicle_query", "battery_query"]#
    for file in datagroup:
        with open('/var/www/html/scripts/'+file+".json", "r+") as jsonFile:
            data = json.load(jsonFile)
        data["where"]["TS"][">="]=int(time)#1558536000000000
        data["max-items"] = int(number)
        with open('/var/www/html/scripts/'+file+".json", "w") as jsonFile:
            json.dump(data, jsonFile, sort_keys=True)
        test = json.dumps(data).encode()
        #print(test)
        #bencoded = base64.b64encode(test)
        #print(bencoded)
        data = base64.urlsafe_b64encode(test)
        #os.system('cat /var/www/html/scripts/{}.json | base64 -w 0'.format(file) > 
        #cmd2 = urlencode(cmd2)
        print(data)
        cmd = 'curl -X GET -s -k -H "Content-Type: application/json" --key /var/www/html/scripts/RESTTEST_key.pem --cert /var/www/html/scripts/RESTTEST_cert.pem https://ctpwyd.conti.de:443/data?q='+data.decode()
        os.system(cmd+ '> /var/www/html/scripts/{}_Data.json'.format(file))
        
        with open("/var/www/html/scripts/{}_Data.json".format(file), "r+") as jsonFile2:
            data2 = json.load(jsonFile2)

        batch.append(data2)
    return batch
    
# print (json.dumps(passer(sys.argv[1], sys.argv[2]), ensure_ascii = 'False'))
print (passer(sys.argv[1], sys.argv[2]))