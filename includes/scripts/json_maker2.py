import json
import sys
import os

def passer(time, number):
    batch = []
    datagroup = ["gps_query"]#, "accgyr_query", "vehicle_query", "battery_query"
    for file in datagroup:
        with open('includes/scripts/'+file+".json", "r+") as jsonFile:
            data = json.load(jsonFile)

        data["where"]["TS"][">="]=int(time)#1558536000000000
        data["max-items"] = int(number)
        with open('includes/scripts/'+file+".json", "w") as jsonFile:
            json.dump(data, jsonFile, sort_keys=True)

        cmd = 'sudo curl -X GET -s -k -H "Content-Type: application/json" --key includes/scripts/RESTTEST_key.pem --cert includes/scripts/RESTTEST_cert.pem https://ctpwyd.conti.de:443/data?q=$(cat includes/scripts/{}.json | base64 -w 0)'.format(file)
        os.system(cmd+ '> includes/scripts/{}_Data.json'.format(file))
        
        with open("includes/scripts/{}_Data.json".format(file), "r+") as jsonFile2:
            data2 = json.load(jsonFile2)

        batch.append(data2)
    return str(batch[0]['result']['data'])
print (json.dumps(passer(sys.argv[1], sys.argv[2])))