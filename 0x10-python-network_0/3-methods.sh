#!/bin/bash
# This script displays all HTTP methods accepted by the server for the given URL

curl -sI "$1" | awk '/^Allow:/{print $2}'

