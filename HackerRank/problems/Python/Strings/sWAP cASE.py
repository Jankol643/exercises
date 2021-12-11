#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/python-tuples
# Difficulty: Easy

def swap_case(s):
    final = ''
    for char in s:
        if char.isalpha():
            if char.islower():
                final += char.upper()
            elif char.isupper():
                final += char.lower()
        else:
            final += char
    return final

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)