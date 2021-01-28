lines = [line.strip() for line in open('input').readlines()]
lines = [(line[0], int(line[1:])) for line in lines]

# part1
moves = {
 'N' : (0, 1),
 'E' : (1, 0),
 'S' : (0, -1),
 'W' : (-1, 0),
}
dirs = list(moves.keys())

x, y = 0, 0
curr = 'E'

def rotate(angle, d):
    global curr
    sign = 1 if d == 'R' else -1
    for _ in range(n // 90):
        curr = dirs[(dirs.index(curr) + sign) % 4]


for ins in lines:
    d, n = ins
    if d in 'NEWS':
        dx, dy = moves[d]
        x + dx * n
        y += dy * n
    else:
        if d in 'LR':
            rotate(n, d)
        else:
            dx, dy = moves[curr]
            x += dx * n
            y += dy * n

print(abs(x) + abs(y))

x, y = 0, 0
wx, wy = 10, 1  # relative

def rotate(angle, d):
    global wx, wy
    if d == 'R':
        for _ in range(n // 90):
            wx, wy = wy, -wx
    else:
        assert d == 'L'
        for _ in range(n // 90):
            wx, wy = -wy, wx

for ins in lines:
    d, n = ins
    if d in 'NEWS':
        ix, iy = moves[d]
        wx += ix * n
        wy += iy * n
    else:
        if d in 'LR':
            rotate(n, d)
        else:
            x += wx * n
            y += wy * n

print(abs(x) + abs(y))
