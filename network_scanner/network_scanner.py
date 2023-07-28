#!/usr/bin/env python

import scapy.all as scapy
import os
import sys

# checks if ran as sudo
def is_root():
    return os.geteuid() == 0

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast/arp_request  
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

if not is_root():
    print("[-] This script requires root privileges. Please run with sudo.")
    sys.exit(1)


print("Reminder: use this for ethical purposes only!")
ip_to_scan = input("Please enter the ip address and the range(EX: 192.168.1.1/24): ")
scan_result = scan(ip_to_scan)
print_result(scan_result)