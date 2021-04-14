import sys
sys.setrecursionlimit(2000)

import hashlib
code = "ioramepc"

R, C = 4, 4

opened = set('bcdef')
closed = set('0123456789a')

def longest(r, c, path):
    if r == R - 1 and c == C - 1:
        return len(path)

    p = code + path
    up, down, left, right = hashlib.md5(p.encode()).hexdigest()[:4]

    n = 0
    def add(rr, cc, pp):
        nonlocal n
        if 0 <= rr < R and 0 <= cc < C:
            n = max(n, longest(rr, cc, pp))

    if up in opened:
        add(r - 1, c, path + 'U')
    if down in opened:
        add(r + 1, c, path + 'D')
    if left in opened:
        add(r, c - 1, path + 'L')
    if right in opened:
        add(r, c + 1, path + 'R')

    return n

def shortest(r, c):
    from collections import deque
    d = deque([(r, c, '')])
    seen = set([(r, c, '')])

    def add(rr, cc, pp):
        t = (rr, cc, pp)
        if 0 <= rr < R and 0 <= cc < C and t not in seen:
            d.append(t)
            seen.add(t)

    while d:
        n = len(d)
        for _ in range(n):
            r, c, path = d.popleft()
            if r == R - 1 and c == C - 1:
                print("Found ", path)
                return

            p = code + path
            up, down, left, right = hashlib.md5(p.encode()).hexdigest()[:4]
            if up in opened:
                add(r - 1, c, path + 'U')
            if down in opened:
                add(r + 1, c, path + 'D')
            if left in opened:
                add(r, c - 1, path + 'L')
            if right in opened:
                add(r, c + 1, path + 'R')

    print("Not found")


def longest(r, c, path):
    if r == R - 1 and c == C - 1:
        return len(path)

    p = code + path
    up, down, left, right = hashlib.md5(p.encode()).hexdigest()[:4]

    n = 0
    def add(rr, cc, pp):
        nonlocal n
        if 0 <= rr < R and 0 <= cc < C:
            n = max(n, longest(rr, cc, pp))

    if up in opened:
        add(r - 1, c, path + 'U')
    if down in opened:
        add(r + 1, c, path + 'D')
    if left in opened:
        add(r, c - 1, path + 'L')
    if right in opened:
        add(r, c + 1, path + 'R')

    return n

n = longest(0, 0, '')
print(n)
