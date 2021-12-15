#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/encryption
# Difficulty: Medium

import math
from collections import defaultdict


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(text):
    text = text.replace(' ', '')
    sqrt = math.sqrt(len(s))
    upper_limit = math.ceil(sqrt)

    d = defaultdict(str)
    for i in range(0,len(text),upper_limit):
        sub = text[i:i+upper_limit]
        for x in range(len(sub)):
            d[x]+=sub[x]
    return(list(d.values()))

if __name__ == '__main__':
    s = input()
    result = encryption(s)
    print(' '.join(result))