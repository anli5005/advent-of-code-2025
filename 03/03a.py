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

result = 0

for line in lines:
    joltage = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            curr = int(line[i] + line[j])
            if curr > joltage:
                joltage = curr
    print(joltage)
    result += joltage

print(result)
