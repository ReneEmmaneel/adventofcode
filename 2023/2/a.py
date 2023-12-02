import sys
sys.path.insert(0, '../..')
from utils import lmap, ints, strs

import itertools
import re

def q1(file):
    tot = 0 
    id = 0
    for l in open(file, 'r').readlines():
        fail = False
        id += 1
        sets = l.split(': ')[1].split(';')
        for set in sets:
            items = [x.strip() for x in set.split(', ')]
            for item in items:
                n, c = item.split(' ')
                n = int(n)

                if c == 'red':
                    if n > 12:
                        fail = True
                if c == 'blue':
                    if n > 14:
                        fail = True
                if c == 'green':
                    if n > 13:
                        fail = True
        if not fail:
            tot += id
    return tot

def q2(file):
    tot = 0 
    id = 0
    for l in open(file, 'r').readlines():
        id += 1
        sets = l.split(': ')[1].split(';')
        minr = 0
        minb = 0
        ming = 0
        for set in sets:
            items = [x.strip() for x in set.split(', ')]
            for item in items:
                n, c = item.split(' ')
                n = int(n)

                if c == 'red':
                    if n > minr:
                        minr = n
                if c == 'blue':
                    if n > minb:
                        minb = n
                if c == 'green':
                    if n > ming:
                        ming = n
        tot += minr * minb * ming

    return(tot)

if __name__ == "__main__":
    for q, fun in enumerate([q1, q2]):
        print(f'Question {q}')
        file = 'test.txt'
        print(f'Answer to test: {fun(file)}')
        file = 'input.txt'
        print(f'Answer to input: {fun(file)}')
