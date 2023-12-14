#Algorithm for part 2 is basically walk through the loop,
#Add all coordinates to the left or right of this loop,
#Then gridfill from those coordinates.
#There are multiple much easier algorithms for part 2.

import sys
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re


def q(file, is_test):
    lines = [l for l in open(file, 'r').readlines()]

    grid = []

    start = None
    char_to_dirs = {
        ".": [],
        "J": [dirs["L"], dirs["U"]],
        "|": [dirs["U"], dirs["D"]],
        "-": [dirs["L"], dirs["R"]],
        "L": [dirs["U"], dirs["R"]],
        "F": [dirs["D"], dirs["R"]],
        "7": [dirs["D"], dirs["L"]],
        "S": [dirs["D"], dirs["L"]] if is_test else [dirs["L"], dirs["R"]] #hardcoded
    }

    for y, l in enumerate(lines):
        l = l.strip()
        gridline = []
        for x, c in enumerate(list(l)):
            if c == "S":
                start = [y, x]
            gridline.append({"dir": c, "dirs": char_to_dirs[c]})
        grid.append(gridline)

    def c_to_dirs(y,x):
        return grid[y][x]["dirs"]
    def c_to_dirs(list):
        return grid[list[0]][list[1]]["dirs"]
    def c_to_dir(list):
        return grid[list[0]][list[1]]["dir"]
    def c_plus_c(c1, c2):
        return [c1[0] + c2[0],c1[1]+c2[1]]

    prev = start
    curr =  c_plus_c(start, c_to_dirs(start)[0])
    length = 1

    loop = [start]
    while not curr == start:
        loop.append(curr)
        temp = curr

        ndirs = [c_plus_c(curr, c_to_dirs(curr)[0]), c_plus_c(curr, c_to_dirs(curr)[1])]
        for n in ndirs:
            if n == prev:
                continue
            else:
                length += 1
                curr = n
                break

        prev = temp

    def cw_next(dir):
        if dir == "U":
            return "R"
        if dir == "R":
            return "D"
        if dir == "D":
            return "L"
        if dir == "L":
            return "U"
    def ccw_next(dir):
        if dir == "U":
            return "L"
        if dir == "L":
            return "D"
        if dir == "D":
            return "R"
        if dir == "R":
            return "U"


    #Walk through loop, add the elements to inside
    dir_look = "L" if is_test else "D" #hardcoded
    inside = []
    is_hor = False if is_test else True #hardcoded
    for l in loop:
        def add(coor):
            check = c_plus_c(coor, dirs[dir_look])
            if not check in loop and not check in inside:
                inside.append(check)

        match grid[l[0]][l[1]]["dir"]:
            case "|":
                add(l)
            case "-":
                add(l)
            case "L" | "7":
                if is_hor:
                    is_hor = False
                    add(l)
                    dir_look = cw_next(dir_look)
                    add(l)
                else:
                    is_hor = True
                    add(l)
                    dir_look = ccw_next(dir_look)
                    add(l)
            case "F" | "J":
                if is_hor:
                    is_hor = False
                    add(l)
                    dir_look = ccw_next(dir_look)
                    add(l)
                else:
                    is_hor = True
                    add(l)
                    dir_look = cw_next(dir_look)
                    add(l)


    inside_to_look = inside
    inside_to_look_next = []

    #gridfill from inside
    while len(inside_to_look) > 0:
        inside_to_look_next = []
        for ind, i in enumerate(inside_to_look):
            for d in dirs.values():
                l = c_plus_c(i, d)
                if l in inside_to_look or l in loop or l in inside:
                    continue
                else:
                    inside.append(l)
                    inside_to_look_next.append(l)
        inside_to_look = inside_to_look_next

    return (length // 2, len(inside))

if __name__ == "__main__":
    print("Solutions (part1, part2):")
    file = 'test.txt'
    print('test: ', q(file, is_test=True))
    file = 'input.txt'
    print('input: ', q(file, is_test=False))