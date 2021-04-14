from functools import lru_cache
from itertools import permutations

grid = [line.strip() for line in open('input2').readlines()]

R, C = len(grid), len(grid[0])

pos = {}
for r in range(R):
    for c in range(C):
        if grid[r][c].isdigit():
            pos[grid[r][c]] = (r, c)

@lru_cache
def bfs(start, end):
    from collections import deque
    d = deque()
    d.append((start, [start]))
    seen = set([start])
    cnt = 0
    while d:
        cnt += 1
        num = len(d)
        for _ in range(num):
            (r, c), path = d.popleft()
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if rr == end[0] and cc == end[1]:
                    return cnt, path

                if grid[rr][cc] != '#' and (rr, cc) not in seen:
                    p = path.copy()
                    p.append((rr, cc))
                    d.append(((rr, cc), p))
                    seen.add((rr, cc))

    return float('+inf')

def path(route):
    s, p = 0, []
    for a, b in zip(route, route[1:]):
        d, pp = bfs(pos[a], pos[b])
        s += d
        p.extend(pp)
    return s, p

keys = set(pos.keys())
keys.remove('0')
m, p = float('+inf'), []
for route in permutations(keys):
    mm, pp = path('0' + ''.join(route))
    if mm < m:
        m = mm
        p = pp

import time
def show(pos):
    rr, cc = pos
    s = ''
    for r in range(R):
        for c in range(C):
            s += '*' if r == rr and c == cc else grid[r][c]
        s += '\n';
    print('\033c')
    print(s)
    time.sleep(0.5)


for pos in p:
    show(pos)
