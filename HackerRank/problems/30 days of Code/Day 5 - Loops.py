#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/30-loops
# Difficulty: Easy

# Script will only run in Python 3.6 or higher because f-strings are used

def printMultiples(n) :
    i = 0
    for i in range(1,11) :
        print(f'{n} x {i} = {n*i}')

if __name__ == '__main__':
    n = int(input().strip())
    printMultiples(n)
