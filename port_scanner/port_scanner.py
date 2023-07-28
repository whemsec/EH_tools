#!/usr/bin/env python

import socket
from IPy import IP

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        try:
            return socket.gethostbyname(ip)
        except socket.gaierror:
            return None

def get_banner(s):
    try:
        return s.recv(1024).decode().strip('\n')
    except socket.timeout:
        return None

def scan_port(ipaddress, port):
    try:
        with socket.socket() as sock:
            sock.settimeout(0.5)
            if sock.connect_ex((ipaddress, port)) == 0:
                banner = get_banner(sock)
                if banner:
                    print(f"[+] Port {port} is open: {banner}")
                else:
                    print(f"[+] Port {port} is open")
    except Exception as e:
        print(f"[-] Error while scanning port {port}: {e}")

def scan(target):
    converted_ip = check_ip(target)
    if converted_ip is None:
        print(f"[-] Invalid target: {target}")
        return

    print(f"\n[+] Scanning Target: {target}")
    for port in range(1, 1001):
        scan_port(converted_ip, port)

if __name__ == "__main__":
    targets = input("[+] Enter Target/s To Scan (split multiple targets with ,): ")
    target_list = [target.strip() for target in targets.split(",")]
    for target in target_list:
        scan(target)
