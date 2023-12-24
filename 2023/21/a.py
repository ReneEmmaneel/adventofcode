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
    G = [[[c, [], []] for c in l.strip()] for l in open(file, 'r')]
    orig_steps = steps = 26501365
    curr = []
    for y in range(len(G)):
        for x in range(len(G[0])):
            if G[y][x][0] == 'S':
                G[y][x][1].append((y,x))
                G[y][x][2].append(0)
                curr.append([y,x])

    prev = 0
    prevprev = 0
    while steps > 0 and len(curr) > 0:
        new_curr = []
        for c in curr:
            co = c
            c = [c[0] % len(G[0]), c[1] % len(G)]

            for d in [[0,1], [0,-1], [-1,0], [1,0]]:
                old = [co[0]+d[0], co[1]+d[1]]
                new = [old[0] % len(G[0]), old[1] % len(G)]

                if G[new[0]][new[1]][0] == '#':
                    continue
                if G[new[0]][new[1]][0] in ['.', 'S']:
                    if not (old[0], old[1]) in G[new[0]][new[1]][1]:
                        G[new[0]][new[1]][1].append((old[0], old[1]))
                        G[new[0]][new[1]][2].append(orig_steps - steps + 1)

                        new_curr.append(old)
        curr = new_curr
        steps -= 1

        tot = 0
        for y in range(len(G)):
            for x in range(len(G[0])):
                for d in G[y][x][2]:
                    if d % 2 == (orig_steps - steps) % 2:
                        tot += 1
        if orig_steps - steps == 64:
            print('Q1: ', tot, '\n')
            print('For Q2, we first find some numbers')
            print('n, tot, delta_tot, delta_delta_tot')
        if steps % len(G) == 0:
            print(orig_steps - steps, tot, tot-prev, (tot-prev)-prevprev)
            prevprev = tot-prev
            prev=tot
            if orig_steps - steps > 500:
                break

q('input.txt')


print('Picking some of these values manually, and iterating it to the end:')

#Calculating it by iteration
step, delta_step, tot, delta_tot, delta_delta_tot = 589, 131, 302402, 119395, 29826

while (step < 26501365):
    step += delta_step
    delta_tot += delta_delta_tot
    tot += delta_tot

print('iterations:', tot)

#Or with quadratic equation
#https://www.mathcelebrity.com/3ptquad.php?p1=327%2C+93438&p2=458%2C+183007&p3=589%2C+302402&pl=Calculate+Equation
def f(x):
    return (-3907206/-4496182) * x**2 + (-7030508/-4496182) * x + (-21647226/-4496182)

print('quadratics:', f(26501365))