import re

lines = [line.strip() for line in open('input').readlines()]
lines = lines[2:]

R = 33
C = 30
grid = [[0] * C for _ in range(R)]

class Data:
    def __init__(self, size, used, avail):
        self.size = size
        self.used = used
        self.avail = avail

for line in lines:
    r, c, size, used, avail, usep = map(int, re.findall('\d+', line))
    grid[r][c] = Data(size, used, avail)


# def check(r, c, used):
#     viable = []
#     for rr in range(R):
#         for cc in range(C):
#             if rr == r and cc == c:
#                 continue
#             if used <= grid[rr][cc][2]:
#                 viable.append((rr, cc))
#     return viable

# counts = set()
# s = 0
# for r in range(R):
#     for c in range(C):
#         used = grid[r][c][1]
#         if used != 0:
#             viable = check(r, c, used)
#             if viable:
#                 counts.update(viable)
#                 s += len(viable)
#                 # print(r, c, "->", viable[0])

# print(s, counts)


# purpose is move goal to access
access = (0, 0)
goal = (R - 1, 0)


# find hole
def hole():
    for r in range(R):
        for c in range(C):
            if grid[r][c].used == 0:
                return (r, c)
    assert False


# move hole to goal
def bfs(r, c, avail):
    from collections import deque
    d = deque([(r, c)])
    seen = set([(r, c)])
    cnt = 0
    while d:
        cnt += 1
        l = len(d)
        for _ in range(l):
            r, c = d.popleft()
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (rr, cc) == goal:
                    return cnt

                if 0 <= rr < R and 0 <= cc < C and (rr, cc) not in seen:
                    if grid[rr][cc].used <= avail:
                        d.append((rr, cc))
                        seen.add((rr, cc))

    assert False, "can't reach goal"

# move hole to goal
r, c = hole()
steps = bfs(r, c, grid[r][c].avail)
print(steps)
print((R - 2) * 5)
for r in range(R):
    for c in range(0, 2):
        d = grid[r][c]
        print(d.used, d.avail, end=' | ')
        if d.used > 90:
            print(d.used, d.avail, d.size)
    print()
