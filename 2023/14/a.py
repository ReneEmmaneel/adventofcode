#Slow...
#Bad
#I had a pretty fast shake algorithm for part 1, but decided to rewrite it for part 2 as this was easier for all 4 directions.
#In hindsight I should have just kept part 1 algorithm
#Also I put all the rocks as input to the dictionary hash, even though just width*height bits are needed.

import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re

D = {}
def shake(rocks, dir, height, width):
    if (rocks, dir) in D:
        return [D[(rocks, dir)], True]

    new_rocks = []
    old_rocks = []

    for r in rocks:
        if r[1] == 'O':
            curr_next_found_pos = r[0]
            curr_next_pos = r[0] + dir

            while 0 <= int(curr_next_pos.real) < width and 0 <= int(curr_next_pos.imag) < height:
                rocks_at_pos1 = [rock for rock in rocks if rock[0] == curr_next_pos and not rock in old_rocks]
                rocks_at_pos2 = [rock for rock in new_rocks if rock[0] == curr_next_pos]
                rocks_at_pos = rocks_at_pos1 + rocks_at_pos2
                # print(curr_next_pos, rocks_at_pos, all_rocks, new_rocks)

                if len(rocks_at_pos) > 0:
                    rock_at_pos = rocks_at_pos[0]
                    if rock_at_pos[1] == 'O':
                        curr_next_pos = curr_next_pos + dir
                    elif rock_at_pos[1] == '#':
                        break
                else:
                    curr_next_found_pos = curr_next_pos
                    curr_next_pos = curr_next_pos + dir
            new_rocks.append((curr_next_found_pos, 'O'))
            old_rocks.append(r)
    
    new_rocks = tuple(sorted(new_rocks + [r for r in rocks if r[1] == '#'], key=lambda x: (x[0].real, x[0].imag)))
    D[(rocks, dir)] = new_rocks
    return [new_rocks, False]
    
def printr(rocks, height, width):
    for y in range(height):
        for x in range(width):
            if (x + y * 1j, '#') in rocks:
                print('#', end='')
            elif (x + y * 1j, 'O') in rocks:
                print('O', end='')
            else:
                print('.', end='')
        print()

def load(rocks, height, width):
    tot = 0 
    for x in range(width):
        col = [r for r in rocks if int(r[0].real) == x and r[1] == 'O']
        tot += sum([height - int(x[0].imag) for x in col])
    return tot         

def q(file):
    #Input -> List<List<complex number>>
    lines = open(file, 'r').read().strip()
    rocks = [(curr_col + curr_row * 1j, x) for curr_row, l in enumerate(lines.split('\n')) for curr_col, x in enumerate(l) if x != '.']

    width = max([int(x[0].real) for x in rocks])+1

    height = len(lines.split('\n'))
    cycles = 1000000000*4
    first_found = False
    i = 0
    
    loads = []
    while i < cycles:
        if i % 100 == 0:
            print(i, len(D))
        if i % 4 == 0:
            dir = 0 - 1j  
        if i % 4 == 1:
            dir = -1
        if i % 4 == 2:
            dir = 0 + 1j
        if i % 4 == 3:
            dir = 1
        rocks, found = shake(tuple(rocks), dir, height, width)
        if first_found:
            if (rocks, found) == cycle:
                cycle_len = i - cycle_start
                aa = (cycles - cycle_start) % cycle_len
                return loads[aa + cycle_start - 1]

        if found and not first_found:
            first_found = True
            cycle_start = i
            cycle = (rocks, found)
            print(i)

        i += 1
        loads.append(load(rocks, height, width))
    return tot

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)