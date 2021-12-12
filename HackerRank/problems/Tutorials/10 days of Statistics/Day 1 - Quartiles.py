#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/s10-quartiles
# Difficulty: Easy

import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(numbers):
    # global variables
    numbers.sort()
    mid = len(numbers) // 2 # floor division

    def median(median_numbers):
        #return np.median(median_numbers) # will work if numpy import is allowed
        middle = len(median_numbers) // 2  # floor division
        if (len(median_numbers) % 2 == 0):  # even or odd
            return (median_numbers[middle-1] + median_numbers[middle]) / 2
        else:
            return median_numbers[middle]

        
    # actual program starts here    
    if (len(numbers) % 2 == 0):    # even or not
        Q1 = median(numbers[:mid])
        Q3 = median(numbers[mid:])
    else:
        # if odd set of numbers
        Q1 = median(numbers[:mid])
        Q3 = median(numbers[mid+1:])

    print(int(Q1))
    print(int(median(numbers)))
    print(int(Q3))

if __name__ == '__main__':
    fptr = sys.stdout   # stdout is already an open stream

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)