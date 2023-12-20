import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import math
import re

#Pulses are always processed in the order they are sent. So, if a pulse is sent to modules a, b, and c, and then module a processes its pulse and sends more pulses, the pulses sent to modules b and c would have to be handled first.
#Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules; they initially default to remembering a low pulse for each input. When a pulse is received, the conjunction module first updates its memory for that input. Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
#Flip-flop modules (prefix %) are either on or off; they are initially off. If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it flips between on and off. If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

L = {}
M = {}
S = []
send = [0,0]
def push(stack, i):
    S = [stack]

    while len(S) > 0:
        fro, name, pulse = S[0]

        # print(f'{fro} -{pulse} -> {name}')
        S = S[1:]
        if not name in M:
            continue
        t, info, items = M[name]

        if t == 1: #flip-flop %
            if pulse == 0:
                M[name][1] = -1 * (M[name][1] - 1)
                info = M[name][1]
            else:
                continue
        if t == 2: #Conjunction &
            M[name][1][fro] = pulse
            new_pulse = 0
            for v in M[name][1].values():
                if v == 0:
                    new_pulse = 1
                    break
        for item in items:
            
            if t == 0:
                send[0] += 1
                S.append([name, item, 0])
            elif t == 1: #flip-flop %
                send[info] += 1
                S.append([name, item, info])
            elif t == 2: #Conjunction high for all -> flow pulse
                send[new_pulse] += 1
                S.append([name, item, new_pulse])
                
                if item == 'kh' and new_pulse == 1 and not name in L:
                    L[name] = i

def q(file):
    lines = [l for l in open(file, 'r')]
    tot = 0 

    for l in lines:
        l = l.strip()
        n, items = l.split(' -> ')
        items = items.split(', ')

        if n == 'broadcaster':
            M['broadcaster'] = [0, 0, items]
        elif n[0] == '%':
            M[n[1:]] = [1, 0, items]
        elif n[0] == '&':
            M[n[1:]] = [2, {}, items]
    
    connected = []
    for k, v in M.items():
        for item in v[2]:
            if item in M:
                if M[item][0] == 2:
                    M[item][1][k] = 0
                if item == 'kh':
                    connected.append(k)

    q1, q2 = 0, 0
    for i in range(1, 100000):
        send[0] += 1
        push(['button', 'broadcaster', 0], i)
        
        if i == 1000:
            q1 = send[0] * send[1]

        if len(L) == 4:
            q2 = math.lcm(*L.values())
            break

    return q1, q2

if __name__ == "__main__":
    L, M, S, send = {}, {}, [], [0,0]
    ans(q('test.txt'), 'test', copy=False)

    L, M, S, send = {}, {}, [], [0,0]
    ans(q('test2.txt'), 'test', copy=False)

    L, M, S, send = {}, {}, [], [0,0]
    ans(q('input.txt'), 'input', copy=True)