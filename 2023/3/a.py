#The original solution (previous_solution.py) was so messy that I just redid it.
#This way of doing it makes a bit more sense.
#Previous solution looped through the gears for Q2, and also didn't work with duplicate numbers around a gear (luckily it wasn't there in my input).
#This solution just loops through the numbers for both questions, and uses a hashmap to just keep track
#of the amount of numbers around each gear

#Also, just getting the grid/symbols/gears before handling the input makes these kind of things much easier

#(This is however almost 10x as slow btw, probably because of line 49, in the previous solution I only look at the line above and below, much faster)

import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
import itertools
import re

def getAround(y, x):
    return [(y-1, x-1), (y-1, x), (y-1, x+1),
            (y,   x-1),           (y,   x+1),
            (y+1, x-1), (y+1, x), (y+1, x+1)]

def isSymbol(c):
    return not c.isdigit() and not c == '.'

def q(file):
    tot_q1, tot_q2 = 0, 0
    
    grid = []
    symbols = []
    gears = []

    for l in open(file, 'r').readlines():
        l = l.strip()
        symbols.extend([(len(grid), x) for x, c in enumerate(l) if isSymbol(c)])    
        gears.extend([(len(grid), x) for x, c in enumerate(l) if c == '*'])   
        
        grid.append(list(l))

    #Question 1
    #Loop through the numbers, if any around a digit is in symbols, it is a part number and should be counted
    for y in range(len(grid)):
        curr_num = []
        is_part_number = False
        for x, c in enumerate(grid[y] + ['END MARKER']):
            if c.isdigit():
                curr_num.append(c)
                if any([coor for coor in getAround(y,x) if coor in symbols]):
                    is_part_number = True
            else:
                if len(curr_num) > 0 and is_part_number:
                        tot_q1 += int(''.join(curr_num))
                curr_num = []
                is_part_number = False

    #Question 2
    #Same loop, keep track of how many numbers are beside a gear in the gear_map map
    gear_map = {}
    for gear in gears:
        gear_map[gear] = []

    for y in range(len(grid)):
        curr_num = []
        gears_beside = []
        for x, c in enumerate(grid[y] + ['END MARKER']):
            if c.isdigit():
                curr_num.append(c)
                for coor in getAround(y,x):
                    if coor in gears:
                        gears_beside.append(coor)
            else:
                if len(curr_num) > 0:
                    value = int(''.join(curr_num))
                    for gear in list(set(gears_beside)):
                        gear_map[gear].append(value)
                        
                curr_num = []
                gears_beside = []
    
    for key, value in gear_map.items():
        if len(value) == 2:
            tot_q2 += value[0] * value[1]

    return tot_q1, tot_q2

if __name__ == "__main__":
    import time
    start_time = time.time()


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
    
    
    print(f"--- {time.time() - start_time} seconds --- (SLOW!)")