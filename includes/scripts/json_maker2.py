import json
import sys
import os

def main():
    batch = []
    datagroup = ["gps_query", "accgyr_query", "vehicle_query", "battery_query"]
    for file in datagroup:
        with open(file+".json", "r+") as jsonFile:
            data = json.load(jsonFile)

        data["where"]["TS"][">="]=int(sys.argv[1])#1558536000000000
        data["max-items"] = sys.argv[2]
        with open(file+".json", "w") as jsonFile:
            json.dump(data, jsonFile)

        cmd = 'curl -X GET -s -k -H "Content-Type: application/json" --key RESTTEST_key.pem --cert RESTTEST_cert.pem https://ctpwyd.conti.de:443/data?q=$(cat {}.json | base64 -)'.format(file)
        os.system(cmd+ '> {}_Data.json'.format(file))

        with open("{}_Data.json".format(file), "r+") as jsonFile2:
            data2 = json.load(jsonFile2)

        batch.append(data2)
    with open("passer.json", "w") as jsonFile3:
            json.dump(batch, jsonFile3)

    with open("passer.json", "r+") as jsonFile4:
            data3 = json.load(jsonFile4)
    print(data3)
    