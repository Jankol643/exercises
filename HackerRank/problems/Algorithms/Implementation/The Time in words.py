#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/the-time-in-words
# Difficulty: Medium


#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    hour_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}
    time_string = ''
    minute_dict = {00: ' o\' clock', 15: 'quarter', 30: 'half', 45: 'quarter'}
    if m in minute_dict:
        minute_string = minute_dict.get(m)
        if m == 00:
            time_string = hour_dict.get(h) + minute_dict.get(m)
            return time_string
        if m <= 30:
            time_string = minute_string + ' past ' + hour_dict.get(h)
        elif m in range(30, 59):
            time_string = minute_string + ' to ' + hour_dict.get(h+1)
    else:
        minute_dict2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                        "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                        "sixteen", "seventeen", "eighteen", "ninteen", "twenty",
                        "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
                        "twenty six", "twenty seven", "twenty eight", "twenty nine"]
        if m < 10:
            minute_string = ' minute'
        elif m in range(10, 59):
            minute_string = ' minutes'
        if m in range(1, 30):
            time_string = minute_dict2[m-1] + minute_string + ' past ' + hour_dict.get(h)
        elif m in range(30, 59):
            time_string = minute_dict2[60-m-1] + minute_string + ' to ' + hour_dict.get(h+1)

    return time_string


if __name__ == '__main__':
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)
