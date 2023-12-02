import sys
sys.path.insert(0, '../..')
from utils import *

import itertools
import re

def cmax(lst):
    if len(lst) > 0:
        return max(lst)
    else:
        return 0

def scenic(lst, curr):
    tot = 0
    for l in lst:
        tot += 1
        if l >= curr:
            return tot
    return tot

def rev(i):
    if i == 1:
        return i
    else:
        return i[::-1]

def q(file):
    tot = 0 

    grid = []
    for l in open(file, 'r').readlines():
        l = digits(l.strip())
        grid.append(l)
    
    max = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            if (x == 0 or y == 0 or x == len(grid) -1 or y == len(grid) - 1):
                tot += 1
                continue
            #q1:
            tot += int(grid[x][y] > cmax(grid[x][:y]) or grid[x][y] > cmax(grid[x][y+1:]) or grid[x][y] > cmax([a[y] for a in grid[:x]]) or grid[x][y] > cmax([a[y] for a in grid[x+1:]]))

            #q2:
            curr = grid[x][y]
            scenic_score = scenic(rev(grid[x][:y]), curr) * scenic(grid[x][y+1:], curr) * scenic(rev([a[y] for a in grid[:x]]), curr) * scenic([a[y] for a in grid[x+1:]], curr)
            
            scenic_score = max(curr, scenic_score)

    return tot, scenic_score

if __name__ == "__main__":
    print('Question 1:')
    file = 'test.txt'
    ans(q(file)[0], 'test', copy=False)
    file = 'input.txt'
    ans(q(file)[0], 'input', copy=True)

    print('Question 2:')
    file = 'test.txt'
    ans(q(file)[1], 'test', copy=False)
    file = 'input.txt'
    ans(q(file)[1], 'input', copy=True)