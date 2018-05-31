#!/usr/bin/env python3


with open("nums.txt","r") as infile:
   # Accumulate list of ints, one per line
   nums = [] 
   for line in infile:
       num = int(line)  # convert this line to int
       nums.append(num)
    
print("nums=",nums)
