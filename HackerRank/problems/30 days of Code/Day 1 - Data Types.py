#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/30-data-types
# Difficulty: Easy

# HackerRank Python
# 30 days
# Day 1 - Data types

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.
int_var = int(input())
double = float(input())
string = input()
# Print the sum of both integer variables on a new line.
print(i + int)
# Print the sum of the double variables on a new line.
print("{:.{}f}".format(d+double, 1)) # print result rounded to one decimal digit
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first
print(s+string)
