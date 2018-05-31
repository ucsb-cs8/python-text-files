#!/usr/bin/env python3

with open("nums.txt","r") as infile:
  data = infile.read()

# Take all the data you read and convert it into a list of strings
  
lines=data.split("\n")

# Convert the list of strings into a list of ints

nums = []
for line in lines:
    num = int(line)
    nums.append(num)

# Print the list of ints
    
print("nums=",nums)
