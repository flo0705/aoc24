#!/bin/python3
import sys
import itertools

lines = sys.argv[1].split('\n')

max_l = len(lines)
max_c = len(lines[0])
start = (0,0)
dir = 0

def get_move(dir):
    if dir == 0:
        return (-1, 0)
    if dir == 1:
        return (0, 1)
    if dir == 2:
        return (1, 0)
    if dir == 3:
        return (0, -1)

def move(liness, pos, dir):
    n_move = get_move(dir)
    n_pos = tuple([sum(x) for x in zip(pos, n_move)])

    if n_pos[0] < 0 or n_pos[1] < 0:
        return dir, n_pos, True

    if n_pos[0] >= max_l or n_pos[1] >= max_c:
        return dir, n_pos, True

    if liness[n_pos[0]][n_pos[1]] == '#' or liness[n_pos[0]][n_pos[1]] == 'O':
        dir += 1
        dir = dir % 4
        return dir, pos, False

    return dir, n_pos, False


for il, line in enumerate(lines):
    for ic, ch in enumerate(line):
        if ch == '^':
            start = (il, ic)

pos = start
moves = [start]
while(True):
    dir, pos, finished = move(lines, pos, dir)
    
    if (finished):
        break


    moves.append(pos)

print(len(set(moves)))

def is_in_loop(input, start, dir):
    pos = start
    moves = [start]
    cache = {}

    while(True):
        dir, pos, finished = move(input, pos, dir)
        k = "-".join([str(x) for x in pos + (dir,)])
        if k in cache:
            return True

        cache[k] = True
        
        if (finished):
            return False

def print_g(grid):
    for l in grid:
        print(l)

c = 0
for pos in set(moves[2:]):
    tmp = [x for x in lines]
    tmp[pos[0]] = tmp[pos[0]][:pos[1]] + "O" + tmp[pos[0]][pos[1]+1:]

    if (is_in_loop(tmp, start, 0)):
        c+=1

print(c)


















