import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import math
import heapq #heappush heappop
import re

def above(b2, b1):
    #Return h for how many tiles b2 is above b1
    #negative if not above b1
    
    if all([(b2[i] <= b1[i] <= b2[i+3] or b2[i] <= b1[i+3] <= b2[i+3] or b1[i] <= b2[i] <= b1[i+3] or b2[i] <= b1[i] <= b2[i+3]) for i in range(2)]):
        return b2[2] - b1[5] - 1
    else:
        return -9999
    


def q(file):
    lines = [l for l in open(file, 'r')]
    tot = 0 

    bricks = []
    for l in lines:
        l = l.strip()
        x1, y1, z1, x2, y2, z2 = ints(l)

        bricks.append([x1,y1,z1,x2,y2,z2])
    bricks.sort(key=lambda x: x[2])

    #First fall down
    for i in range(len(bricks)):
        brick1 = bricks[i]
        fall_down = 1000000
        for j, brick2 in enumerate(bricks):
            abov =  above(brick1, brick2)
            if abov > 0:
                fall_down = min(fall_down, abov)
        if fall_down == 1000000:
            fall_down = brick1[2]
        
        bricks[i][2] -= fall_down
        bricks[i][5] -= fall_down

    all = set()

    M = defaultdict(list)

    for i, brick1 in enumerate(bricks):
        curr = set()
        found = 0
        for j, brick2 in enumerate(bricks):
            if i == j:
                continue
            #Check if brick1 directly on top of brick2
            if above(brick1, brick2) == 0:
                found += 1
                curr.add(j)

        for l in curr:
            M[i].append(l)

        if found == 1:
            all.update(curr)

    #Q1
    all_q1 = set()
    for m in M.values():
        if len(m) == 1:
            all_q1.update(m)
    tot_q1 = len(bricks) - len(all_q1)

    #Q2
    tot_q2 = 0
    for i, a in enumerate(list(all)):
        C = M.copy()
        fallen = {a}

        cont = True
        while cont:
            cont = False
        
            for k, v in C.items():
                if len(set(C[k])) - len(set(C[k]) - fallen) > 0:
                    cont = True
                C[k] = set(C[k]) - fallen
            for k, v in C.items():
                if len(v) == 0:
                    fallen.add(k)

        tot_q2 += len(fallen) - 1

    return tot_q1, tot_q2

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)