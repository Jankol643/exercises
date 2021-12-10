#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/s10-weighted-mean/
# Difficulty: Easy


#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    n = len(X)
    total_sum = 0
    value_sum = 0
    for i in range(n):
        total_sum += X[i] * W[i]
        value_sum += W[i]
    print(round(total_sum/value_sum, 1))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
