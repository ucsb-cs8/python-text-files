#!/usr/bin/env python3

import sys

if len(sys.argv)<2:
    print("""
Please supply a filename when you run this file

For example:
 python3 readFile4.py input.txt
 python3 readFile4.py nums.txt
          """)
    sys.exit(1)

filename = sys.argv[1]
          
with open(filename,"r") as infile:
  data = infile.read()

print("data=",data)
