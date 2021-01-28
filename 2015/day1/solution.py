from collections import *

lines = []
with open('input', 'r') as f:
    for line in f:
        lines.append(line.strip())

c = Counter(lines[0])
print(c['('] - c[')'])

floor = 0
for idx, c in enumerate(lines[0], start=1):
    if c == '(':
        floor += 1
    else:
        floor -= 1
        if floor == -1:
            print(idx)
            break
