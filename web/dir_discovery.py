#!/usr/bin/env python

import requests
from urllib.parse import urljoin

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "http://targeturlhere"
with open("/usr/share/seclists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = urljoin(target_url, word)
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)
