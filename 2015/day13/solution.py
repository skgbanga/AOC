from collections import defaultdict
from itertools import permutations

lines = [line.strip()[:-1] for line in open('input').readlines()]

g = defaultdict(dict)
for line in lines:
    a, _, action, num, _, _, _, _, _, _, b = line.split()
    if action == 'gain':
        num = int(num)
    elif action == "lose":
        num = -int(num)
    g[a][b] = num

def happiness():
    m = 0
    for s in permutations(g.keys()):
        m = max(m, sum(g[a][b] + g[b][a] for a, b in zip(s, s[1:] + s[:1])))
    print(m)

# part1
happiness()

for n in list(g.keys()):
    g[n]['you'] = 0
    g['you'][n] = 0

happiness()
