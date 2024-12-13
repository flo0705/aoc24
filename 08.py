#!/bin/python3
import sys
import itertools

lines = sys.argv[1].split('\n')

def get_pairs(coords):
    pairs = []
    for coord in coords:
        for coord2 in coords:
            if coord == coord2:
                continue

            if (coord2, coord) in pairs:
                continue
            pairs.append((coord, coord2))

    return pairs

def get_distance(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])

freq = {}

for il, line in enumerate(lines):
    for ic, c in enumerate(line):
        if c != ".":
            if c in freq:
                freq[c].append((il, ic))
            else:
                freq[c] = [(il,ic)]


allAntis =  set([])

for f in freq:
    pairs = get_pairs(freq[f]) 

    for p1, p2 in pairs:
        dist = get_distance(p1, p2)
        anti1 = (p1[0] + dist[0], p1[1] + dist[1])
        anti2 = (p2[0] - dist[0], p2[1] - dist[1])

        if anti1[0] >= 0 and anti1[1] >= 0 and anti1[0] < len(lines) and anti1[1] < len(lines[0]):
            allAntis.add(anti1)

        if anti2[0] >= 0 and anti2[1] >= 0 and anti2[0] < len(lines) and anti2[1] < len(lines[0]):
            allAntis.add(anti2)

print(len(allAntis))
            

allAntis =  set([])

for f in freq:
    pairs = get_pairs(freq[f]) 

    for p1, p2 in pairs:
        dist = get_distance(p1, p2)

        allAntis.add(p1)
        allAntis.add(p2)
        anti1 = p1
        while (True):
            anti1 = (anti1[0] + dist[0], anti1[1] + dist[1])
            if anti1[0] >= 0 and anti1[1] >= 0 and anti1[0] < len(lines) and anti1[1] < len(lines[0]):
                allAntis.add(anti1)
            else:
                break

        anti2 = p2
        while (True):
            anti2 = (anti2[0] - dist[0], anti2[1] - dist[1])
            if anti2[0] >= 0 and anti2[1] >= 0 and anti2[0] < len(lines) and anti2[1] < len(lines[0]):
                allAntis.add(anti2)
            else:
                break

print(len(allAntis))

for il, l in enumerate(lines):
    line = ""
    for ic, c in enumerate(l):
        if (il, ic) in allAntis:
            line += "#"
        else:
            line += "."

    print(line)
