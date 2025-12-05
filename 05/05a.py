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
ranges = []
ranges_done = False
result = 0

for line in lines:
    if line == "":
        ranges_done = True
        continue
    if ranges_done:
        id = int(line)
        if any(id >= r[0] and id <= r[1] for r in ranges):
            result += 1
    else:
        a, b = line.split("-")
        ranges.append((int(a), int(b)))

print(result)
