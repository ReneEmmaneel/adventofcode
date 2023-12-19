import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re


def q(file):
    lines = [l for l in open(file, 'r')]
    
    a, b = open(file).read().split('\n\n')
    
    rules = {}
    for rule in a.split('\n'):
        n, R = rule.split('{')
        rules[n] = R.split('}')[0].split(',')
    
    tot = 0
    for line in b.split('\n'):
        part = line[1:].split('}')[0].split(',')
        
        start = 'in'
        stop = False
        while True:
            if start == 'A':
                tot += sum(ints(line))
                break
            elif start == 'R':
                break

            
            for rule in rules[start]:
                found = False
                if ':' in rule:
                    C, goto = rule.split(':')

                    for i, p in enumerate(part):
                        n, val = p.split('=')
                        
                        if ':' in rule:
                            if n in C:
                                evalted = eval(C.replace(n, val))
                                if evalted:
                                    start = goto
                                    found = True
                                    break
                else:
                    start = rule
                    break
                if found:
                    break

    return tot
          
import math 
def q2(file):      
    lines = [l for l in open(file, 'r')]
    
    a, b = open(file).read().split('\n\n')
    
    rules = {}
    for rule in a.split('\n'):
        n, R = rule.split('{')
        rules[n] = R.split('}')[0].split(',')

    curr = ["in", {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000] }]
    all = [curr]

    tot = 0
    fail = 0
    while len(all) > 0:
        curr = all[0]
        all = all[1:]

        if curr[0] == 'A':
            sums = [(b-a)+1 for a,b in curr[1].values()]
            tot += math.prod(sums)
            continue
        elif curr[0] == 'R':
            sums = [(b-a)+1 for a,b in curr[1].values()]
            fail += math.prod(sums)
            continue

        for rule in rules[curr[0]]:
            if ":" in rule:
                C, goto = rule.split(':')
                if '<' in C:
                    c, val = C.split('<')
                    val = int(val)
                    
                    if curr[1][c][0] < val < curr[1][c][1]:
                        curr_dict = curr[1].copy()
                        curr_dict[c] = [curr[1][c][0], val - 1]
                        all.append([goto, curr_dict])
                        curr_dict = curr[1].copy()
                        curr_dict[c] = [val, curr[1][c][1]]
                        all.append([curr[0], curr_dict])
                        break
                    elif curr[1][c][0] < val and curr[1][c][1] < val:
                        curr_dict = curr[1].copy()
                        curr_dict[c] = [curr[1][c][0], curr[1][c][1]]
                        all.append([goto, curr_dict])
                        break
                    else:
                        continue
                        
                elif '>' in C:
                    c, val = C.split('>')
                    val = int(val)
                    
                    if curr[1][c][0] < val < curr[1][c][1]:
                        curr_dict = curr[1].copy()
                        curr_dict[c] = [curr[1][c][0], val]
                        all.append([curr[0], curr_dict])
                        curr_dict = curr[1].copy()
                        curr_dict[c] = [val + 1, curr[1][c][1]]
                        all.append([goto, curr_dict])
                        break
                    elif curr[1][c][0] > val and curr[1][c][1] > val:
                        curr_dict = curr[1].copy()
                        curr_dict[c] = [curr[1][c][0], curr[1][c][1]]
                        all.append([goto, curr_dict])
                        break
                    else:
                        continue
            else:
                all.append([rule, curr[1]])

    print(tot + fail)
    print(4000 ** 4)
    return tot, fail

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)
    file = 'test.txt'
    ans(q2(file), 'test', copy=False)
    file = 'input.txt'
    ans(q2(file), 'input', copy=True)