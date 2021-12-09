#!/usr/bin/env python3

if __name__ == '__main__':
    n = int(input())
    temp = input().split()
    arr = list()
    for i in range(n):
        arr.append(int(temp[i]))
    temp2 = list(dict.fromkeys(arr))
    temp2.sort()
    print(temp2[-2]) # penultimate element
