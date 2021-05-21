import re
from collections import defaultdict, deque

lines = (line.strip() for line in open("input").readlines())
g = defaultdict(list)

for line in lines:
    a, *args = list(map(int, re.findall("\d+", line)))
    g[a].extend(args)

groups = 0
seen = set()
for key in g.keys():
    if key not in seen:
        d = deque([key])
        seen.add(key)
        while d:
            num = d.popleft()
            for ns in g[num]:
                if ns not in seen:
                    d.append(ns)
                    seen.add(ns)

        groups += 1

print(groups)
