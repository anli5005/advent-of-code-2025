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
    dp = [["" for i in range(12)] for j in range(len(line))]
    joltage = 0
    for i in range(len(line)):
        dp[i][0] = line[i]
        for j in range(1, 12):
            acc = ""
            for k in range(0, i):
                curr = dp[k][j - 1]
                if curr != "" and (acc == "" or int(curr) > int(acc)):
                    acc = curr
            dp[i][j] = acc + line[i]
        joltage = max(joltage, int(dp[i][11]))
    result += joltage

print(result)
