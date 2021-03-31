from collections import defaultdict
import sys
import re

lines = [[line.strip(), False] for line in open('input').readlines()]
bots = defaultdict(list)
outputs = {}

# set it up
for line in lines:
    ins, _ = line
    if ins.startswith('value'):
        value, bot = map(int, re.findall('\d+', ins))
        bots[bot].append(value)
        line[1] = True

# run simulation
while True:
    changed = False
    for line in lines:
        ins, executed = line
        if executed:
            continue

        a, b, c = map(int, re.findall('\d+', ins))
        if len(bots[a]) == 2:
            changed = True
            x, y = bots[a]
            lo, hi = min(x, y), max(x, y)
            if ins.count('output') == 1:
                outputs[b] = lo
                bots[c].append(hi)
            elif ins.count('output') == 2:
                outputs[b] = lo
                outputs[c] = hi
            else:
                bots[b].append(lo)
                bots[c].append(hi)
            line[1] = True

    if not changed:
        break

m = 1
for k in (0, 1, 2):
    m *= outputs[k]
print(m)
