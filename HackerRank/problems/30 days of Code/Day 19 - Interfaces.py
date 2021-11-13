#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/30-interfaces
# Difficulty: Easy

class AdvancedArithmetic(object):

    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    @staticmethod
    def divisorSum(n):
        divisor_sum = 0
        for i in range(1, n + 1):
            if (n % i == 0):
                divisor_sum += i
        return divisor_sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
