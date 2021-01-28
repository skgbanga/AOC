from collections import defaultdict
from math import inf
from itertools import permutations

lines = [line.strip() for line in open('input').readlines()]

# traveling salesman problem in a fully connected graph
g = defaultdict(dict)
for line in lines:
    a, _, b, _, n = line.split()
    g[a][b] = int(n)
    g[b][a] = int(n)

nodes = list(g.keys())
lo, hi = inf, 0
for path in permutations(nodes):
    s = sum(g[a][b] for a, b in zip(path, path[1:]))
    lo = min(lo, s)
    hi = max(hi, s)

print(lo, hi)

# dijkstra
def search(graph, source):
    distances = {}
    group = {source : 0}
    while group:
        key, weight = min(group.items(), key=lambda x:x[1])
        group.pop(key)
        distances[key] = weight
        for n, w in graph[key]:
            if n not in distances:
                group[n] = min(group.get(n, inf), weight + w)

    return distances
