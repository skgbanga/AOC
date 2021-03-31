line = open('input', 'r').readlines()[0].strip()
tokens = [token.strip(" ,") for token in line.split()]

d = 0
x, y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

locs = set()
for token in tokens:
    moves = int(token[1:])
    if token[0] == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4

    for _ in range(moves):
        x, y = x + dx[d], y + dy[d]
        if (x, y) in locs:
            print(abs(x) + abs(y))
            break
        else:
            locs.add((x, y))
