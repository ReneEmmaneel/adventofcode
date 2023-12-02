import sys
sys.path.insert(0, '../..')
from utils import *

import itertools
import re

def q(file, amount):
    tot = 0 
    for l in open(file, 'r').readlines():
        l = l.strip()
        
        for i in range(len(l)):
            if len(list(set(l[i:i+amount]))) == amount:
                return i+amount
        
    return tot

if __name__ == "__main__":
    print('Question 1:')
    file = 'test.txt'
    ans(q(file, 4), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, 4), 'input', copy=True)
    print('Question 2:')
    file = 'test.txt'
    ans(q(file, 14), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, 14), 'input', copy=True)