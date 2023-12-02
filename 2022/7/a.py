import sys
sys.path.insert(0, '../..')
from utils import *

import itertools
import re

global_score = 0
def add_total(tree):
    total = 0
    total = sum([x[0] for x in tree[1]])
    for child in tree[2]:
        total += add_total(child)

    if total <= 100000:
        global global_score
        global_score = global_score + total
    return total

current_best = 99999999999999999999
def find_smallest(tree, min):
    total = 0
    total = sum([x[0] for x in tree[1]])
    for child in tree[2]:
        total += find_smallest(child, min)

    global current_best
    if min <= total < current_best:
        current_best = total
    return total

def q(file):
    _outer = ['/', [], [], None]
    current = _outer

    tot = 0 
    is_ls = False
    for l in open(file, 'r').readlines():
        l = l.strip()
        if l.startswith('$ cd /'):
            skip_ls = False
            current = _outer
        else:
            if not l[0] == '$':
                if not skip_ls:
                    a, b = l.split(' ')
                    if a == 'dir':
                        current[2].append([b, [], [], current])
                    else:
                        current[1].append([int(a), b])

            if l[0] == '$':
                skip_ls = False
                cmd = l[2:]
                if cmd.startswith('cd'):
                    dir = cmd[3:]
                    if dir == '..':
                        current = current[3]
                    else:
                        found=False
                        for all in current[2]:
                            if all[0] == dir:
                                current = all
                                found=True
                                break
                        if not found:
                            current[2].append([dir, [], [], current])
                            current = current[2]

                if cmd.startswith('ls'):
                    if len(current[1]) > 0:
                        skip_ls = True

    global global_score
    global current_best

    total = add_total(_outer)
    min = total - 40000000
    total = find_smallest(_outer, min)

    return total, current_best

if __name__ == "__main__":
    print('Question 1:')
    file = 'test.txt'
    ans(q(file)[0], 'test', copy=False)
    file = 'input.txt'
    ans(q(file)[0], 'input', copy=True)

    print('Question 2:')
    file = 'test.txt'
    ans(q(file)[1], 'test', copy=False)
    file = 'input.txt'
    ans(q(file)[1], 'input', copy=True)