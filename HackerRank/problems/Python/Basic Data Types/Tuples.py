#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/python-tuples
# Difficulty: Easy

if __name__ == '__main__':
    n = int(input())
    ints = input().split()
    t = tuple(int(i) for i in ints)
    print(hash(t))