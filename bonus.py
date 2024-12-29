#!/usr/bin/env python3
#pip install netmiko
from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.68.80",
    username="cisco",
    password="cisco",
)

# Grab output
output = net_connect.send_command('show version')

# Type of output
print("This is the type of output: ")
print(type(output))
print("")

print("This is the full output: ")
# Print out raw output
print(output)
print("")

print("Narrow down on output: ")
# Split string output by return, result in a list
# Then search for 'Cisco IOS Software' in each term
for line in output.split("\n"):
    if "Cisco IOS Software" in line:
        print(line.strip())