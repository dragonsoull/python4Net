#!/usr/bin/env python3

# use the import statement to import the requests package
# use 'import json as an example
import json
import requests

# change the URL the appropriate IP
url='http://192.168.68.78/ins'
# create a variable of username and a variable of password with the
# appropriate value
username = "cisco"
# create the password variable here
password = "cisco"


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
# substitute username and password variable name below
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()
# print the value of the response variable
print(response)
print("")
# Bonus: print just the exact version of the output
print(response["result"]["body"]["nxos_ver_str"])