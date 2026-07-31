#!/usr/bin/python3
"""Gets GitHub user ID using authentication."""

import requests
import sys


if __name__ == "__main__":
    response = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2])
    )

    data = response.json()

    print(data.get("id"))
