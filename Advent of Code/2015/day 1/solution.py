#!/usr/bin/env python

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
infile = "input.txt"

with open(infile, "r") as fp:
    input = fp.read()

# Part 1 - Calculating final floor
open_count = input.count('(')
close_count = input.count(")")
print("total chars:", len(input))
print("open count:", open_count)
print("close count:", close_count)
print("Floor (open - close):", open_count - close_count)

# Part 2

count = 0
basement = 0
for i, ch in enumerate(input):
    if ch == '(':
        count += 1
    elif ch == ')':
        count -= 1
    if basement == 0 and count == -1:
        basement = i+1

print ("basement:", basement)