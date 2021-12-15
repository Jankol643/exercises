#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/bigger-is-greater
# Difficulty: Medium

from itertools import permutations

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreaterSlow(w):
    p = list(permutations(w))
    perm_list = []
    for perm in p:
        perm = ''.join(perm)
        perm_list.append(perm)
    perm_list.sort()
    found = False
    for perm in perm_list:
        if perm > w and perm != w:
            found = True
            return perm
    if found == False:
        return "no answer"

def biggerIsGreaterFast(w):
    # https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    arr = list(w)
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return 'no answer'

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]

    return "".join(arr)

if __name__ == '__main__':
    T = int(input().strip())
    result_list = []
    for T_itr in range(T):
        w = input()
        result = biggerIsGreaterFast(w)
        print(result)