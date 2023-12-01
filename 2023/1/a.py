from utils import lmap, ints, strs
import itertools
import re

nums = ['zero', 'one', 'two', 'three', 'four','five','six','seven','eight','nine']
q = 2

tot = 0 
for l in open('in.txt', 'r').readlines():
    ind = [(a, int(x)) for a, x in enumerate(l) if x.isdigit()]

    if q == 2:
        for c in range(10):
            try:
                a = [m.start() for m in re.finditer(nums[c], l)]
                if len(a) > 0:
                    ind.append((int(a[0]), c))
                    ind.append((int(a[-1]), c))
            except:
                pass
    
    ind.sort()

    tot += ind[0][1] * 10 + ind[-1][1]
print(tot)