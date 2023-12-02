import sys
sys.path.insert(0, '../..')
from utils import *

import itertools
import re


def q(file):
    size = 2000
    field = [[0 for _ in range(size)] for _ in range(size)]
    H = [size//2,size//2]
    K = [[size//2,size//2] for _ in range(9)]

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

            field[K[-1][0]][K[-1][1]] = 1
        
    tot = sum([sum(x) for x in field])

    # for x in range(len(field)):
    #     for y in range(len(field)):
    #         print(field[x][y], end='')
    #     print('')
        
    return tot

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)