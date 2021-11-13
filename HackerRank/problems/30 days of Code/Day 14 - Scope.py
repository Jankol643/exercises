#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/30-scope
# Difficulty: Easy

class Difference():

    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
