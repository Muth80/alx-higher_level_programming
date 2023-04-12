#!/usr/bin/python3
import sys

TOTAL_SIZE = 0
STATUS_CODES = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin):
        ip, _, _, _, status_code, size = line.split()
        size = int(size)
        TOTAL_SIZE += size
        STATUS_CODES[int(status_code)] += 1
        if (i + 1) % 10 == 0:
            print("File size: {:d}".format(TOTAL_SIZE))
            for code in sorted(STATUS_CODES.keys()):
                if STATUS_CODES[code] != 0:
                    print("{:d}: {:d}".format(code, STATUS_CODES[code]))
            sys.stdout.flush()
except KeyboardInterrupt:
    print("File size: {:d}".format(TOTAL_SIZE))
    for code in sorted(STATUS_CODES.keys()):
        if STATUS_CODES[code] != 0:
            print("{:d}: {:d}".format(code, STATUS_CODES[code]))

