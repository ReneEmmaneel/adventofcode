#Don't look at this solution... ugh

import sys
sys.path.insert(0, '../..')
from utils import *

import itertools
import re

def add(prev_nums):
    tot = 0
    p_i = -1
    c_s = []
    found_s = False
    for p in prev_nums:
        if len(c_s) > 0:
            if p[0] == p_i + 1:
                c_s.append(p[1])
                if p[2]:
                    found_s = True
            else:
                a = int(''.join(c_s))
                if found_s:
                    tot += a
                    found_s = False

                c_s = []
                c_s.append(p[1])
                if p[2]:
                    found_s = True
            p_i = p[0]
        else:
            p_i = p[0]
            c_s.append(p[1])
            if p[2]:
                found_s = True
    #add
    if len(c_s) > 0:
        a = int(''.join(c_s))
        if found_s:
            tot += a
            found_s = False
    c_s = []
    return tot

def q1(file):
    tot = 0 
    prev_nums = []
    prev_symbols = []
    for l in open(file, 'r').readlines():
        l = l.strip()
        curr_nums = [(a, x, False) for a,x in enumerate(l) if x.isdigit()]
        symbols = [(a, x) for a, x in enumerate(l) if not x.isdigit() and not x == '.']

        temp = []
        for b in prev_nums:
            find = False
            for a, x in symbols:
                if abs(b[0] - a) <= 1:
                    find = True
                    temp.append((b[0], b[1], True))
            if not find:
                temp.append(b)
        prev_nums = temp

        temp = []
        for b in curr_nums:
            find = False
            for a, x in symbols:
                if abs(b[0] - a) <= 1:
                    find = True
                    temp.append((b[0], b[1], True))
            if not find:
                temp.append(b)
        curr_nums = temp

        temp = []
        for b in curr_nums:
            find = False
            for a, x in prev_symbols:
                if abs(b[0] - a) <= 1:
                    find = True
                    temp.append((b[0], b[1], True))
            if not find:
                temp.append(b)
        curr_nums = temp
        
        tot += add(prev_nums)

        prev_symbols = symbols
        prev_nums = curr_nums

    tot += add(curr_nums)

        
    return tot

def q2(file):
    tot = 0 
    lines = []
    for l in open(file, 'r').readlines():
        lines.append(l.strip())

    for i, l in enumerate(lines):
        if i == 0 or i == len(lines) -1:
            continue
        gears = [(a, x) for a, x in enumerate(l) if x == '*']
        
            # temp = []
            # for b in prev_nums:
            #     find = False
            #     for a, x in gears:
            #         if abs(b[0] - a) <= 1:
            #             find = True
            #             temp.append((b[0], b[1], True))
            #     if not find:
            #         temp.append(b)
            # prev_nums = temp
        
        for a, g in gears:
            prev_nums = [(a, x) for a,x in enumerate(lines[i-1]) if x.isdigit()]
            curr_nums = [(a, x) for a,x in enumerate(lines[i]) if x.isdigit()]
            next_nums = [(a, x) for a,x in enumerate(lines[i+1]) if x.isdigit()]

            nums = []
            find = 0
            for k in [prev_nums, curr_nums, next_nums]:
                num = []
                curr_ind = -1

                ffound = False
                for ind_num, value in k:



                    if len(num) == 0:
                        num.append(value)
                        curr_ind = ind_num
                    elif ind_num == curr_ind + 1:
                        num.append(value)
                        curr_ind = ind_num
                    else:
                        if ffound:
                            nums.append(num)
                        ffound = False
                        num = []
                        num.append(value)
                        curr_ind = ind_num
                    
                    if abs(ind_num - a) <= 1:
                        ffound = True
                if ffound:
                    nums.append(num)
            
            numsc = [int(''.join(n)) for n in nums]
            if len(numsc) == 2:
                tot += numsc[0] * numsc[1]
    return tot


if __name__ == "__main__":
    import time
    start_time = time.time()


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

    
    print(f"--- {time.time() - start_time} seconds ---")