def cycle(a, b):
    ai = 0
    bi = 0
    turn = 'a'
    while ai < len(a) or bi < len(b):
        if turn == 'a':
            turn = 'b'
            if ai < len(a):
                yield a[ai]
                ai += 1
        else:
            assert turn == 'b'
            turn = 'a'
            if bi < len(b):
                yield b[bi]
                bi += 1


# x = [1, 2, 3, 4]
# y = ['a', 'b']
# print(list(cycle(x, y)))
# assert False

from fractions import Fraction
import math
from collections import Counter, defaultdict, deque
from contextlib import suppress
from functools import partial

G = [list(line.strip()) for line in open('input').readlines()]
R = len(G)
C = len(G[0])
print(R, C)
# print(R, C)

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.vertical = False
        if x1 == x2:
            self.vertical = True
            self.x = x1
        else:
            self.a = Fraction(y1 - y2, x1 - x2)
            self.c = Fraction(x1 * y2 - x2 * y1,  x1 - x2)


    def check(self, x, y):
        if self.vertical:
            return x == self.x
        else:
            return y == self.a * x + self.c

    def __eq__(self, other):
        if self.vertical and other.vertical:
            return self.x == other.x
        elif not self.vertical and not other.vertical:
            # return self.a == other.a and self.c == other.c
            return self.a == other.a

        return False

    def __str__(self):
        if self.vertical:
            return str(math.inf)
        return str(self.a)

# X -> C
# Y -> R
# column comes first

def exists(px, py, line):
    s = set()
    for y in range(R):
        for x in range(C):
            if x == px and y == py:
                continue

            if G[y][x] == '#' and line.check(x, y):
                s.add((x, y))

    return s
    
def stations(px, py):
    def distance1(v):
        x, y = v
        return (x - px) + (y - py)
    
    def picks1(_, s):
        p = set()
        with suppress(ValueError):
            p.add(min(v for v in s if distance1(v) >= 0))
        with suppress(ValueError):
            p.add(max(v for v in s if distance1(v) <= 0))

        return p

    def distance2(p, line):
        x, y = p
        if line.vertical:
            assert y - py != 0
            return y - py
        assert px - x != 0
        return px - x

    def picks2(line, s):
        p = set()
        with suppress(ValueError):
            p.add(min(v for v in s if distance2(v, line) > 0))
        with suppress(ValueError):
            p.add(max(v for v in s if distance2(v, line) < 0))

        return p

    lines = []
    pts = []
    m = 0
    su = set()
    for y in range(R):
        for x in range(C):
            if y == py and x == px:
                continue

            line = Line(px, py, x, y)
            if line not in lines:
                s = exists(px, py, line)
                if s:
                    assert picks1(line, s) == picks2(line, s), f'{picks1(line, s)} != {picks2(line, s)} . {s}'
                    ps = picks2(line, s)
                    su.update(ps)
                    print(ps)
                    m += len(ps)
                    lines.append(line)
                    pts.append(s)

    print('unique', len(su))
    return m, lines, pts

mpt = (1, 20)
x, y = mpt
print(G[y][x])
m, mlines, mpts = stations(x, y)
print('=', m)
exit(1)
# assert False

m = 0
for y in range(R):
    for x in range(C):
        if G[y][x] == '#':
            n, lines, pts = stations(x, y)
            if n >= m:
                print(f'Changing to ({x}, {y}) because m = {m} and n = {n}')
                m = n
                mpt = (x, y)
                mlines = lines
                mpts = pts


print(m)
print(mpt)
px, py = mpt
def slope(lp):
    line, _ = lp
    if line.vertical:
        return -math.inf
    return line.a

lines = list(zip(mlines, mpts))
lines = sorted(lines, key=slope)

def distance(p, line):
    x, y = p
    if line.vertical:
        assert y - py != 0
        return y - py
    assert px - x != 0
    return px - x

flines = []
for line, pts in lines:
    s1 = sorted([p for p in pts if distance(p, line) < 0], reverse=True, key=partial(distance, line=line))
    s2 = sorted([p for p in pts if distance(p, line) > 0], key=partial(distance, line=line) )
    s = deque(cycle(s1, s2))
    flines.append((line, s))

print('Number of lines = ', len(flines))

m = 0
for idx, (line, pts) in enumerate(flines, start=1):
    print(idx, line, pts, m)
    m += len(pts)

G[py][px] = 'X'
d = {}
idx = 1
markers = set()
def draw():
    print('---')
    for row in G:
        print(''.join(row))
    print('---')



while True:
    yielded = False
    def do(sign):
        global yielded
        global idx
        global markers
        for line, pts in flines:
            if pts:
                pt = pts[0]
                if (sign == '+' and distance(pt, line) > 0) or (sign == '-' and distance(pt, line) < 0):
                    pt = pts.popleft()
                    d[idx] = pt
                    idx += 1
                    mx, my = pt
                    markers.add(pt)
                    G[my][mx] = str(len(markers))
                    if len(markers) == 40:
                        draw()
                        for marker in markers:
                            mx, my = marker
                            G[my][mx] = '.'
                        markers = set()
                    yielded = True

    do('-')
    do('+')
    if not yielded:
        break

for x, y in d.items():
    print(x, y)
# x, y = d[200]
# print(x, y)
# print(100 * x + y)
