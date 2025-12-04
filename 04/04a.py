import sys
import re
from collections import *
from itertools import *
from heapq import *
from dataclasses import *
import functools
import math

inp = sys.stdin.read()
lines = inp.split("\n")
m = len(lines)
n = len(lines[0])

grid = defaultdict((lambda: defaultdict(lambda: "!")), enumerate(defaultdict((lambda: "!"), enumerate(line)) for line in lines))
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
diag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
dirs = dirs + diag

result = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] != "@":
            continue
        rolls = 0
        for di, dj in dirs:
            if grid[i + di][j + dj] == "@":
                rolls += 1
        if rolls < 4:
            result += 1

print(result)
