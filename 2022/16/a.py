import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re

D = defaultdict(str)
DP = {}

def f1(start, time_left, open, curr_flow):
    open.sort()
    key = (start, time_left, tuple(open))
    if key in DP:
        return DP[key]

    if time_left == 1:
        return curr_flow
    else:
        possible = []

        #move to
        if start in D:
            for t in D[start][1]:
                possible.append(f1(t, time_left-1, open, curr_flow))

        #Open
        if not start in open and D[start][0] > 0:
            possible.append(f1(start, time_left-1, open + [start], curr_flow + D[start][0]))

        final_flow = curr_flow + max(possible)
        DP[key] = final_flow
        return final_flow

    
    return max_flow

best_flow_found = 0
def f2(start_l, start_r, time_left, open, curr_flow, is_player):
    open.sort()
    key = (start_l, start_r, time_left, tuple(open), is_player)

    if key in DP:
        return DP[key]
    if time_left == 1:
        return curr_flow
    else:
        pos = start_l if is_player else start_r
        possible = [0]
        
        #Open
        if not pos in open and D[pos][0] > 0:
            possible.append(f2(start_l, start_r, time_left - (0 if is_player else 1), open + [pos], curr_flow + D[pos][0], not is_player))

        for t in D[pos][1]:
            possible.append(f2(t if is_player else start_l, start_r if is_player else t, time_left - (0 if is_player else 1), open, curr_flow, not is_player))

        final_flow = max(possible) + (curr_flow if is_player else 0)
        DP[key] = final_flow
        
        global best_flow_found
        if final_flow > best_flow_found:
            print(final_flow, len(DP), ' | time_left: ', time_left, ' ', is_player)
            best_flow_found = final_flow
        return final_flow
    
def f2(start_l, start_r, time_left, open, curr_flow, is_player):
    open.sort()
    key = (start_l, start_r, time_left, tuple(open), is_player)

    if key in DP:
        return DP[key]
    if time_left == 1:
        return curr_flow
    else:
        pos = start_l if is_player else start_r
        possible = [0]
        
        #Open
        if not pos in open and D[pos][0] > 0:
            possible.append(f2(start_l, start_r, time_left - (0 if is_player else 1), open + [pos], curr_flow + D[pos][0], not is_player))

        for t in D[pos][1]:
            possible.append(f2(t if is_player else start_l, start_r if is_player else t, time_left - (0 if is_player else 1), open, curr_flow, not is_player))

        final_flow = max(possible) + (curr_flow if is_player else 0)
        DP[key] = final_flow
        
        global best_flow_found
        if final_flow > best_flow_found:
            print(final_flow, len(DP), ' | time_left: ', time_left, ' ', is_player)
            best_flow_found = final_flow
        return final_flow
    
def f2_w_prev(prev_l, prev_r, start_l, start_r, time_left, open, curr_flow, is_player):
    open.sort()
    key = (prev_l, prev_r, start_l, start_r, time_left, tuple(open), is_player)

    if key in DP:
        return DP[key]
    if time_left == 1:
        return curr_flow
    else:
        pos = start_l if is_player else start_r
        possible = [0]

        #Open
        if not pos in open and D[pos][0] > 0:
            possible.append(f2_w_prev(start_l if is_player else prev_l, prev_r if is_player else start_r, 
                                      start_l, start_r, time_left - (0 if is_player else 1), 
                                      open + [pos], curr_flow + D[pos][0], not is_player))

        for t in D[pos][1]:
            if (t == prev_l and is_player) or (t == prev_r and is_player):
                continue
            else:
                possible.append(f2_w_prev(start_l if is_player else prev_l, prev_r if is_player else start_r, 
                                          t if is_player else start_l, start_r if is_player else t, 
                                          time_left - (0 if is_player else 1), open, curr_flow, not is_player))

        final_flow = max(possible) + (curr_flow if is_player else 0)
        DP[key] = final_flow
        
        global best_flow_found
        if final_flow > best_flow_found:
            print(final_flow, len(DP), ' | time_left: ', time_left, ' ', is_player)
            best_flow_found = final_flow
        return final_flow


def q(file, q2):
    lines = [l for l in open(file, 'r')]
    tot = 0 

    for l in lines:
        l = l.strip().replace('; tunnel leads to valve ', '; tunnels lead to valves ')
        left, right = l.split('; tunnels lead to valves ')
        tunnel, flow_rate = left.split(' has flow rate=')
        
        tunnel = tunnel.split('Valve ')[-1]
        flow_rate = int(flow_rate)
        connect_to = right.split(', ')
        D[tunnel] = [flow_rate, connect_to]

    #Create dict of dict from AA+good valves to other all other good valves
    print(D.items())
    good_valves = [[k, v[0], v[1]] for k, v in D.items() if v[0] > 0 or k == 'AA']


    return
    start = 'AA'

    highest_flow = sorted([p[0] for p in D.values()])[-1]

    if not q2:
        return f1(start, 30, [], 0)
    else:
        return f2(start, start, 26, [], 0, True)
        # return f2_w_prev(None, None, start, start, 26, [], 0, True)

if __name__ == "__main__":

    import time
    start_time = time.time()
    # print('Question 1:')
    # file = 'test.txt'
    # ans(q(file, False), 'test', copy=False)
    # DP = {}
    # file = 'input.txt'
    # ans(q(file, False), 'input', copy=True)
    # DP = {}

    print(f"--- {time.time() - start_time} seconds")
    start_time = time.time()

    D = defaultdict(str)

    best_flow_found = 0

    print('Question 2:')
    file = 'test.txt'
    ans(q(file, True), 'test', copy=False)
    DP = {} 
    best_flow_found = 0
    file = 'input.txt'
    ans(q(file, True), 'input', copy=True)
    
    print(f"--- {time.time() - start_time} seconds")