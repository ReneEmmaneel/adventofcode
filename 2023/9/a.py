import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re


def q(file):
    lines = [l for l in open(file, 'r')]
    tot_first = tot_last = 0

    for l in lines:
        curr_diff = ints(l)

        first = curr_diff[0]
        last = curr_diff[-1]

        counter = 0
        while not max(curr_diff) == min(curr_diff):
            curr_diff = [curr_diff[i+1] - curr_diff[i] for i in range(len(curr_diff) - 1)]
            
            last += curr_diff[-1]

            #For left extrapolate, we need to keep track of the sign, which flips after each step
            counter += 1
            first += curr_diff[0] * (int(counter % 2 == 0) * 2 - 1)
        
        tot_first += first
        tot_last += last


    return tot_last, tot_first

def q_bonus_solution(file):
    #Just reverse the input for q2
    lines = [ints(l) for l in open(file, 'r')]
    tots = [0,0]

    for l in lines:
        for tot, curr_diff in ([0, l], [1, l[::-1]]):
            last = curr_diff[-1]

            while not max(curr_diff) == min(curr_diff):
                curr_diff = [curr_diff[i+1] - curr_diff[i] for i in range(len(curr_diff) - 1)]
                last += curr_diff[-1]
            
            tots[tot] += last

    return tots

if __name__ == "__main__":
    print('Answer with calculating the first and last value directly (Q1, Q2):')
    file = 'test.txt'
    ans(q(file), 'test ', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)
    print('\nAnswer with just reversing the input (Q1, Q2):')
    file = 'test.txt'
    ans(q_bonus_solution(file), 'test ', copy=False)
    file = 'input.txt'
    ans(q_bonus_solution(file), 'input', copy=True)