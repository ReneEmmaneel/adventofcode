#Just call the library lol

import sys
sys.path.insert(0, '../..')
from utils import *
import networkx as nx

from functools import reduce
from collections import defaultdict, Counter
import itertools
import math
import heapq #heappush heappop
import re
import random
from collections import defaultdict

def q(file):
    G = nx.Graph()

    for l in [l for l in open(file, 'r')]:
        r = re.findall(r"\w+", l)
        for i in r[1:]:
            G.add_edge(r[0], i)

    G.remove_edges_from(nx.minimum_edge_cut(G))
    g = [len(c) for c in nx.connected_components(G)]
    return g[0] * g[1]

if __name__ == "__main__":
    file = 'test.txt'
    ans(q(file), 'test', copy=False)
    file = 'input.txt'
    ans(q(file), 'input', copy=True)