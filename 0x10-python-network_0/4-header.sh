#!/bin/bash
# This script sends a GET request to the given URL with a
# header variable and displays the body of the response

curl -s -H "X-School-User-Id: 98" "$1"
