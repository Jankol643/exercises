#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/zipped
# Difficulty: Easy

total_sub, total_student = input().split()

all_marks = []

for i in range(int(total_student)):
    all_marks.append([float(i) for i in input().split()])

for i in list(zip(*all_marks)):
    a = (sum(i)) / int(total_student)
    print(round(a, 1))
