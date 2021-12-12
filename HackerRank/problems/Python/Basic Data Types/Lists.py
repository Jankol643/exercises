#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/python-lists
# Difficulty: Easy

if __name__ == '__main__':
    lst = list()
    commands_input = []
    n = int(input())
    for i in range(n):
        commands_input.append(input())

    for line in commands_input:
        splitted = line.split(' ')
        command = splitted[0]
        if len(splitted) > 1:
            integer = int(splitted[1])
            if len(splitted) > 2:
                idx = int(splitted[2])
        if command == 'insert':
            lst.insert(integer, idx)
        elif command == 'print':
            print(lst)
        elif command == 'remove':
            lst.remove(integer)
        elif command == 'append':
            lst.append(integer)
        elif command == 'sort':
            lst.sort()
        elif command == 'pop':
            lst.pop()
        elif command == 'reverse':
            lst.reverse()
