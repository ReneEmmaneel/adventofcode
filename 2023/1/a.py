import sys
sys.path.insert(0, '../..')
from utils import lmap, ints, strs

import itertools
import re

nums = ['zero', 'one', 'two', 'three', 'four','five','six','seven','eight','nine']

def q1(file):
    tot = 0
    for l in open(file, 'r').readlines():
        values = [int(c) for c in l if c.isdigit()]

        tot += values[0] * 10 + values[-1]
    return(tot)

def q2(file):
    tot = 0 
    for l in open(file, 'r').readlines():
        values = [(c, int(x)) for c, x in enumerate(l) if x.isdigit()]

        for i in range(10):
            a = [m.start() for m in re.finditer(nums[i], l)]
            if len(a) > 0:
                values.append((int(a[0]), i))
                values.append((int(a[-1]), i))
        
        values.sort()

        tot += values[0][1] * 10 + values[-1][1]
    return(tot)

if __name__ == "__main__":
    file = 'input.txt'
    # file = 'test.txt'

    print(f'Answer to question 1: {q1(file)}')
    print(f'Answer to question 2: {q2(file)}')
