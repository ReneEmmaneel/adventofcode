import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict
import itertools
import re

def print_grid(grid):
    for row in grid:
        for y in row:
            print('.' if y is None else chr(y), end='')
        print()

def q(file, q1):
    tot = 0 
    grid = []
    for l in open(file, 'r').readlines():
        if q1:
            grid.append([ord('a') if (x == 'S' or x == 'a') else ord(x) if not x.isupper() else ord('z')+1 for x in list(l.strip())  ])
        else:
            grid.append([ord('a')-1 if (x == 'S') else ord(x) if not x.isupper() else ord('z')+1 for x in list(l.strip())  ])
    
    new_poss = []
    poss = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if q1:
                if grid[y][x] == ord('a'):
                    poss.append([y,x])

            else:
                if grid[y][x] == ord('a')-1:
                    grid[y][x] = ord('a')
                    poss.append([y,x])

    for i in range(5000):
        poss = [list(x) for x in set(tuple(x) for x in poss)]

        for pos in poss:
            c = grid[pos[0]][pos[1]]
            if c == None:
                continue

            if c == ord('z')+1:
                return i
            grid[pos[0]][pos[1]] = None
            for d in dirs.values():
                y = pos[0] + d[0]
                x = pos[1] + d[1]
                
                if x < 0 or len(grid[0]) <= x or y < 0 or len(grid) <= y:
                    continue
                go = grid[y][x]
                if go is not None and go <= c+1:
                    new_poss.append([y, x])
        poss = new_poss
        new_poss = []
        
    return tot

if __name__ == "__main__":
    print('Question 1:')
    file = 'test.txt'
    ans(q(file, False), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, False), 'input', copy=True)
    print('Question 2:')
    file = 'test.txt'
    ans(q(file, True), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, True), 'input', copy=True)