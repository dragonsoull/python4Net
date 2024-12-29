#!/usr/bin/env python3

import requests
import json
from netmiko import ConnectHandler

# 1. Create a device list
devices = ["192.168.68.11","192.168.68.12","192.168.68.13","192.168.68.14","192.168.68.15"]
# 2. Create a for loop for the devices 

for device in devices:
    url=device
    username='cisco'
    password='cisco'

    net_connect = ConnectHandler(
    device_type="cisco_ios",
    host=device,
    username="cisco",
    password="cisco",
)

    response = net_connect.send_command("show version")

    print("")
    # print(response)
    # print(response['result']['body']['sys_ver_str'])
    for line in response.split("\n"):
        if "Cisco IOS Software" in line:
            print(line.strip())
