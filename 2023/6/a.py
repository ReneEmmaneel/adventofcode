import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict
import itertools
import re
from math import *

def f(time, dist):
    wins = 0
    for t in range(time):
        if t * (time - t) > dist:
            wins += 1
    return wins

def q1(file):
    times, dists = [ints(l) for l in open(file, 'r')]

    tot = 1
    for i in range(len(times)):
        tot *= f(times[i], dists[i])
    
    return tot

def q2(file):
    times, dists = [ints(l.replace(' ', '')) for l in open(file, 'r')]

    tot = 1
    for i in range(len(times)):
        tot *= f(times[i], dists[i])
    
    return tot


if __name__ == "__main__":
    print('Question 1:')
    file = 'test.txt'
    ans(q1(file), 'test', copy=False)
    file = 'input.txt'
    ans(q1(file), 'input', copy=True)
    print('Question 2:')
    file = 'test.txt'
    ans(q2(file), 'test', copy=False)
    file = 'input.txt'
    ans(q2(file), 'input', copy=True)