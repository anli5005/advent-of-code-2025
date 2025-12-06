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

offsets = []
lengths = []
ops = []
for i, c in enumerate(lines[-1]):
    if c != " ":
        offsets.append(i)

for i in range(len(offsets) - 1):
    lengths.append(offsets[i + 1] - offsets[i] - 1)

lengths.append(len(lines[-1]) - offsets[-1])
for l in lengths:
    ops.append(["" for _ in range(l)])

result = 0

for line in lines:
    for i, o in enumerate(offsets):
        if line[o] == "*":
            amount = 1
            for x in ops[i]:
                amount *= int(x)
            result += amount
        elif line[o] == "+":
            for x in ops[i]:
                result += int(x)
        else:
            for j in range(lengths[i]):
                if line[o + j] != " ":
                    ops[i][j] += line[o + j]

print(result)
