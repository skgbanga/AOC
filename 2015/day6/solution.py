lines = [line.strip() for line in open('input').readlines()]

grid = []
for _ in range(1000):
    grid.append([0] * 1000)

def op(start, end, action):
    x1, y1 = [int(token) for token in start.split(',')]
    x2, y2 = [int(token) for token in end.split(',')]

    for dx in range(x2 - x1 + 1):
        for dy in range(y2 - y1 + 1):
            x = x1 + dx
            y = y1 + dy
            grid[x][y] = action(grid[x][y])

d = {
    'turn on' : lambda x: x + 1,
    'turn off' : lambda x: max(0, x - 1),
    'toggle': lambda x: x + 2
}

for line in lines:
    ins, start, _, end = line.rsplit(maxsplit=3)
    op(start, end, d[ins])

print(sum(sum(s) for s in grid))
