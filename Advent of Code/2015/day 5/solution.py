#!/usr/bin/env python3

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
infile = "input.txt"

file_lines = list()
with open(infile, "r") as fp:
    for line in fp:
        file_lines.append(line)

def is_nice(s):
    # check for vowels
    vowels = 0
    for c in s:
        if c in 'aeiou':
            vowels += 1
        if vowels >= 3:
            break
    if vowels < 3:
        return False
    # check for letters in a row
    repeat = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeat = True
            break
    if not repeat:
        return False
    forbidden_strings = ['ab', 'cd', 'pq', 'xy']
    if any(substring in s for substring in forbidden_strings):
        return False
    return True

def is_really_nice(s):
    first = False
    for i in range(len(s) - 3):
        sub = s[i: i + 2]
        if sub in s[i + 2:]:
            first = True
            break
    if not first:
        return False
    second = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            second = True
            break
    return second

count1 = 0
count2 = 0
for s in file_lines:
    if is_nice(s):
        count1 += 1
    if is_really_nice(s):
        count2 += 1
print(count1)
print(count2)