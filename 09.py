#!/bin/python3
import sys
import itertools

inp = sys.argv[1]

files = []

empty = []
is_free_space = False
index = 0
for c in inp:
    ic = int(c)

    num = index
    if is_free_space:
        for i in range(ic):
            empty.append(len(files) + i)
        num = -1
    else:
        index += 1

    for i in range(ic):
        files.append(num)

    is_free_space = not is_free_space

while(True):
    if len(empty) == 0:
        break

    last = files[-1]

    if last == -1:
        files = files[:-1]
        continue

    files = files[:-1]

    insert_index = empty[0]
    if insert_index >= len(files):
        files.append(last)
    else:
        files[empty[0]] = last

    empty = empty[1:]

sum = 0
for i,f in enumerate(files):
    sum += i*f

print(sum)

files = []
is_free_space = False
index = 0
pos = 0

for c in inp:
    ic = int(c)

    num = index
    if not is_free_space:
        index += 1

    files.append((ic, pos, is_free_space, index-1))

    pos += ic
    is_free_space = not is_free_space

def get_first_free(files, l):
    for i, f in enumerate(files):
        if not f[2]:
            continue

        if f[0] >= l[0] and f[1] < l[1]:
            return i,f

    return None

index = len(files) - 1 

print(files)
print()

def print_files(files):
    line = ""
    for f in files:
        for l in range(f[0]):
            if f[2]:
                line+= "."
            else:
                line += str(f[3])
            

    print(line)

while(True):
    if index == 0:
        break

    print(index)
    last = files[index]
    index -= 1

    if last[2] == True:
        continue

    res = get_first_free(files, last)

    if res == None:
        continue

    i,f = res

    tmp = files[:i] + [(last[0], -1, last[2], last[3])]
    tmp_idx = index + 1
    if f[0] - last[0] > 0:
        tmp += [(f[0] - last[0], f[1] + last[0], True, last[3])]
        tmp_idx += 1

    tmp += files[i+1:]
    tmp[tmp_idx] = (last[0], last[1], True, last[3])
    files = tmp 
    index = tmp_idx - 1


i = 0
sum = 0
for ll, p, empty, any in files:
    for l in range(ll):
        i += 1

        if empty:
            continue

        sum += (i-1)*any



print(sum)
