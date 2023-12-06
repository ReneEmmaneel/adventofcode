import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict
import itertools
import re

def sign(a,b):
    if a == b:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1

def q(file):
    lines = [l.strip() for l in open(file, 'r')]
    coors = [[ints(coors) for coors in l.split(' -> ')] for l in lines]
    grid = [[0 for _ in range(1000)] for r in range(1000)]

    for coor_line in coors:
        curr = coor_line[0]

        grid[curr[1]][curr[0]] = 1

        for coor in coor_line[1:]:
            while True:
                if coor == curr:
                    break
                dir = [sign(coor[0], curr[0]), sign(coor[1], curr[1])]
                curr[0] += dir[0]
                curr[1] += dir[1]

                grid[curr[1]][curr[0]] = 1

    #Floor for Q2
    max_y = 0
    for line in coors:
        for coor in line:
            if coor[1] > max_y:
                max_y = coor[1]
    max_y += 2

    for i in range(1000):
        grid[max_y][i] = 1


    sand = [0, 500]
    tot = 1
    while sand[1] < 1000:
        y, x = sand

        #Abyss for Q1
        if y >= 999:
            break

        if grid[y+1][x] == 0:
            sand[0] += 1
            continue
    
        if grid[y+1][x] == 1:
            if grid[y+1][x-1] == 0:
                sand[0] += 1
                sand[1] -= 1
                continue
            elif grid[y+1][x+1] == 0:
                sand[0] += 1
                sand[1] += 1
                continue
            else:
                grid[y][x] = 1
                sand = [0, 500]

                #Origin blocked for Q2
                if grid[0][500] == 1:
                    return tot
                
                tot += 1
                continue
    return tot-1
        
            
        

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)