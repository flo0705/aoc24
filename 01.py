#!/bin/python3
import sys

input = sys.argv[1]
input = input.replace("   ", "\n").split("\n")

left = []
right = []
for x in range(int(len(input) / 2)):
    left.append(int(input[2 * x]))
    right.append(int(input[2 * x + 1]))

left = sorted(left)
right = sorted(right)

sum = 0
for x in range(len(left)):
    sum += abs(left[x] - right[x])

print(sum)

sim = 0
for x in left:
    num = 0;
    for y in right:
        if y == x:
            num += 1

    sim += x * num
    
print(sim)

