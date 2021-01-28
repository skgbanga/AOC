lines = [line.strip() for line in open('input').readlines()]
line = lines[0]

moves = {
        '^' : (0, 1),
        '>' : (1, 0),
        '<' : (-1, 0),
        'v' : (0, -1)
}

def santa(start):
    visited = set()
    x, y = 0, 0
    visited.add((x, y))
    for c in line[start::2]:
        dx, dy = moves[c]
        x += dx
        y += dy
        visited.add((x, y))

    return visited


print(len(santa(0) | santa(1)))
