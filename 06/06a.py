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

ops = defaultdict(lambda: [])

result = 0

for line in lines:
    parts = re.split(r" +", line)
    for i, part in enumerate(filter(lambda part: part, parts)):
        if part == "*":
            amount = 1
            for x in ops[i]:
                amount *= x
            result += amount
        elif part == "+":
            for x in ops[i]:
                result += x
        else:
            ops[i].append(int(part))

print(result)
