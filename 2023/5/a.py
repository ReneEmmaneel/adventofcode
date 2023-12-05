# I first made q2(), then went back and created a (reverse) brute force solution.
# Should have definitely started with the brute force solution as it took much longer to create q2() than it took for q2_brute() to run

import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict
import itertools
import re

def q1(file):
    #bruteforce
    lines = open(file, 'r').read()
    curr_seeds = ints(lines.split('\n\n')[0])

    maps = [[ints(x) for x in group.split('\n')[1:]] for group in lines.split('\n\n')[1:] ]

    for map in maps:
        new_seeds = []
        for seed in curr_seeds:
            found = False
            for dest,start,length in map:
                if start <= seed < start+length:
                    new_seeds.append(seed - start + dest)
                    found = True
                    break
            if not found:
                new_seeds.append(seed)
        curr_seeds = new_seeds
    
    return min(curr_seeds)
    
def q2_brute(file):
    #bruteforce
    lines = open(file, 'r').read()
    curr_seeds = chunks(ints(lines.split('\n\n')[0]), 2)
    curr_seeds = [[x,x+y] for x,y in curr_seeds]

    maps = [[ints(x) for x in group.split('\n')[1:]] for group in lines.split('\n\n')[1:] ]

    i = 0
    while True:
        i += 1
        seed = i
        for map in maps[::-1]:
            new_seed = None
            for dest,start,length in map:
                if dest <= seed < dest+length:
                    new_seed = seed + start - dest
                    break
            if new_seed is None:
                new_seed = seed
            seed = new_seed
        
        #Check if in range
        for min, max in curr_seeds:
            if min <= seed < max:
                return i


def q2(file):
    lines = [l for l in open(file, 'r')]
    
    maps = []

    curr_seeds = chunks(ints(lines[0]), 2)
    curr_seeds = [[x,y] for x,y in curr_seeds]

    temp_seeds = []
    for seed in curr_seeds:
        seed_min, seed_range = seed
        temp_seeds.append([seed_min, seed_min + seed_range - 1])

    curr_seeds = temp_seeds
    next_seeds = []

    name_ind = 0
    for l in lines[2:]:
        l = l.strip()

        if l == '' or len(l) <= 2:
            continue 

        if ':' in l:
            maps.append([])
        else:
            dest, map_min, map_range = [int(x) for x in l.split(' ')]
            maps[-1].append([dest - map_min, map_min, map_min + map_range - 1])
    
    verbose = False
    for map in maps:
        curr_seeds.sort()
        
        skip_seeds = []
        for m in map:
            map_delta, map_min, map_max = m

            if verbose:
                print('curr seeds: ', curr_seeds)
                print('next seeds: ', next_seeds)
                print('skip seeds: ', skip_seeds)
                print('map:', m)

            for seed in curr_seeds:
                if seed in skip_seeds:
                    continue

                seed_min, seed_max = seed
                
                #Skip mapping for this seed
                if map_max < seed_min or map_min > seed_max:
                    continue

                #Full seed should map
                if map_min <= seed_min and map_max >= seed_max:
                    skip_seeds.append(seed)
                    next_seeds.append([seed_min + map_delta, seed_max + map_delta])
                    continue

                #Left side of seed should map
                if map_min <= seed_min and map_max >= seed_min and map_max < seed_max:
                    left = [seed_min + map_delta, map_max + map_delta]
                    right = [map_max + 1, seed_max]
                    skip_seeds.append(seed)
                    curr_seeds.append(right)
                    next_seeds.append(left)
                    continue
                

                #Right side of seed should map
                if map_min > seed_min and map_min <= seed_max and map_max >= seed_max:
                    left = [seed_min, map_min - 1]
                    right = [map_min + map_delta, seed_max + map_delta]
                    skip_seeds.append(seed)
                    curr_seeds.append(left)
                    next_seeds.append(right)
                    continue
            
                #Map in the middle of seed
                if map_min > seed_min and map_max < seed_max:
                    left = [seed_min, map_min -1]
                    middle = [map_min + map_delta, map_max + map_delta]
                    right = [map_max + 1, seed_max]
                    skip_seeds.append(seed)
                    curr_seeds.append(left)
                    curr_seeds.append(right)
                    next_seeds.append(middle)
                    continue

                print('ERROR!', m, seed) #This was a very usefully print statement during development :)
                
        for seed in curr_seeds:
            if not seed in skip_seeds:
                next_seeds.append(seed)

        if verbose:
            print('==========after all is done=======')
            print('next seeds: ', next_seeds)
            print('=======')

        curr_seeds = next_seeds
        next_seeds = []

    return sorted(curr_seeds)[0][0]

if __name__ == "__main__":
    import time
    start_time = time.time()

    print('Question 1:')
    file = 'test.txt'
    ans(q1(file), 'test', copy=False)
    file = 'input.txt'
    ans(q1(file), 'input', copy=True)
    
    print(f"--- {time.time() - start_time} seconds")
    start_time = time.time()

    print('Question 2 (mapping ranges)')
    file = 'test.txt'
    ans(q2(file), 'test', copy=False)
    file = 'input.txt'
    ans(q2(file), 'input', copy=True)

    print(f"--- {time.time() - start_time} seconds")
    print('===WARNING! Starting bruteforce solution for Q2, this is very slow! (~8min)')
    start_time = time.time()
    
    print('Question 2 (reverse bruteforce)')
    file = 'test.txt'
    ans(q2_brute(file), 'test', copy=False)
    file = 'input.txt'
    ans(q2_brute(file), 'input', copy=True)
    print(f"--- {time.time() - start_time} seconds --- (SLOW!)")