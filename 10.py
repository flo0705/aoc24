#!/bin/python3
import sys

lines = sys.argv[1].split('\n')
lines = [[int(c) for c in l] for l in lines]

def find_trailheads(lines):
    trailheads = []
    for il, l in enumerate(lines):
        for ic, c in enumerate(l):
            if c == 0:
                trailheads.append((il, ic))

    return trailheads

def find_next_step(next):

    l, c, level = next

    next_nexts = []

    for il in range(-1,2):
        for ic in range(-1, 2):
            if (il != 0 and ic != 0):
                continue

            nl = l + il
            nc = c + ic

            if nl < 0 or nc < 0 or nl >= len(lines) or nc >= len(lines[0]):
                continue

            if lines[nl][nc] != lines[l][c] + 1:
                continue

            next_nexts.append((nl, nc, lines[nl][nc]))

    return next_nexts

def to_key(next):
    return "-".join([str(n) for n in next])

def find_trails(start):
    cache = {}
    positions = [(start[0], start[1], 0)]

    count = 0

    while (True):
        if len(positions) == 0:
            break
    
        next = positions[0]
        positions = positions[1:]
        next_nexts = find_next_step(next)
        
        for pos in next_nexts:
            if to_key(pos) in cache:
                continue

            if pos[2] == 9:
                count += 1
            else:
                positions.append(pos)

        # Uncoment for Part 1
        #cache[to_key(pos)] = True

    return count
    

trailheads = find_trailheads(lines)
print(trailheads)
c = 0
for head in trailheads:
    score = find_trails(head)
    c += score
    print(head, score)

print(c)

