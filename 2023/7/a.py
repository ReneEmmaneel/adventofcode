import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re


def q(file, q2):
    lines = [l.strip().split(' ') for l in open(file, 'r')]
    tot = 0 

    card_strength = 'J23456789TQKA' if q2 else '23456789TJQKA'

    hands = []
    for cards, bid in lines:
        jokers = cards.count('J') if q2 else 0
        cards_num = [card_strength.find(c) for c in cards]

        C = Counter()
        for c in cards_num:
            if c > 0 or not q2:
                C[c] += 1
        
        if jokers == 5:
            h = [5]
        else:
            h = sorted(C.values(), reverse=True)
            h[0] += jokers 

        hand_strength = [[1,1,1,1,1],[2,1,1,1],[2,2,1],[3,1,1],[3,2],[4,1],[5]].index(h)
        
        hands.append([hand_strength, cards_num, bid])
    
    hands = sorted(hands, key=lambda x: (x[0], x[1]))

    tot = sum([(i + 1) * int(h[2]) for i, h in enumerate(hands)])
        
    return tot

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file, False), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, False), 'input', copy=True)
    file = 'test.txt'
    ans(q(file, True), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, True), 'input', copy=True)