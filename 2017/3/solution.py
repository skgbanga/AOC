import math
import itertools

target = 361527

R, C = 1001, 1001
mat = [[0] * C for _ in range(R)]

r, c = 500, 500
mat[r][c] = 1

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

num = 1
def check():
    if num > target:
        m = abs(r - 500) + abs(c - 500)
        print(r, c, m)
        exit(1)

def ns(r, c):
    s = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            rr = r + dr
            cc = c + dc
            s += mat[rr][cc]
    print(f"For {r}, {c} num = {s}")
    return s

while True:
    for rad in itertools.count(2, 2):
        r, c = r, c + 1
        num = ns(r, c)
        check()
        for d in range(4):
            b = rad - 1 if d == 0 else rad
            for _ in range(b):
                check()
                mat[r][c] = num
                r += dr[d]
                c += dc[d]
                num = ns(r, c)

        mat[r][c] = num
