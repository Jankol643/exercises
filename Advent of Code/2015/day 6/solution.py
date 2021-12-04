#!/usr/bin/env python3

import os
import re
import numpy as np

PARSER = re.compile(
    r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")


def parse_line(line):
    (instruction, x1, y1, x2, y2) = re.search(PARSER, line).groups()
    return (instruction, int(x1), int(y1), int(x2), int(y2))


def read_file(infile):
    file_lines = list()
    line_endings = []
    with open(infile, "r") as fp:
        for line in fp:
            line_endings.append(repr(fp.newlines))
            file_lines.append(line)

    def yes_or_no(question):
        yes_answer = ['y', 'yes']
        no_answer = ['n', 'no']
        valid = False
        while valid is False:
            reply = str(input(question + ' (y/n): ')).lower().strip()
            if reply[0] in yes_answer:
                valid = True
                return 'y'
            elif reply[0] in no_answer:
                valid = True
                return 'n'

    different_endings = False
    for ending in line_endings:
        if ending != line_endings[0]:
            different_endings = True
            break

    if different_endings == True:
        print("Input file contains different line endings")
        if yes_or_no("Would you like to convert to a correct format?") == 'y':
            with open('testfile.txt', 'w') as wf:
                for line in file_lines:
                    wf.write(line)

    return file_lines


def part1(commands):
    grid = np.zeros((1000, 1000), dtype=bool)
    for (instruction, x1, y1, x2, y2) in commands:
        if instruction == "turn on":
            grid[y1: y2 + 1, x1: x2 + 1] = 1
        elif instruction == "turn off":
            grid[y1: y2 + 1, x1: x2 + 1] = 0
        elif instruction == "toggle":
            grid[y1: y2 + 1, x1: x2 + 1] = np.logical_not(
                grid[y1: y2 + 1, x1: x2 + 1]
            )
        else:
            raise ValueError("Unknown instruction")
    print("Part 1:", np.count_nonzero(grid))
    # Part 1: Answer should be 569999


def part2(commands):
    grid = np.zeros((1000, 1000), dtype=int)
    for (instruction, x1, y1, x2, y2) in commands:
        if instruction == "turn on":
            grid[y1: y2 + 1, x1: x2 + 1] += 1
        elif instruction == "turn off":
            grid[y1: y2 + 1, x1: x2 + 1] -= 1
            grid[y1: y2 + 1, x1: x2 + 1] = np.maximum(
                0, grid[y1: y2 + 1, x1: x2 + 1]
            )
        elif instruction == "toggle":
            grid[y1: y2 + 1, x1: x2 + 1] += 2
        else:
            raise ValueError("Unknown instruction")
    print("Part 2:", np.sum(grid))
    # Part 2: Answer should be 17836115


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    infile = "input.txt"
    file_lines = read_file(infile)
    commands = [parse_line(line) for line in file_lines]
    part1(commands)
    part2(commands)
