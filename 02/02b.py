import sys
import re
from collections import *
from itertools import *
from heapq import *
from dataclasses import *
import functools
import math

inp = sys.stdin.read()
parts = inp.split(",")
result = 0

for part in parts:
    a, b = part.split("-")
    for i in range(int(a), int(b) + 1):
        s = str(i)
        l = len(s)
        for j in range(1, l // 2 + 1):
            if l % j != 0:
                continue
            if s == s[:j] * (l // j):
                result += i
                break

print(result)
