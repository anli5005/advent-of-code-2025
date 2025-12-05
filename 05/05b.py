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
result = 0

for line in lines:
    if line == "":
        break
    
    a, b = line.split("-")
    ranges.append((int(a), int(b)))

ranges.sort()

while True:
    did_change = False
    l = len(ranges)
    for i in range(l - 1):
        a = ranges[i]
        b = ranges[i + 1]
        if a[1] >= b[0]:
            ranges[i] = (a[0], max(a[1], b[1]))
            ranges.pop(i + 1)
            did_change = True
            break
    if not did_change:
        break

for r in ranges:
    result += r[1] - r[0] + 1

print(result)
