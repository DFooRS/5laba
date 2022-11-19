#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("Seasons:\n1 - winter\n2 - spring\n3 - summer\n4 - autumn\n")
    n = int(input("Enter season: "))

    if n == 1:
        print("December, January, February")
    elif n == 2:
        print("March, April, May")
    elif n == 3:
        print("June, July, August")
    elif n == 4:
        print("September, October, November")
    else:
        print("Error!", file=sys.stderr)
        exit(1)
