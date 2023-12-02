import sys
sys.path.insert(0, '../..')
from utils import lmap, ints, strs, chunks, ans

import itertools
import re

def q(file, test, q1):
    lines = []
    for l in open(file, 'r').readlines():
        lines.append(l)
    l = lines

    stacks = [[] for _ in range(9) ]

    for i in range(9):
        input = list(chunks(l[i], 4))
        for si, c in enumerate(input):
            if not c[0]=='[':
                continue
            c = c[1]
            stacks[si].insert(0, c)

    for l in lines[5 if test else 10:]:
        a, s, e = ints(l)
        stacks[e-1].extend(stacks[s-1][-a:][::-1 if q1 else 1])
        stacks[s-1] = stacks[s-1][:-a]

    return ''.join([x[-1] for x in stacks if len(x) > 0])

if __name__ == "__main__":
    print('Question 1')
    file = 'test.txt'
    ans(q(file, True, True), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, False, True), 'input', copy=True)
    print('Question 2')
    file = 'test.txt'
    ans(q(file, True, False), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, False, False), 'input', copy=True)