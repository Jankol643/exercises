#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/python-print
# Difficulty: Easy

if __name__ == '__main__':
    n = int(input())
    print_string = '123'
    if n > 3:
        for i in range(4, n + 1):
            print_string += str(i)
    print(print_string)
