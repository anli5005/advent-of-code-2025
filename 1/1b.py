import sys
import re
from collections import *
from itertools import *
from heapq import *
from dataclasses import *
import functools
import math

def count(it):
    return sum(1 for _ in it)

inp = sys.stdin.read()
lines = inp.split("\n")
m = len(lines)
n = len(lines[0])

grid = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
diag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
# dirs = dirs + diag

result = 0
pos = 50

for line in lines:
    amount = int(line[1:])
    for i in range(amount):
        if line[0] == "L":
            pos -= 1
        else:
            pos += 1
        pos = (pos + 100) % 100
        if pos == 0:
            result += 1

print(result)
