#!/usr/bin/env python3

import subprocess
import os
import sys
import re

# checks if ran as sudo
def is_root():
    return os.geteuid() == 0

# checks if input is valid for mac address
def validate_mac_address(mac_address):
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return re.match(pattern, mac_address)

# changes mac address
def mac_changer(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    try:
        subprocess.run(["ip", "link", "set", "dev", interface, "down"], check=True)
        subprocess.run(["ip", "link", "set", "dev", interface, "address", new_mac], check=True)
        subprocess.run(["ip", "link", "set", "dev", interface, "up"], check=True)
        print("[+] MAC address changed successfully!")
    except subprocess.CalledProcessError as e:
        print("[-] An error occurred:")
        print(e)
        print("Use 'ip link' command to check your interface ether")
        sys.exit(1)

# checks if ran as sudo
if not is_root():
    print("[-] This script requires root privileges. Please run with sudo.")
    sys.exit(1)

# interface input
interface = input("Please select interface (Use 'ip link' command, EX: eth0): ")

# Validate the MAC address before proceeding
new_mac = input("Please type your new MAC address: ")
if not validate_mac_address(new_mac):
    print("[-] Invalid MAC address format. Please use the following format: 00:11:22:33:44:55")
    sys.exit(1)

mac_changer(interface, new_mac)
