#!/bin/python3
import sys
import itertools

input = sys.argv[1].split('\n\n')

rules =  [[int(r) for r in rule.split('|')] for rule in input[0].split('\n')]
lines =  [[int(r) for r in inp.split(",")] for inp in input[1].split('\n')]

def get_rights(lines, is_break):
    right = []
    for numbers in lines:
        is_right = True
        
        for i, number in enumerate(numbers):

            for y in range(i):
                c_rules = [rule for rule in rules if rule[0] == number and rule[1] == numbers[y]]
                
                if (len(c_rules) > 0):
                    is_right = False
                    break

            for y in range(i, len(numbers)):
                c_rules = [rule for rule in rules if rule[1] == number and rule[0] == numbers[y]]
                
                if (len(c_rules) > 0):
                    is_right = False
                    break

        if (is_right and  is_break):
            return [numbers]

        if (is_right):
            right.append(numbers)

    return right


right = get_rights(lines, False)

sum = 0
for r in right:
    c = len(r) // 2
    sum += r[c]

print(sum)


def order(numbers):
    new = []
    for i, number in enumerate(numbers):
        if i == 0:
            new.append(number)
            continue

        left = [rule for rule in rules if rule[0] == number and rule[1] in new]
        right = [rule for rule in rules if rule[1] == number and rule[0] in new]

        if len(left) == 0:
            new.append(number)
            continue

        index = sorted([numbers.index(l[1]) for l in left])[0]
        new = new[:index] + [number] + new[index:]
        
    return new


sum = 0
for numbers in lines:
    ordered = order(numbers)

    while (True):
        tmp = order(ordered)
        if tmp == ordered:
            break

        ordered = tmp

    if numbers != ordered:
        print(ordered)
        c = len(ordered) // 2
        sum += ordered[c]

print(sum)
