#!/usr/bin/env python3

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
infile = "input.txt"

with open(infile, "r") as fp:
    contents = fp.read()

def part_one():
    coords = (0, 0) # starting coordinates
    visited = set([coords])
    for c in contents:
        x, y = coords
        if c == '^':
            coords = (x, y-1)
        elif c == 'v':
            coords = (x, y+1)
        elif c == '<':
            coords = (x-1, y)
        elif c == '>':
            coords = (x+1, y)
        visited.add(coords)

    print("Part 1:", len(visited))

def part_two():
    coords = [(0, 0), (0, 0)] # starting coordinates for Santa and Robo-Santa
    visited = set([(0,0)])
    for n, c in enumerate(contents): # n is the character number, c is the character
        x, y = coords[n%2]
        if c == '^':
            coords[n%2] = (x, y-1)
        elif c == 'v':
            coords[n%2] = (x, y+1)
        elif c == '<':
            coords[n%2] = (x-1, y)
        elif c == '>':
            coords[n%2] = (x+1, y)
        visited.add(coords[n%2])

    print("Part 2:", len(visited))

part_one()
part_two()