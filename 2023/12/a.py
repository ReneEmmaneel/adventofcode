#Tried many different ways to make an efficient solution without recursion.
#In the end, functools.cache is the way...
#Takes half a minute, function is called 776k times
#Still very dumb solution: should have used indices of some sort as keys instead of the entire list
#Also had to turn the list into string to make it hashable... which might have been a hint that I shouldnt have done it that way
#Actually disregard that last line, can turn it into a tuple and reduce the time to 1.7 seconds

import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re
import functools


import ast

@functools.cache
def check(springs, nums):
    springs = list(springs)
    nums = list(nums)
    
    result = 0
    if len(springs) == 0:
        if len(nums) == 0:
            result = 1
        else:
            result = 0
    elif len(nums) == 0:
        if any([s == 1 for s in springs]):
            result = 0
        else:
            result = 1
    else:
        if springs[0] == 0:
            result = check(tuple([1] + springs[1:]), tuple(nums)) + check(tuple(springs[1:]), tuple(nums))
        elif springs[0] == -1:
            result = check(tuple(springs[1:]), tuple(nums))
        elif springs[0] == 1:
            end = True
            for i, spring in enumerate(springs):
                if spring == -1:
                    if i == nums[0]:
                        #success:
                        # print('yeah', i, spring, springs, springs[i:])
                        result = check(tuple(springs[i:]), tuple(nums[1:]))
                    else:
                        result = 0
                    end = False
                    break
                elif spring == 0:
                    if i < nums[0]:
                        try:
                            result = check(tuple([1] + springs[i+1:]), tuple([nums[0] - i] + nums[1:]))
                        except:
                            result = 0
                    elif i == nums[0]:
                        #success:
                        # print('nah', i, spring, springs, springs[i:], [-1] + springs[i+1:])
                        result = check(tuple([-1] + springs[i+1:]), tuple(nums[1:]))
                    else:
                        result = 0
                    end = False
                    break
            if end and len(nums) == 1 and i + 1 == nums[0]:
                return 1

    # print(springs, nums, result)
    return result

def q(file, mult=1, verbose=False):
    lines = [l for l in open(file, 'r')]
    tot = 0

    for j, l in enumerate(lines):
        l = l.strip()
        left, right = l.split(' ')
        
        if mult > 1:
            left = '?'.join([left for _ in range(mult)])
        
        right = right + ', '
        if mult > 1:
            right = right * mult
        
        nums = ints(right)
        springs = [-1 if x == '.' else 0 if x == '?' else 1 for x in list(left)]

        result = check(tuple(springs), tuple(nums))
        tot += result
        # print(j, result)

    return tot

if __name__ == "__main__":
    import time
    start_time = time.time()

    file = 'test.txt'
    ans(q(file, 1, False), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, 1, False), 'input', copy=True)
    file = 'test.txt'
    ans(q(file, 5, False), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, 5, False), 'input', copy=True)

    
    print(f"--- {time.time() - start_time} seconds --- (SLOW!)")