from copy import deepcopy
from collections import defaultdict

lines = [line.strip() for line in open('input').readlines()]
d = len(lines)
start = 0
print(d)

cube = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : defaultdict(int))))

rg = range(start, start + d)
for x in rg:
    for y in rg:
        v = lines[x][y]
        if v == '.':
            cube[x][y][0][0] = 0
        else:
            assert v == '#'
            cube[x][y][0][0] = 1


def zero():
    print('=' * 8)
    rg = range(start, start + d)
    for x in rg:
        for y in rg:
            print(cube[x][y][0], end=' ')
        print()


# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.

def count():
    s = 0
    rg = range(start, start + d)
    for x in rg:
        for y in rg:
            for z in rg:
                for w in rg:
                    if cube[x][y][z][w] == 1:
                        s += 1
    return s


copy = deepcopy(cube)
def turn():
    rg = range(start, start + d)
    # print(rg)
    for x in rg:
        for y in rg:
            for z in rg:
                for w in rg:
                    s = 0
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            for dz in (-1, 0, 1):
                                for dw in (-1, 0, 1):
                                    if not (dx == 0 and dy == 0 and dz == 0 and dw == 0):
                                        if cube[x + dx][y + dy][z + dz][w + dw] == 1:
                                            s += 1
                    # print(x, y, z, s)
                    if cube[x][y][z][w] == 1:
                        if s == 2 or s == 3:
                            pass
                        else:
                            copy[x][y][z][w] = 0
                    else:
                        if s == 3:
                            copy[x][y][z][w] = 1



for _ in range(6):
    d += 2
    start += -1
    turn()
    cube = deepcopy(copy)
# zero()


print(count())
