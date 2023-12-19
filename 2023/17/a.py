# I think my logic is valid, basically dijkstra: evaluate the lowest current value, 
# add new values to the potential to be explored places, dont explore the same state twice.
# The big problem is my choice in datastructure. I use a dict to keep track of seen places, which is fine (maybe just a set is better, because distance is unimportant),
# but use a list for next places, which has to be sorted each time. This result in adding a new item now taking O(n logn) instead of O(logn)
# That said, n does not get bigger than ~3000 so I just let it run for a minute to get the answer

import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re


def q(file):
    G = [[int(x) for x in list(l.strip())] for l in open(file, 'r').read().split('\n') ]
    tot = 0 
    
    
    start = [0,0,0,None,0] #y,x,straight, dir, tot, 
    
    next = [start]
    
    seen = defaultdict() #(y,x) -> tot
    seen2 = defaultdict() #(y,x,straight, dir) -> tot
    
    while len(next) > 0:
        next = sorted(next, key=lambda x: (x[4])) #This should make you sad
        # print(next)

        curr = next[0]
        if curr[0] == len(G) - 1 and curr[1] == len(G[0]) - 1:
            return curr[4]
        
        next = next[1:]
        for dir in [[0,1],[-1,0],[0,-1],[1,0]]:
            check = [curr[0] + dir[0], curr[1] + dir[1]]

            if check[0] < 0 or check[0] >= len(G) or check[1] < 0 or check[1] >= len(G[0]):
                continue

            if not curr[3] == None and (abs(curr[3][0] - dir[0]) == 2 or abs( curr[3][1] -dir[1]) == 2):
                #cant turn back
                continue
            
            heat = G[check[0]][check[1]]

            if dir == curr[3]: #straight
                if curr[2] < 3:
                    key = (check[0], check[1])
                    key2 = (check[0], check[1], curr[2] + 1, tuple(dir))

                    if not key in seen:
                        seen[key] = curr[4] + heat
                        seen2[key2] = curr[4] + heat
                        next.append([check[0], check[1], curr[2] + 1, dir, curr[4] + heat])
                    else:
                        if key2 in seen2 and curr[4] + heat >= seen2[key2]:
                            continue
                        if curr[4] + heat < seen[key] + 20:
                            seen[key] = min(seen[key], curr[4] + heat)
                            seen2[key2] = curr[4] + heat
                            next.append([check[0], check[1], curr[2] + 1, dir, curr[4] + heat])

            else:
                key = (check[0], check[1])
                key2 = (check[0], check[1], 1, tuple(dir))
                if not key in seen:
                    seen[key] = curr[4] + heat
                    seen2[key2] = curr[4] + heat
                    next.append([check[0], check[1], 1, dir, curr[4] + heat])
                else:
                    if key2 in seen2 and curr[4] + heat >= seen2[key2]:
                        continue
                    if curr[4] + heat < seen[key] + 20:
                        seen[key] = min(seen[key], curr[4] + heat)
                        seen2[key2] = curr[4] + heat
                        next.append([check[0], check[1], 1, dir, curr[4] + heat])

    return tot


def q2(file):
    G = [[int(x) for x in list(l.strip())] for l in open(file, 'r').read().split('\n') ]
    tot = 0 
    
    
    start = [0,0,0,None,0] #y,x,straight, dir, tot, 
    
    next = [start]
    
    seen = defaultdict() #(y,x) -> tot
    seen2 = defaultdict() #(y,x,straight, dir) -> tot

    magic = 30 #cars cant be in already seen squares (but with potentially different direction/speed, if heat is greater than best at that square + magic number)
               #There can definitely be inputs constructed for which this does not hold, but it reduces the search space and is good enough
    
    while len(next) > 0:
        next = sorted(next, key=lambda x: (x[4])) #This should make you sad
        # print(next)


        curr = next[0]
        if curr[0] == len(G) - 1 and curr[1] == len(G[0]) - 1:
            if curr[2] >= 4:
                return curr[4]
            else:
                next = next[1:]
                continue
        next = next[1:]
        
        for dir in [[0,1],[-1,0],[0,-1],[1,0]]:
            check = [curr[0] + dir[0], curr[1] + dir[1]]

            if check[0] < 0 or check[0] >= len(G) or check[1] < 0 or check[1] >= len(G[0]):
                continue

            if not curr[3] == None and (abs(curr[3][0] - dir[0]) == 2 or abs( curr[3][1] -dir[1]) == 2):
                #cant turn back
                continue
            
            heat = G[check[0]][check[1]]

            if curr[3] == None or dir == curr[3]: #straight
                if curr[2] < 10:
                    key = (check[0], check[1])
                    key2 = (check[0], check[1], curr[2] + 1, tuple(dir))

                    if not key in seen:
                        seen[key] = curr[4] + heat
                        seen2[key2] = curr[4] + heat
                        next.append([check[0], check[1], curr[2] + 1, dir, curr[4] + heat])
                    else:
                        if key2 in seen2 and curr[4] + heat >= seen2[key2]:
                            continue
                        if curr[4] + heat < seen[key] + magic:
                            seen[key] = min(seen[key], curr[4] + heat)
                            seen2[key2] = curr[4] + heat
                            next.append([check[0], check[1], curr[2] + 1, dir, curr[4] + heat])

            else:
                if curr[2] > 3:
                    key = (check[0], check[1])
                    key2 = (check[0], check[1], 1, tuple(dir))
                    if not key in seen:
                        seen[key] = curr[4] + heat
                        seen2[key2] = curr[4] + heat
                        next.append([check[0], check[1], 1, dir, curr[4] + heat])
                    else:
                        if key2 in seen2 and curr[4] + heat >= seen2[key2]:
                            continue
                        if curr[4] + heat < seen[key] + magic:
                            seen[key] = min(seen[key], curr[4] + heat)
                            seen2[key2] = curr[4] + heat
                            next.append([check[0], check[1], 1, dir, curr[4] + heat])

    return tot

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)
    file = 'test.txt'
    ans(q2(file), 'test', copy=False)
    file = 'test2.txt'
    ans(q2(file), 'test2', copy=False)
    file = 'input.txt'
    ans(q2(file), 'input', copy=True)