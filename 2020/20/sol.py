x = 0
with open('grid.txt', 'r') as f:
    for line in f:
        row = line.strip()
        for c in row:
            if c == '#':
                x += 1

print(x)


lines = [line.strip() for line in open('grid.txt', 'r').readlines()]
print(len(lines), len(lines[0]))
