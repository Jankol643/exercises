#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/kaprekar-numbers
# Difficulty: Easy


def kaprekarNumbers(p, q):
    numlist = []
    for i in range(p, q + 1):
        if i == 1:
            numlist.append(i)
        elif i**2 > 9:
            numstring = str(i**2)
            rem = len(numstring) - len(str(i))
            left = numstring[:rem]
            right = numstring[rem:]
            if int(left) + int(right) == i:
                numlist.append(i)

    if len(numlist) == 0:
        print("INVALID RANGE")
    else:
        for i in range(len(numlist)):
            print(numlist[i], end=' ')


if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)
