import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import math
import heapq #heappush heappop
import re


def q(file):
    lines = [l for l in open(file, 'r')]
    tot = 0 
    for l in lines:
        l = l.strip()
        
    return tot

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)