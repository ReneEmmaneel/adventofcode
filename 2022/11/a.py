import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict
import itertools
import re

def q(file, q1):
    tot = 0 

    monkeys = []

    cmonkey = False
    for l in open(file, 'r').readlines():
        l = l.strip()
        if l.startswith('Monkey'):
            if cmonkey:
                monkeys.append(cmonkey)
            cmonkey = {'id': ints(l)[0], 'items': [], 'op': [], 'test': {'div': -1, 'true': -1, 'false': -1}, 'ins': 0}
        if l.startswith('Starting items'):
            cmonkey['items'] = ints(l)
        if l.startswith('Operation'):
            d = ints(l)
            if len(d) == 0:
                d = 'old'
            else:
                d = d[0]
            if '*' in l:
                cmonkey['op'] = ['*', d]
            if '+' in l:
                cmonkey['op'] = ['+', d]
        if l.startswith('Test'):
            d = ints(l)[0]
            cmonkey['test']['div'] = d
        if l.startswith('If true'):
            d = ints(l)[0]
            cmonkey['test']['true'] = d
        if l.startswith('If false'):
            d = ints(l)[0]
            cmonkey['test']['false'] = d
    monkeys.append(cmonkey)

    all_mul = reduce(lambda x,y: x*y, [x['test']['div'] for x in monkeys])
    
    #Actual logic
    for i in range(20 if q1 else 10000):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey['ins'] += 1
                if monkey['op'][0] == '*':
                    if monkey['op'][1] == 'old':
                        worry = item * item
                    else:
                        worry = item * monkey['op'][1]
                if monkey['op'][0] == '+':
                    worry = item + monkey['op'][1]
                if q1:
                    worry = worry // 3

                #check div
                div = monkey['test']['div']
                if worry % div == 0:
                    next = monkey['test']['true']
                else:
                    next = monkey['test']['false']
                worry = worry % all_mul
                monkeys[next]['items'].append(worry)
            monkey['items'] = []

    bus = [x['ins'] for x in monkeys]
    bus.sort()

    return bus[-1] * bus[-2]

if __name__ == "__main__":
    print('Question 1:')
    file = 'test.txt'
    ans(q(file, True), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, True), 'input', copy=True)
    print('Question 2:')
    file = 'test.txt'
    ans(q(file, False), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, False), 'input', copy=True)