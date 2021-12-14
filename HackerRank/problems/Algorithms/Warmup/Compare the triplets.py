#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/compare-the-triplets
# Difficulty: Easy

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return [alice, bob]

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(str(result[0]) + " " + str(result[1]))
