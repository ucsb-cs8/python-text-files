#!/usr/bin/env python3

import sys

if len(sys.argv)<2:
    print("""
Please supply a filename when you run this file

For example:
 python3 readFile2.py input.txt
 python3 readFile2.py nums.txt
          """)
    sys.exit(1)

filename = sys.argv[1]
          
infile = open(filename,"r")
data = infile.read()
infile.close()

print("data=",data)
