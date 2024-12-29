#!/usr/bin/env python3
import requests
import json

# create a function that takes ip, username, and password
# as positional arguments
# Starting code is the same as challenge_1_final_local.py

def show_version(ip,username, password):
    username=username
    password=password
    ip=ip
    url='http://'+ip+'/ins'


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

    print(response)
    print("")
    print(response['result']['body']['nxos_ver_str'])
    print("")
    print(json.dumps(payload))


if __name__ == '__main__':
    show_version("192.168.68.21","cisco","cisco")
