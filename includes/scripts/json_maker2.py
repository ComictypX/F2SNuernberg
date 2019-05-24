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
        data["max-items"] = number
        with open('includes/scripts/'+file+".json", "w") as jsonFile:
            json.dump(data, jsonFile)

        cmd = 'sudo curl -X GET -s -k -H "Content-Type: application/json" --key RESTTEST_key.pem --cert RESTTEST_cert.pem https://ctpwyd.conti.de:443/data?q=$(cat includes/scripts/{}.json | base64 -)'.format(file)
        os.system(cmd+ '> includes/scripts/{}_Data.json'.format(file))
    for file in datagroup:
        with open("includes/scripts/{}_Data.json".format(file), "r+") as jsonFile2:
            data2 = json.load(jsonFile2)

        batch.append(data2)
    with open("includes/scripts/passer.json", "w") as jsonFile3:
            json.dump(batch, jsonFile3)

    with open("includes/scripts/passer.json", "r+") as jsonFile4:
            data3 = json.load(jsonFile4)
    print(data3)
   
   
print sys.argv[1]
print sys.argv[2]
passer(sys.argv[1], sys.argv[2])