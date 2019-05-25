import json
import os

def data_maker(time, number):
    datagroup = ["gps_query", "accgyr_query", "vehicle_query", "battery_query"]
    for file in datagroup:
        with open(file+".json", "r+") as jsonFile:
            data = json.load(jsonFile)

        data["where"]["TS"][">="]=int(time)#1558536000000000
        data["max-items"] = number
        with open(file+".json", "w") as jsonFile:
            json.dump(data, jsonFile)

        cmd = 'curl -X GET -s -k -H "Content-Type: application/json" --key RESTTEST_key.pem --cert RESTTEST_cert.pem https://ctpwyd.conti.de:443/data?q=$(cat {}.json | base64 -)'.format(file)
        os.system(cmd+ '> {}_Data.json'.format(file))
    pass
