#!/bin/bash
# This script sends a request to a given URL and displays the size of the body in bytes

curl -s "$1" | wc -c
