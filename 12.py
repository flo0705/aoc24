#!/bin/python3
import sys

lines = sys.argv[1].split('\n')

def find_region(regions, il, ic, c):

    regions_idxs = []

    for i, region in enumerate(regions):
        if ((il - 1, ic, c) in region):
            regions_idxs.append(i)
        if ((il + 1, ic, c) in region):
            regions_idxs.append(i)
        if ((il, ic  - 1, c) in region):
            regions_idxs.append(i)
        if ((il, ic  + 1, c) in region):
            regions_idxs.append(i)

    nr = []
    for i, region in enumerate(regions):
        if i in regions_idxs:
            continue

        nr.append(region)

    conc = [(il, ic, c)]
    for idx in regions_idxs:
        conc += regions[idx]

    nr.append(list(set(conc)))
    return nr


def find_regions(lines):
    regions = []

    for il, line in enumerate(lines):
        for ic, c in enumerate(line):
            regions = find_region(regions, il, ic, c)

    return regions

def print_region(region):
    for il, line in enumerate(lines):
        p = ""
        for ic, c in enumerate(line):
            if (il, ic, c) in region:
                p += c
            else:
                p += "."
        print(p)

def get_neighbours_count(region, elem):
    count = 0
    neigs = []
    for r in region:
        diff0 = abs(r[0] - elem[0])
        diff1 = abs(r[1] - elem[1])
        if diff0 + diff1 == 1:
            count += 1
            neigs.append(r)


    if count == 2 and len(set([neig[0] for neig in neigs])) == 1 :
        return 0
            
    if count == 2 and len(set([neig[1] for neig in neigs])) == 1:
        return 0
    return count

def get_region_perimeter(region):
    if len(region) == 1:
        return 4

    peri = 0
    for r in region:
        neigs = get_neighbours_count(region, r)

        if neigs == 1:
            peri += 3
        if neigs == 2:
            peri += 2
        if neigs == 3:
            peri += 1

    return peri

def is_inner_edge(r, region):
    (il, ic , c) = r
    num = 0
    if ((il - 1, ic + 1, c) not in region and (il - 1, ic, c) in region and (il, ic + 1, c) in region):
        num += 1
    if ((il - 1, ic - 1, c) not in region and (il - 1, ic, c) in region and (il, ic - 1, c) in region):
        num += 1
    if ((il + 1, ic + 1, c) not in region and (il + 1, ic, c) in region and (il, ic + 1, c) in region):
        num += 1
    if ((il + 1, ic  - 1, c) not in region and (il + 1, ic, c) in region and (il, ic - 1, c) in region):
        num += 1

    return num

def get_region_sides(region):
    if len(region) == 1:
        return 4

    region = sorted(region)
    sides = 0
    for r in region:
        neigs = get_neighbours_count(region, r)

        inner = is_inner_edge(r, region)
        if is_inner_edge(r, region):
            sides += inner 
        if neigs == 2:
            sides += 1
        if neigs == 1:
            sides += 2

    return sides


regions = find_regions(lines)

sum1 = 0
for region in regions:
    peri = get_region_perimeter(region)
    sum1 += len(region) * peri

print(sum1)

sum1 = 0
for region in regions:
    sides = get_region_sides(region)
    sum1 += len(region) * sides

print(sum1)
