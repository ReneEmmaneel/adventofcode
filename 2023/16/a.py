import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re

def one(grid, width, height, start):
    just_pos = []
    grid_dict = dict(grid)

    tot = 0
    curr_all = [start] #pos, dirr
    seen = curr_all
    while len(curr_all) > 0:
        # print(curr_all)

        curr = curr_all[0]
        if not curr[0] in just_pos:
            tot += 1
            just_pos.append(curr[0])
        
        curr_all = curr_all[1:]

        next_pos = curr[0] + curr[1]
        next_dir = curr[1]
        if (next_pos, next_dir) in seen:
            # print('seen')
            continue

        if next_pos.real < 0 or next_pos.real >= width or next_pos.imag < 0 or next_pos.imag >= height:
            # print('OOB')
            continue

        seen.append((next_pos, next_dir))

        if next_pos in grid_dict:
            c = grid_dict[next_pos]
            if c == "\\":
                next_dir *= 1j if curr[1].imag == 0 else -1j
                curr_all.append([next_pos, next_dir])
            elif c == '/':
                next_dir *= -1j if curr[1].imag == 0 else 1j
                curr_all.append([next_pos, next_dir])
            elif c == '|':
                if curr[1].imag == 0:
                    curr_all.append([next_pos, next_dir * 1j])
                    curr_all.append([next_pos, next_dir * -1j])
                else:
                    curr_all.append([next_pos, next_dir])
            elif c == '-':
                if not curr[1].imag == 0:
                    curr_all.append([next_pos, next_dir * 1j])
                    curr_all.append([next_pos, next_dir * -1j])
                else:
                    curr_all.append([next_pos, next_dir])
            else:
                print(c)
                return
        else:
            curr_all.append([next_pos, next_dir])

    return tot - 1

def q(file):
    grid = [(col * 1j + row, c) for col, line in enumerate(open(file,'r').read().split('\n')) for row, c in enumerate(list(line.strip())) if not c == '.']
    width = max(int(x[0].real) for x in grid) + 1
    height = max(int(x[0].imag) for x in grid) + 1

    max_tot = 0

    #left
    for i in range(height):
        start = [(-1 + i * 1j), (1+0j)]
        tot = one(grid, width, height, start)
        max_tot = max(tot, max_tot)
        print('left | start: ', start, ', tot: ', tot)
    #right
    for i in range(height):
        start = [(width + i * 1j), (-1+0j)]
        tot = one(grid, width, height, start)
        max_tot = max(tot, max_tot)
        print('right | start: ', start, ', tot: ', tot)
    #top
    for i in range(width):
        start = [(i -1j), (0+1j)]
        tot = one(grid, width, height, start)
        max_tot = max(tot, max_tot)
        print('top | start: ', start, ', tot: ', tot)
    #bot
    for i in range(width):
        start = [(i + height * 1j), (0-1j)]
        tot = one(grid, width, height, start)
        max_tot = max(tot, max_tot)
        print('bot | start: ', start, ', tot: ', tot)
    
    return max_tot

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)