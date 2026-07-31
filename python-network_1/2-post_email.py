#!/usr/bin/python3
"""Sends an email using a POST request."""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode(
        {"email": sys.argv[2]}
    ).encode("utf-8")

    request = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
