#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/s10-standard-deviation
# Difficulty: Easy

import math

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    n = len(arr)
    dictionary = {}
    arr.sort()

    # create dictionary with numbers:frequency
    for num in arr:
        if num not in dictionary:
            dictionary[num] = 1
        else:
            dictionary[num] = dictionary[num] + 1
    # find total and mean
    total = 0
    for key, value in dictionary.items():
        total = total + (key * value)
    mean = total/n

    sum_squared_dev = 0
    for i in arr:
        sum_squared_dev += (i - mean) * (i - mean)
    stdev = math.sqrt(sum_squared_dev/n)
    print(stdev)

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
