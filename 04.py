#!/bin/python3
import sys

input = sys.argv[1].split('\n')

def get_words_count(l, c):
    directions = [(x,y) for x in range(-1,2) for y in range(-1,2)]

    count = 0
    for dir in directions:
        nl = l
        nc = c
        word = ""
        for i in range(3):
            if nl+dir[0] < 0 or nc+dir[1] < 0:
                continue

            if nl+dir[0] >= len(input) or nc+dir[1] >= len(input[0]):
                continue

            word += input[nl+dir[0]][nc+dir[1]]
            nl = nl+dir[0]
            nc = nc+dir[1]
        
        if word == "MAS":
            count+=1
         
    return count


def find_word(startl, startc):
    move = (startl,startc)
    return get_words_count(startl, startc)

c = 0
for il, line in enumerate(input):
    for ic, char in enumerate(line):
        if char == "X":
            c += find_word(il, ic)

print(c)


def get_ms_position(l, c):
    directions = [(x,y) for x in range(-1,2) for y in range(-1,2)]

    count = 0
    ms = []
    for dir in directions:
        if (dir[0] == 0 or dir[1] == 0):
            continue
        nl = l
        nc = c
        word = ""
        for i in range(2):
            if nl+dir[0] < 0 or nc+dir[1] < 0:
                continue

            if nl+dir[0] >= len(input) or nc+dir[1] >= len(input[0]):
                continue

            word += input[nl+dir[0]][nc+dir[1]]
            nl = nl+dir[0]
            nc = nc+dir[1]
        
        if word == "AS":
            coord = (nl-dir[0], nc-dir[1])
            ms.append((nl-dir[0], nc-dir[1]))
            count+=1
         
    return list(set(ms))


ms = []
for il, line in enumerate(input):
    for ic, char in enumerate(line):
        if char == "M":
            ms += get_ms_position(il, ic)

duplicates = list(set([num for num in ms if ms.count(num) > 1]))
print(len(duplicates))





