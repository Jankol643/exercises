#!/usr/bin/env python3

import re

if __name__ == '__main__':
    credit_cards = list()
    n = int(input())

    for _ in range(n):
        credit_cards.append(input())

    def is_valid(number):
        allowed_starts = [4, 5, 6]
        # check if number starts with the right digit
        if int(number[0]) not in allowed_starts:
            return False
        # check if number has correct length (without and with hyphens)
        if len(number) < 16 or len(number) > (16 + 3):
            return False
        hyphen_count = number.count('-')
        if hyphen_count > 0:
            # check if the number of hyphens is correct
            if len(number) != (16 + 3) and hyphen_count != 3:
                return False
            # check if numbers are splitted into even chunks
            splitted = number.split('-')
            char_len = []
            for s in splitted:
                char_len.append(len(s))
            if char_len.count(char_len[0]) != len(char_len):
                return False
            without_hyphens = number.replace('-', '')
        else:
            if re.match('\d', number) is None:
                # string contains non-numeric characters other than hyphens
                return False
        # check for four or more consecutive numbers
        if hyphen_count > 0:
            tmp = without_hyphens
        else:
            tmp = number
        regex = r"([\d])\1\1\1"
        if re.search(regex, tmp) is not None:
            return False
        else:
            return True
            
    for i in range(n):
        if is_valid(credit_cards[i]):
            print("Valid")
        else:
            print("Invalid")