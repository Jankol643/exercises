#!/usr/bin/env python3

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
infile = "input.txt"

dimension_list = list()
with open(infile, "r") as fp:
    for line in fp:
        dimension_list.append(line)

total_paper = 0
total_ribbon = 0

for dimension in dimension_list:
    paper = 0
    l, w, h = dimension.split('x')
    l, w, h = int(l), int(w), int(h)

    # paper
    s1 = l * w
    s2 = l * h
    s3 = w * h
    slack = min(s1, s2, s3)
    wrapping = 2*(s1 + s2 + s3) + slack
    total_paper += wrapping

    # ribbon
    ribbon = min(l+l+w+w, l+l+h+h, w+w+h+h)
    bow = l * w * h
    total_ribbon += (ribbon + bow)

print("Total paper area:", total_paper)
print("Total ribbon length:", total_ribbon)