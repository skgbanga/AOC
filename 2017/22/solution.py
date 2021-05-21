lines = open("input").read().splitlines()

R, C = len(lines), len(lines[0])

from collections import defaultdict

seen = defaultdict(int)
for r in range(R):
    for c in range(C):
        seen[(r, c)] = 1 if lines[r][c] == "#" else 0

r, c = R // 2, C // 2
d = 1

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

s = 0
for _ in range(10_000_000):
    state = seen[(r, c)]
    if state == 0:
        d = (d - 1) % 4
    elif state == 1:
        d = (d + 1) % 4
    elif state == 3:
        d = (d + 2) % 4
    else:
        assert state == 2, f"{state}"

    if state == 0:
        seen[(r, c)] = 2
    elif state == 2:
        seen[(r, c)] = 1
        s += 1
    elif state == 1:
        seen[(r, c)] = 3
    else:
        assert state == 3, f"{state}"
        seen[(r, c)] = 0

    r, c = r + dr[d], c + dc[d]


print(s)
