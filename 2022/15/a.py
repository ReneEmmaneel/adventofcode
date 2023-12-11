#Even after some improvements still quite slow (~30s)

import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re
import time


def q(file, row_to_check):
    lines = [l for l in open(file, 'r')]

    cannot = []
    beacons = []

    tot = 0 
    for l in lines:
        l = l.strip()
        sx, sy, bx, by = ints(l)
        
        md = abs(bx - sx) + abs(by - sy)
        # print(ints(l), md)

        if by == row_to_check:
            beacons.append(bx)

        dist_to_row = abs(sy - row_to_check)
        amount_left = md - dist_to_row
        if amount_left >= 0:
            xmin = sx - amount_left
            xmax = sx + amount_left
            cannot.extend(list(range(xmin, xmax + 1)))
            cannot = list(set(cannot))
        print(len(cannot), len(beacons))
        # print(cannot, beacons, len(cannot))
    
    return len(list(set(cannot) - set(beacons)))

def q2(file, max_val):
    def signal(x, y):
        # return f"({x},{y})"
        return x * 4000000 + y

    lines = [l for l in open(file, 'r')]

    beacons = []
    possible = defaultdict(list)

    tot = 0 
    for l in lines:
        l = l.strip()
        sx, sy, bx, by = ints(l)
        
        md = abs(bx - sx) + abs(by - sy)

        beacons.append(signal(bx, by))

        #Get all positions md+1
        for y in range(-1 * md - 1, md + 2):
            xrange = md - abs(y) + 1

            if 0 <= sx - xrange <= max_val and 0 <= sy + y <= max_val:
                possible[sy + y].append(sx - xrange)

            if 0 <= sx + xrange <= max_val and 0 <= sy + y <= max_val:
                possible[sy + y].append(sx + xrange)

    for k in possible.keys():
        possible[k] = sorted(list(set(possible[k])))

    for i, l in enumerate(lines):
        l = l.strip()
        sx, sy, bx, by = ints(l)
        
        md = abs(bx - sx) + abs(by - sy)

        #Get all positions md+1
        for y in range(-1 * md - 1, md + 2):
            xrange = md - abs(y) + 1

            if not sy + y in possible:
                continue

            # possible[sy + y] = list(set(possible[sy + y]) - set(range(, )))
            new = []
            for p in possible[sy + y]:
                if p < sx + (-1 * xrange + 1) or p >= sx + xrange:
                    new.append(p)
            possible[sy + y] = new
            
            if possible[sy + y] == []:
                del possible[sy + y]

    coor = list(possible.items())[0]

    return coor[0] + coor[1][0] * 4000000

if __name__ == "__main__":
    start_time = time.time()

    file = 'test.txt'
    ans(q(file, 10), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, 2000000), 'input', copy=True)
    file = 'test.txt'
    ans(q2(file, 20), 'test', copy=False)
    file = 'input.txt'
    ans(q2(file, 4000000), 'input', copy=True)
    
    print(f"--- {time.time() - start_time} seconds --- (SLOW!)")