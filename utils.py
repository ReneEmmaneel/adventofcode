import typing
import re

def lmap(func, *iterables):
    return list(map(func, *iterables))

def ints(s: str) -> typing.List[int]:
    assert isinstance(s, str), f"you passed in a {type(s)}!!!"
    return lmap(int, re.findall(r"(?:(?<!\d)-)?\d+", s))  # thanks mserrano!

def strs(s: str) -> typing.List[str]:
    return s.strip().split(' ')