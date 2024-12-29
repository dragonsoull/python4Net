#!/usr/bin/env python3

import requests
import json

# 1. Create a device list
devices = ["192.168.68.21","192.168.68.22","192.168.68.23"]
# 2. Create a for loop for the devices 

for device in devices:
    url="http://"+device+"/ins"
    # print(url)
    username='cisco'
    password='cisco'

    myheaders={'content-type':'application/json-rpc'}
    payload=[
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
        "cmd": "show version",
        "version": 1.2
        },
        "id": 1
    }
    ]
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username, password)).json()

    print("")
    # print(device)
    print(response['result']['body']['nxos_ver_str'])
