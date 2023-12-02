import sys
sys.path.insert(0, '../..')
from utils import lmap, ints, strs, ans

import itertools
import re

def q1(file):
    tot = 0 
    for l in open(file, 'r').readlines():
        l = l.strip()
        fs, sn = l.split(',')
        ff, fs = lmap(int, fs.split('-'))
        sf, ss = lmap(int, sn.split('-'))

        #Check the 2 cases
        tot += int(ff >= sf and fs <= ss or sf >= ff and ss <= fs)
    return tot


def q2(file):
    tot = 0 
    for l in open(file, 'r').readlines():
        l = l.strip()
        fs, sn = l.split(',')
        ff, fs = lmap(int, fs.split('-'))
        sf, ss = lmap(int, sn.split('-'))

        #Check the 4 cases
        tot += int(ff >= sf and ff <= ss or fs >= sf and fs <= ss or sf >= ff and sf <= fs or ss >= ff and ss <= fs)
    
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