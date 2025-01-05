#!/usr/bin/env python3
from netmiko import ConnectHandler

# Device details
def define_devices(totalNum):
    # self.totalNum = totalNum
    j=1
    devices = []
    while j<=totalNum:
        device={
            "device_type": "cisco_ios",  # Adjust based on your device type (e.g., cisco_nxos for NX-OS)
            "host": "192.168.68.1"+str(j),       # Replace with the device's IP address
            "username": "cisco",         # Replace with your username
            "password": "cisco",      # Replace with your password
            "secret": "cisco", # Optional: Replace with your enable password if required
        }
        devices.append(device)
        j+=1
    return devices

def config_device(device):
        # Connect to the device
    try:
        connection = ConnectHandler(**device)
        connection.enable()  # Enter enable mode if required

        # Commands to configure an IP address
        interface = "Ethernet0/1"  # Replace with your interface name
        ip_address = "10.10.10.1"
        subnet_mask = "255.255.255.0"
        config_commands = [
            f"interface {interface}",
            f"ip address {ip_address} {subnet_mask}",
            "no shutdown",
        ]

        # Send configuration commands
        output = connection.send_config_set(config_commands)
        print(output)

        # Verify the configuration
        verify_command = f"show run interface {interface}"
        verification_output = connection.send_command(verify_command)
        print(verification_output)

        # Disconnect
        connection.disconnect()

    except Exception as e:
        print(f"An error occurred: {e}")

def write_to_memory(devices):    
    for device in devices:
        try:
            connection = ConnectHandler(**device)
            # connection.enable()  # Enter enable mode if required
            connection.send_command("write memory")
            connection.disconnect()
        except Exception as e:
            print(f"An error occurred: {e}")

def disable_secret(devices):
    for device in devices:
        try:
            connection = ConnectHandler(**device)
            connection.enable()  # Enter enable mode if required
            config_commands = "no enable secret"
            output = connection.send_config_set(config_commands)
            print(output)
        except Exception as e:
            print(f"An error occurred: {e}")

def show_interface(devices):
    for device in devices:
        try:
            connection = ConnectHandler(**device)
            connection.enable()  # Enter enable mode if required
            output = connection.send_command("show ip interface brief")
            print(output)
            connection.disconnect()
        except Exception as e:
            print(f"An error occurred: {e}")

# write_to_memory(define_devices(int(input("type in total number of device you want to write memory"))))
devices = define_devices(3)
# disable_secret(devices)
write_to_memory(devices)
