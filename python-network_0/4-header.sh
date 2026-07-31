#!/bin/bash
# Sends a GET request with a custom header
curl -H "X-HolbertonSchool-User-Id: 98" -s "$1"
