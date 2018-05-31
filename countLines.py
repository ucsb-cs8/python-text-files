#!/usr/bin/env python3

import sys

if len(sys.argv)<2:
    print("""
Please supply a filename when you run this file

For example:
 python3 {0} input.txt
 python3 {0} nums.txt
          """.format(sys.argv[0]))
    sys.exit(1)

filename = sys.argv[1]

with open("nums.txt","r") as infile:
   linecount = 0
   for line in infile:
       linecount += 1
    
print("line count=",linecount)
