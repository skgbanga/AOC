import math
from collections import deque
lines = [line.strip() for line in open('input').readlines()]

nodes = set()
edges = []
for line in lines:
    a, b = line.split(')')
    nodes.add(a)
    nodes.add(b)
    edges.append((a, b))


# def visit(node):
#     q = deque()
#     visited = set()
#     q.append(node)
#     while q:
#         n = q.popleft()
#         visited.add(n)
#         for a, b in edges:
#             if b == n and a not in visited:
#                 q.append(a)
#     return len(visited) - 1


# print(visit('C'))
# s = 0
# for node in nodes:
#     v = visit(node)
#     # print(node, v)
#     s += v
# print(s)

# print(visit())


distance = {}
for node in nodes:
    distance[node] = math.inf

distance['YOU'] = 0
visited = set()
q = deque()
q.append('YOU')
while q:
    n = q.popleft()
    visited.add(n)
    for a, b in edges:
        if a == n or b == n:
            other = a if b == n else b
            if other not in visited:
                distance[other] = min(distance[other], distance[n] + 1)
                q.append(other)


print(distance['SAN'] - 2)
# print(len(distance))
# l = [k for k, v in distance.items() if v != math.inf]
# print(len(l))

# for k, v in distance.items():
#     print(k, v)
