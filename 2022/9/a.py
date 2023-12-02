import sys
sys.path.insert(0, '../..')
from utils import *

import itertools
import re


def q(file, knots):
    size = 2000
    field = [[0 for _ in range(size)] for _ in range(size)]
    H = [size//2,size//2]
    K = [[size//2,size//2] for _ in range(knots)]

    tot = 0 
    for l in open(file, 'r').readlines():
        l = l.strip()
        d, n = l.split(' ')
        dir = dirs[d]

        field[K[-1][0]][K[-1][1]] = 1

        for i in range(int(n)):
            H[0] += dir[0]
            H[1] += dir[1]

            A = H
            
            # Very readable code, I know...
            # The idea is that when the knot before is 2 away, it should move 1 in that direction,
            # plus possibly max 1 more if diagonally
            # The difference in movement between q1 and q2 is that the knot before it can now possibly be 2 away in both directions,
            # instead of max a horse jump difference away. This makes some difference in the movement logic.
            for B in K:
                if A[0] - B[0] == 2:
                    B[0] += 1
                    if abs(B[1] - A[1]) <= 1:
                        B[1] = A[1]
                    else:
                        B[1] += 1 * (int(A[1] > B[1])*2-1)
                elif A[0] - B[0] == -2:
                    B[0] -= 1
                    if abs(B[1] - A[1]) <= 1:
                        B[1] = A[1]
                    else:
                        B[1] += 1 * (int(A[1] > B[1])*2-1)
                elif A[1] - B[1] == 2:
                    B[1] += 1
                    if abs(B[0] - A[0]) <= 1:
                        B[0] = A[0]
                    else:
                        B[0] += 1 * (int(A[0] > B[0])*2-1)
                elif A[1] - B[1] == -2:
                    B[1] -= 1
                    if abs(B[0] - A[0]) <= 1:
                        B[0] = A[0]
                    else:
                        B[0] += 1 * (int(A[0] > B[0])*2-1)
                A = B

            # Just keep track where the tail has been
            field[K[-1][0]][K[-1][1]] = 1
        
    tot = sum([sum(x) for x in field])
        
    return tot

if __name__ == "__main__":
    print('Question 1:')
    file = 'test.txt'
    ans(q(file, 1), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, 1), 'input', copy=True)
    
    print('Question 2:')
    file = 'test.txt'
    ans(q(file, 9), 'test', copy=False)
    file = 'input.txt'
    ans(q(file, 9), 'input', copy=True)