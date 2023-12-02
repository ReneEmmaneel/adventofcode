import sys
sys.path.insert(0, '../..')
from utils import lmap, ints, strs, inter, ans

from functools import reduce
import itertools as iter
import re

print(ord('A'))

def pr(c):
    prio = ord(c) - 96
    if prio < 0:
        prio = ord(c) - 64 + 26
    return prio

def q1(file):
    tot = 0 
    for l in open(file, 'r').readlines():
        l = l.strip()
        fh = l[0:len(l)//2]
        sh = l[len(l)//2:]
        tot += sum(map(lambda x: pr(x), list(set(fh).intersection(set(sh)))))

    return tot

def q2(file):
    tot = 0 
    lines = []
    for l in open(file, 'r').readlines():
        l = l.strip()
        lines.append(l)
        if len(lines) == 3:
            tot += pr(list(reduce(inter, lmap(set, lines)))[0])

            #Initial solution:
            #tot +=  pr(list(set(lines[0]).intersection( set(lines[1])).intersection( set(lines[2])))[0])
            lines = []

    return tot

if __name__ == "__main__":
    print('Question 1')
    file = 'test.txt'
    ans(q1(file), 'test', copy=False)
    file = 'input.txt'
    ans(q1(file), 'input', copy=True)

    print('Question 2')
    file = 'test.txt'
    ans(q2(file), 'test', copy=False)
    file = 'input.txt'
    ans(q2(file), 'input', copy=True)