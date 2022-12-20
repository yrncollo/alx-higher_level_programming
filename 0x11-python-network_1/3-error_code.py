#!/usr/bin/python3
"""
Takes in a URL, sends a request to URL, and displays body of response decoded
in utf-8. Manage urllib's error exceptions.
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
