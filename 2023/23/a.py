import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import math
import heapq #heappush heappop
import re

cross = defaultdict(list)
def dfs(length, curr_pos, prev, height):
    if curr_pos[0] == height:
        return length

    best = 0
    for l, next in cross[curr_pos]:
        if not next in prev:
            a = dfs(length + l, next, prev | set([tuple(next)]), height)
            best = max(a, best)
    return best

def q(file, q1):
    G = [list(l.strip()) for l in open(file, 'r')]

    height = len(G) - 1

    start = (0,1)
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    all = [[start, start, 0, 0]] #prev crossroad, curr position, prev_dir, len_from_cross

    while len(all) > 0:
        prev_cross, curr_pos, prev_dir, len_from_cross = all[0]
        all = all[1:]

        if curr_pos[0] == len(G) - 1:
            cross[prev_cross].append([len_from_cross, curr_pos])
            continue
        
        next_d = [[i, d] for i, d in enumerate(dirs) if (not i is (prev_dir+2)%4) and G[curr_pos[0] + d[0]][curr_pos[1] + d[1]] != '#']
        if q1:
            next_d = [[i,d] for i,d in next_d if G[curr_pos[0] + d[0]][curr_pos[1] + d[1]] != '>v<^'[(i+2)%4]]

        if len(next_d) > 1:
            #found crossroad
            if not curr_pos in [b for a,b in cross[prev_cross]]:
                cross[prev_cross].append([len_from_cross, curr_pos])
                prev_cross = curr_pos
                len_from_cross = 0
            else:
                continue #running in circles
        
        for i, d in next_d:
            all.append([prev_cross, (curr_pos[0]+d[0], curr_pos[1]+d[1]), i, len_from_cross + 1])
        
    #exhausitve search through dict:
    best = dfs(0, start, set([tuple(start)]), height)

    return best

if __name__ == "__main__":
    print('Question 1:')
    cross = defaultdict(list)
    file = 'test.txt'
    ans(q(file, True), 'test', copy=False)
    cross = defaultdict(list)
    file = 'input.txt'
    ans(q(file, True), 'input', copy=True)

    print('Question 2:')
    cross = defaultdict(list)
    file = 'test.txt'
    ans(q(file, False), 'test', copy=False)
    cross = defaultdict(list)
    file = 'input.txt'
    ans(q(file, False), 'input', copy=True)