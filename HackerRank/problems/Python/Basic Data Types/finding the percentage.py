#!/usr/bin/env python3
#https://www.hackerrank.com/challenges/finding-the-percentage
"""
Reads an list of n student grades and a student to search for and prints the average grade for that student
The grades of each students are entered after the student name separated with spaces
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    NO_SCORES = 3
    DECIMAL_PLACES = 2
    result_format = "{:0." + str(DECIMAL_PLACES) + "f}"
    for key, value in student_marks.items():
        if key == query_name:
            total_score = 0
            for score in student_marks[key]:
                total_score += score
            
            print(result_format.format(total_score/NO_SCORES))
            break
