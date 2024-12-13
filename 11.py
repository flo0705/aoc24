#!/bin/python3
import sys

stones = sys.argv[1].split(' ')
stones = [int(stone) for stone in stones]

def move(stones):
    n_list = []
    for stone in stones:
        if stone == 0:
            n_list.append(1)
            continue

        if len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            half = len(str_stone) // 2
            n_list.append(int(str_stone[:half]))
            n_list.append(int(str_stone[half:]))
            continue

        n_list.append(stone * 2024)

    return n_list



new = stones
for i in range(25):
    new = move(new)

print(len(new))

mapping = {
    0: [1],
    1: [2024],
    2024: [20, 24]
}

counter = {}

for stone in stones:
    counter[stone] = 1

def n_move(counter):
    cc = dict(counter)
    keys = [k for k in counter if counter[k] != 0]
    for k in keys:
        if k in mapping:
            mapped = mapping[k]

            for m in mapped:
                if m in cc:
                    cc[m] += counter[k]
                else:
                    cc[m] = counter[k]

            cc[k] -= counter[k]
            continue

        if len(str(k)) % 2 == 0:
            str_stone = str(k)
            half = len(str_stone) // 2
            mapping[k] = [int(str_stone[:half]), int(str_stone[half:])]

            for m in mapping[k]:
                if m in cc:
                    cc[m] += counter[k]
                else:
                    cc[m] = counter[k]

            cc[k] -= counter[k]
            continue

        mapping[k] = [k*2024]
        cc[k*2024] = counter[k]
        cc[k] -= counter[k]

    return cc

def count(counter):
    line = ""
    sum = 0
    for k in counter:
        if counter[k] != 0:
            line += " ("
            line += str(k)
            line += ","
            line += str(counter[k])
            line += ") "
        sum += counter[k]
    
    #print(line)
    return sum

new = stones
for i in range(75):
    counter = n_move(counter)
    #print(counter)

print(count(counter))
