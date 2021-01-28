from collections import namedtuple

lines = [line.strip() for line in open('input').readlines()]

# lines = ["R8,U5,L5,D3", "U7,R6,D4,L4"]

point = namedtuple('point', 'x y')
class line:
    def __init__(self, start, end, delay):
        self.start = start
        self.end = end
        self.delay = delay

    def horizontal(self):
        return self.start.y == self.end.y


def coords(row):
    co = []
    sx, sy = 0, 0
    delay = 0
    for l in row.split(','):
        d = l[0]
        num = int(l[1:])
        ex, ey = sx, sy
        if d == 'R':
            ex += num
        elif d == 'L':
            ex -= num
        elif d == 'U':
            ey += num
        elif d == 'D':
            ey -= num
        else:
            assert False

        delay += num
        co.append(line(point(sx, sy), point(ex, ey), delay))
        sx, sy = ex, ey
    return co

assert len(lines) == 2
A = coords(lines[0])
B = coords(lines[1])

m = 100_000_0000

def match(a, b):
    global m
    assert a.start.y == a.end.y
    assert b.start.x == b.end.x
    if (a.start.x <= b.start.x <= a.end.x or a.end.x <= b.start.x <= a.start.x) and (
        b.start.y <= a.start.y <= b.end.y or b.end.y <= a.start.y <= b.start.y):
        manhattan = abs(a.start.y) + abs(b.start.x)
        sa = abs(a.end.x - b.start.x)
        sb = abs(b.end.y - a.start.y)
        d = a.delay + b.delay - sa - sb
        if manhattan != 0:
            m = min(m, d)

for a in A:
    for b in B:
        if a.horizontal() and not b.horizontal():
            match(a, b)
        elif not a.horizontal() and b.horizontal():
            match(b, a)

print(m)
