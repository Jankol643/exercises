#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/extra-long-factorials
# Difficulty: Medium


#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

# no special datatype needed because python has no limit for int
# (https://docs.python.org/3/whatsnew/3.0.html#integers)
def extraLongFactorials(n):

    def fact(n):
        if(n == 1):
            return 1
        prod = n*fact(n-1)
        return prod

    print(fact(n))


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
