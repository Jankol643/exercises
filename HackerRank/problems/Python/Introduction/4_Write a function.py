#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/write-a-function/problem
# Difficulty: Easy

def is_leap(year):
    """
    Checks if a year is a leap year

    :param year: year to check
    :type year: int
    :return: True if year is a leap year, else False
    :rtype: boolean
    """
    leap = False
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if (is_leap):
        leap = True
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))