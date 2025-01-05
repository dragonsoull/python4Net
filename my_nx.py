#!/usr/bin/env python3
import requests
import json

# create a function that takes ip, username, and password
# as positional arguments
# Starting code is the same as challenge_1_final_local.py

#defind Device class    
class Device:
   def __init__(self,ip,username,password):
      self.ip = ip
      self.username = username
      self.password = password
      self.url='http://'+self.ip+'/ins'
      self.header={'content-type':'application/json-rpc'}

      

# def device(self,ip,username,password):
#     self.ip = ip
#     self.username = username
#     self.password = password
#     self.url='http://'+device.ip+'/ins'
#     self.header={'content-type':'application/json-rpc'}
    
#     return self
    
iplist=['192.168.68.11','192.168.68.12','192.168.68.13']
def deviceList(iplist):
  devices=[]
  for ip in iplist:
    # device(device,ip,"cisco","cisco")
    devices.append(Device(ip,'cisco','cisco'))
  for dev in devices:
     print(dev.url)
  return devices


def exe_command(iplist,command):
   devices=deviceList(iplist)
   for device in devices:
      payload=[
        {
          "jsonrpc": "2.0",
          "method": "cli",
          "params": {
          "cmd": str(command),
          "version": 1.2
          },
          "id": 1
        }
      ]
      # username=device.username
      # password=device.password
      # response=requests.post(device.url,data=json.dumps(payload),headers=device.header,auth=(device.username,device.password)).json()
      response = requests.post(device.url,data=json.dumps(payload),headers=device.header,auth=(device.username,device.password)).json()
      print("")
      print(response)

def exe_commandList(iplist,commandlist):
   devices=deviceList(iplist)
   for device in devices:
      payload=[]
      for command in commandlist:
        payload.append(
          {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
            "cmd": str(command),
            "version": 1.2
            },
            "id": 1
          }
        )
      # username=device.username
      # password=device.password
      # response=requests.post(device.url,data=json.dumps(payload),headers=device.header,auth=(device.username,device.password)).json()
      print("===========================================")
      print(payload)

      response = requests.post(device.url,data=json.dumps(payload),headers=device.header,auth=(device.username,device.password)).json()
      print("")
      print("===========================================")

      print(response)
      # print("payload------begin--here----------------") 
      # print(payload)       
    
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


# if __name__ == '__main__':
#   #  exe_commandList(iplist,["interface Ethernet1/4","no switchport","show interface mgmt 0"])
#    exe_commandList(iplist,["show interface mgmt 0"])

#   #  show_version("192.168.68.11","cisco","cisco")
#   save_config(deviceList(["192.168.68.11","192.168.68.12"]))
