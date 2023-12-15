import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re

def hash(str):
    l = str.strip()
    val = 0
    for c in list(l):
        val += ord(c)
        val *= 17
        val = val % 256
    return val


def q(file, q1):
    if q1:
        return sum([hash(x) for x in open(file, 'r').read().split(',')])

    l = open(file, 'r').read().strip()

    D = defaultdict(list)
    for x in l.split(','):
        if '=' in x:
            label, focal = x.split('=')
            hashed_label = hash(label)

            found = False
            for x in D[hashed_label]:
                if x[1] == label:
                    x[0] = int(focal)
                    found = True
                    break
            
            if not found:
                D[hashed_label].append([int(focal), label])

        elif '-' in x:
            label = x.split('-')[0]
            hashed_label = hash(label)

            for idx, value in enumerate(D[hashed_label]):
                if value[1] == label:
                    del D[hashed_label][idx]
                    break
    tot = 0
    for k, v in D.items():
        for i, el in enumerate(v):
            tot += (k+1) * (i+1) * el[0]

    return tot

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file, True), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, True), 'input', copy=True)
    file = 'test.txt'
    ans(q(file, False), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, False), 'input', copy=True)