'''
Its left and center tiles are traps, but its right tile is not.
Its center and right tiles are traps, but its left tile is not.
Only its left tile is a trap.
Only its right tile is a trap.
'''

lines = [line.strip() for line in open('input').readlines()]
assert len(lines) == 1
start = lines[0]

grid = []
grid.append(list(start))

for i in range(1, 40):
    n = []
    prev = ['.'] + grid[i - 1] + ['.']
    for a in zip(prev, prev[1:], prev[2:]):
        if ''.join(a) in ('^^.', '.^^', '^..', '..^'):
            n.append('^')
        else:
            n.append('.')
    grid.append(n)

s = 0
for row in grid:
    s += sum(k == '.' for k in row)
print(s)
