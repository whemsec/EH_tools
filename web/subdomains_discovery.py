#!/usr/bin/env python

import requests


def request(url):
    try:
        return  requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
       pass

target_url = "http://targeturlhere"
with open("/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered Subdomain --> " + test_url)