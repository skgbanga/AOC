from collections import defaultdict
import re

lines = [line.strip() for line in open("input").readlines()]


d = defaultdict(int)

for line in lines:
    _, r, c, R, C = list(map(int, re.findall("\d+", line)))
    for dr in range(R):
        for dc in range(C):
            d[(r + dr, c + dc)] += 1


for line in lines:
    id, r, c, R, C = list(map(int, re.findall("\d+", line)))

    def good():
        for dr in range(R):
            for dc in range(C):
                if d[(r + dr, c + dc)] != 1:
                    return False
        return True

    if good():
        print(id)
        break
