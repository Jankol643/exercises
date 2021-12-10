#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/s10-basic-statistics
# Difficulty: Easy

dictionary = {}
n = int(input())
numbers = [int(val) for val in input().split()]
numbers.sort()

# create dictionary with numbers:frequency
for num in numbers:
    if num not in dictionary:
        dictionary[num] = 1
    else:
        dictionary[num] = dictionary[num] + 1
# find total and mean
total = 0
for key, value in dictionary.items():
    total = total + (key * value)
mean = total/n
# find median
middle = int(n / 2)
if n % 2:
    median = numbers[int((n + 1) / 2)]
else:
    median = (numbers[middle - 1] + numbers[middle]) / 2
# find mode
freq = 0
mode = 0
for val, count in dictionary.items():
    if count > freq:
        mode = val
        freq = count

    elif count == freq and val < mode:
        mode = val

print(round(mean, 1))
print(round(median, 1))
print(mode)
