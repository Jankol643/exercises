#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/30-exceptions-string-to-integer
# Difficulty: Easy


# deleted '__name__ == "__main__"' because first word of line must not be used

def toInteger(S):
    try:
        print(int(S))
    except ValueError:
        print("Bad String")

S = input().strip()
toInteger(S)
