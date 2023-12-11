import sys
sys.path.insert(0, '../..')
from utils import *

from functools import reduce
from collections import defaultdict, Counter
import itertools
import re

D = defaultdict(str)

def f(start, max_time, open, curr_flow, tot_flow, highest_flow):
    time_left = max_time
    possible = [[start, time_left, open, curr_flow, tot_flow]]
    max_flow = 0

    iter = 0
    while len(possible) > 0:
        iter += 1
        if iter % 10000000 == 0:
            print(iter, len(possible), max_flow, possible[-1])
            # print(possible)
        start, time_left, open, curr_flow, tot_flow = possible[-1]
        possible = possible[:-1]

        combined_max_flow = tot_flow
        curr_temp_flow = curr_flow
        for i in range(time_left):
            combined_max_flow += curr_temp_flow 
            curr_temp_flow += highest_flow if i % 2 == 0 else 0
        if combined_max_flow <= max_flow:
            # print(time_left, curr_flow, tot_flow, combined_max_flow, max_flow)
            continue

        if time_left == 0:
            max_flow = max(max_flow, tot_flow)
            continue
        else:

            #move to
            if start in D:
                for t in D[start][1]:
                    possible.append([t, time_left-1, open, curr_flow, tot_flow+curr_flow])
            else:
                #Wait (strictly worse than move to)
                possible.append([start, time_left-1, open, curr_flow, tot_flow+curr_flow])

            #Open
            if not start in open and D[start][0] > 0:
                possible.append([start, time_left-1, open + [start], curr_flow + D[start][0], tot_flow+curr_flow])

    
    return max_flow


def f2(start, max_time, open, curr_flow, tot_flow, highest_flow):
    time_left = max_time
    possible = [[[None, None], start, time_left, open, curr_flow, tot_flow, True, curr_flow]]
    max_flow = 1650

    valve_flow = sorted([[v[0], k] for k,v in D.items() if v[0] > 0])[::-1]
    all_valve = set([x[1] for x in valve_flow])
    print(valve_flow)

    iter = 0
    while len(possible) > 0:
        iter += 1
        if iter % 2000000 == 0:
            print(iter, len(possible), max_flow, possible[-1])
            # print(possible)
        prev, start, time_left, open, curr_flow, tot_flow, is_player, next_flow = possible[-1]
        start_l, start_r = start
        prev_l, prev_r = prev
        possible = possible[:-1]

        #####CALCULATE COMBINED_MAX_FLOW
        combined_max_flow = tot_flow
        curr_temp_flow = curr_flow
        curr_temp_open = open.copy()
        # print('!!!', curr_temp_flow, curr_temp_open, combined_max_flow)
        if is_player:
            for i in range(time_left):
                combined_max_flow += curr_temp_flow

                if i % 2 == 0:
                    added = 0
                    for a in valve_flow:
                        found = False
                        for b in curr_temp_open:
                            if b == a[1]:
                                found=True
                                break
                        
                        if not found:
                            #add
                            curr_temp_open.append(a[1])
                            curr_temp_flow += a[0]
                            added += 1
                        if added >= 2:
                            break
                # print(curr_temp_flow, combined_max_flow)
                if combined_max_flow > max_flow:
                    continue
        if is_player and combined_max_flow <= max_flow:
            # print(time_left, curr_flow, tot_flow, combined_max_flow, max_flow)
            continue
        #####CALCULATE COMBINED_MAX_FLOW

        if time_left == 0:
            max_flow = max(max_flow, tot_flow)
            continue
        else:
            if is_player:
                #move to
                for t in D[start_l][1]:
                    if not t == prev_l:
                        possible.append([[start_l, prev_r], [t, start_r], time_left, open, curr_flow, tot_flow, False, curr_flow])

                #Open
                if not start_l in open and D[start_l][0] > 0:
                    possible.append([[start_l, start_r], [start_l, start_r], time_left, open + [start_l], curr_flow, tot_flow, False, curr_flow + D[start_l][0]])
            
            else: #elephant
                #move to
                for t in D[start_r][1]:
                    if not t == prev_r:
                        possible.append([[prev_l, start_r], [start_l, t], time_left - 1, open, next_flow, tot_flow+curr_flow, True, next_flow])

                #Open
                if not start_r in open and D[start_r][0] > 0:
                    possible.append([[start_l, start_r], [start_l, start_r], time_left - 1, open + [start_r], next_flow + D[start_r][0], tot_flow+curr_flow, True, next_flow + D[start_r][0]])
    
    print('total iter:', iter)
    return max_flow


def q(file):
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
    start = 'AA'

    highest_flow = sorted([p[0] for p in D.values()])[-1]
    # return f1(start, 30, [], 0, 0, highest_flow)
    return f2([start, start], 26, [], 0, 0, highest_flow)

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)