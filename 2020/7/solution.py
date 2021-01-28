from collections import deque
lines = [line.strip()[:-1] for line in open('input').readlines()]


contained = []
contains = []


for line in lines:
    first, *args = [token.strip() for token in line.split(',')]
    a, b = [token.strip() for token in first.split('contain')]

    others = [b]
    others.extend(args)
    for arg in others:
        wt, color = [token.strip() for token in arg.split(maxsplit=1)]
        if wt == '1':
            color = color + 's'
        if wt != 'no':
            contained.append((color, a, int(wt)))
            contains.append((a, color, int(wt)))


# part 1
group = deque()
group.append(('shiny gold bags'))
visited = {}
while group:
    color = group.popleft()
    visited[color] = True
    for a, b, _ in contained:
        if a == color and b not in visited:
            group.append(b)

print(len(visited) - 1)


# part2
wt = 0
group = deque()
group.append(('shiny gold bags', 1))

while group:
    color, mult = group.popleft()
    for a, b, w in contains:
        if a == color:
            wt += mult * w
            group.append((b, mult * w))

print(wt)
