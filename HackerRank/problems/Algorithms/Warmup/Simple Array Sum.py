#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/simple-array-sum
# Difficulty: Easy

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    array_sum = 0
    for i in ar:
        array_sum += i
    return array_sum

if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    print(result)
