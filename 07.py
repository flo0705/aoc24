#!/bin/python3
import sys
import itertools

lines = sys.argv[1].split('\n')

def get_operations_list(num, ops):
    return [p for p in itertools.product(ops, repeat=num)]

def is_right(check, nums, include_concat):
    ops = ["+", "*"]
    
    if include_concat:
        ops += ["||"]

    perms = get_operations_list(len(nums) - 1, ops)

    for perm in perms:
        value = nums[0] 
        for i, op in enumerate(perm):
            if (op == "+"):
                value += nums[i+1]
            if (op == "*"):
                value *= nums[i+1]
            if (op == "||"):
                value = int(str(value) + str(nums[i+1]))

        if value == check:
            return True

    return False

sum = 0
for line in lines:
    left = int(line.split(":")[0])
    rights = [int(num) for num in line.split(":")[1][1:].split(" ")]

    if is_right(left, rights, False):
        sum += left

print(sum)

sum = 0
for line in lines:
    left = int(line.split(":")[0])
    rights = [int(num) for num in line.split(":")[1][1:].split(" ")]

    if is_right(left, rights, True):
        sum += left

print(sum)


