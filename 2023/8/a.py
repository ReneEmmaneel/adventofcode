# VERY IMPORTANT ASSUMPTIONS!
# 1. the ghost are on a cycle from the start to end with no run up to that cycle
# 2. length of instruction is a divisor for the cycle length
# 3. There is exactly 1 end note in the cycle
#
# Those two assumptions must be made for the LCM to be sufficient for solving
# The general case is much more difficult:
# 1. You have to keep track when the ghost is in an actual cycle (cycle can be up to #instructions * #nodes)
# 2. You have to keep track of the offset when the ghost gets into that cycle + any end notes in that runup
# 3. You have to handle multiple end nodes in that cycle, and keep track of that
# 4. When done, you could calculate it somehow, or make a pretty fast bruteforce solution

import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import math
import re


def q(file):
    lines = [l.strip() for l in open(file, 'r')]
    path = [0 if l == 'L' else 1 for l in list(lines[0])]

    d = defaultdict(str)
    for l in lines[2:]:
        s, l, r = re.findall(r"\w+", l)
        d[s] = [l,r]
    
    curr_pos = [s for s in d.keys() if s[-1] == 'A']

    #Keep record of first time every ghost has find the Z
    first_found = [0 for i in range(len(curr_pos))]

    step = -1
    while True:
        step += 1
        instruction = path[step % len(path)]
        
        #Update first found if first time a ghost is on an end node
        first_found = [step if (pos[-1] == 'Z' and ff == 0) else ff 
                       for pos, ff in zip(curr_pos, first_found)]

        #Update ghost positions
        curr_pos = [d[s][instruction] for s in curr_pos]
        
        #When all ghosts have found the exit, calculate the solution !WITH BIG ASSUMPTIONS MADE!
        if not any([f == 0 for f in first_found]):
            return math.lcm(*first_found)

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)