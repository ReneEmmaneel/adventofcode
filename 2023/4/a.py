import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict
import itertools
import re

def q(file):
    lines = [l for l in open(file, 'r')]
    q1 = 0 

    extra = defaultdict(lambda: 1)

    for l in lines:
        l = l.strip()
        match, have = l.split('|')
        id = ints(match)[0]
        match = ints(match)[1:]
        have = ints(have)
        
        amount = len(set(match) & set(have))
        
        q1 += int(2**(amount-1))
        
        for i in range(id + 1, amount+id+1):
            extra[i] += extra[id]
        
    return q1, sum(extra.values())

if __name__ == "__main__":
    print('Questions (1,2):')
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)