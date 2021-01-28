from copy import deepcopy
lines = [line.strip() for line in open('input').readlines()]

tiles = set()
black = set()
dirs = ('e', 'se', 'sw', 'w', 'nw', 'ne')
for line in lines:
    ds = []
    while line:
        for d in dirs:
            if line.startswith(d):
                ds.append(d)
                line = line[len(d):]
                break

    x, y = 0, 0
    for d in ds:
        if d == 'e':
            x, y = x + 1, y
        elif d == 'w':
            x, y = x - 1, y
        elif d == 'ne':
            x, y = x + 1/2, y + 1
        elif d == 'nw':
            x, y = x - 1/2, y + 1
        elif d == 'se':
            x, y = x + 1/2, y - 1
        elif d == 'sw':
            x, y = x - 1/2, y - 1
        else:
            assert False

    tt = (x, y)
    tiles.add(tt)
    if tt in black:
        black.remove(tt)
    else:
        black.add(tt)

# print(len(tiles))
print(len(black))

def ns(x, y):
    return [(x + 1, y),
            (x - 1, y),
            (x + 1/2, y + 1),
            (x - 1/2, y + 1),
            (x + 1/2, y - 1),
            (x - 1/2, y - 1)]

for _ in range(100):
    next_tiles = set()
    for x, y in tiles:
        next_tiles.add((x, y))
        next_tiles.update(ns(x, y))

    next_black = deepcopy(black)
    for x, y in next_tiles:
        tt = (x, y)
        b = sum(n in black for n in ns(x, y))

        if tt in black:
            assert tt in next_black
            if b == 0 or b > 2:
                next_black.remove(tt)
        else:
            if b == 2:
                next_black.add(tt)

    tiles = deepcopy(next_tiles)
    black = deepcopy(next_black)

print(len(black))
