#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/merge-the-tools
# Difficulty: Medium

def merge_the_tools(string, k):
    ln = len(string)

    for i in range(0, ln, k):
        ss = string[i:i+k]
        sss = []
        for x in ss:
            if x not in sss:
                sss.append(x)
        print(''.join(sss))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
