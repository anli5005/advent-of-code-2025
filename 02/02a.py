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
        if l % 2 == 0:
            if s[:(l // 2)] == s[(l // 2):]:
                result += i

print(result)
