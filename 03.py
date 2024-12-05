#!/bin/python3
import sys
import re

input = sys.argv[1]

pos = 0

pattern = "mul\(\d{1,3},\d{1,3}\)"
match = re.findall(pattern, input)

sum = 0
for m in match:
    nums = m[4:].split(",")
    first = int(nums[0])
    second = int(nums[1][:-1])
    sum += (first * second)

print(sum)


pattern = "mul\(\d{1,3},\d{1,3}\)"
dos = "do\(\)"
donts = "don't\(\)"
match = re.findall(pattern + "|" + dos + "|" + donts, input)

sum = 0
isDont = False
for m in match:

    if m[:3] == "mul" and isDont:
        continue

    if m[:3] == "don":
        isDont = True
        continue

    if m[:3] == "do(":
        isDont = False
        continue

    nums = m[4:].split(",")
    first = int(nums[0])
    second = int(nums[1][:-1])
    sum += (first * second)

print(sum)

