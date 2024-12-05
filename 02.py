#!/bin/python3
import sys

input = sys.argv[1]

input = input.split("\n")

sum = 0
for report in input:
    n_int = [int(n) for n in report.split(" ")]
    n_sorted = sorted(n_int)
    n_sorted_desc = sorted(n_int, reverse=True)

    if (n_sorted != n_int and n_sorted_desc != n_int):
        continue

    print(n_int)
    
    add = True
    for x,y in zip(n_int[:-1], n_int[1:]):
        if abs(x-y) < 1 or abs(x-y) > 3:
            add = False 

    if add:
        sum += 1
        
print(sum)

sum = 0
for report in input:
    n_int = [int(n) for n in report.split(" ")]

    variatios = [n_int]
    
    for idx,n in enumerate(n_int):
        nn = [n for nidx, n in enumerate(n_int) if idx != nidx]
        variatios.append(nn)

    for n_int in variatios:
        n_sorted = sorted(n_int)
        n_sorted_desc = sorted(n_int, reverse=True)

        if (n_sorted != n_int and n_sorted_desc != n_int):
            continue
        
        add = True
        for x,y in zip(n_int[:-1], n_int[1:]):
            if abs(x-y) < 1 or abs(x-y) > 3:
                add = False 

        if add:
            print(n_int)
            sum += 1
            break
        
print(sum)
