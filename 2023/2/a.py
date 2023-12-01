import sys
sys.path.insert(0, '../..')
from utils import lmap, ints, strs

import itertools
import re

def q1(file):
    tot = 0 
    for l in open(file, 'r').readlines():
        values = ints(l)
        


    return(tot)

def q2(file):
    tot = 0 
    for l in open(file, 'r').readlines():
        values = ints(l)



    return(tot)

if __name__ == "__main__":
    # file = 'input.txt'
    file = 'test.txt'


    print(f'Answer to question 1: {q1()}')
    print(f'Answer to question 2: {q2()}')
