#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/30-conditional-statements
# Difficulty: Easy

def weirdNotWeird(n) :
    if (n % 2 != 0) : # odd number
        print("Weird")
    if (n % 2 == 0) : # even number
        if (n >= 2 and n <= 5) :
            print("Not Weird")
        elif (n >= 6 and n <= 20) :
            print("Weird")
        else:
            print("Not Weird") 

if __name__ == '__main__':
    N = int(input().strip())
    weirdNotWeird(N)
