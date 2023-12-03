import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict
import itertools
import re

def draw_signal(i, X):
    X = X + 1
    i = i % 40
    if abs(i - X) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if i==0:
        print('')

def q(file):
    signal = []
    X = 1

    for l in open(file, 'r').readlines():
        l = l.strip()
        if l.startswith('noop'):
            signal.append(X * (len(signal) + 1))
            draw_signal(len(signal), X)
        elif l.startswith('addx'):
            _, dX = l.split(' ')
            dX = int(dX)
            signal.append(X * (len(signal) + 1))
            draw_signal(len(signal), X)
            signal.append(X * (len(signal) + 1))
            draw_signal(len(signal), X)
            X += dX

    return sum(list(signal[19::40])[:6])

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)