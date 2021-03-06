#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/30-operators
# Difficulty: Easy

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    costAfterTip = meal_cost * tip_percent/100
    costAfterTax = meal_cost * tax_percent/100
    total_cost = meal_cost + costAfterTip + costAfterTax
    roundedTotal = round(total_cost)
    print(roundedTotal)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
