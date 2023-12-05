import typing
import re
import subprocess 
from functools import reduce

def lmap(func, *iterables):
    return list(map(func, *iterables))

def ints(s: str) -> typing.List[int]:
    assert isinstance(s, str), f"you passed in a {type(s)}!!!"
    return lmap(int, re.findall(r"(?:(?<!\d)-)?\d+", s))  # thanks mserrano!

def digits(s: str) -> typing.List[int]:
    return [int(c) for c in s if c.isdigit()]

def strs(s: str) -> typing.List[str]:
    return s.strip().split(' ')

def inter(a, b):
    #a and b can be lists or sets
    return a.intersection(b)

def ans(i: int, s: str, copy: bool):
    print(f'Answer to {s}: {i}')
    if copy:
        subprocess.run(f"echo {i} | clip", shell=True)

def chunks(lst, n):
    """returns successive n-sized chunks from lst."""
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i:i + n])
    return result

dirs = {
    'R': [0,1],
    'U': [1,0],
    'L': [0,-1],
    'D': [-1,0]
}

def product(lst):
    return reduce(lambda x,y: x*y, lst)

def flatten(l):
    return list(flatten_yield(l))

def flatten_yield(l):
    for item in l:
        try:
            yield from flatten(item)
        except TypeError:
            yield item