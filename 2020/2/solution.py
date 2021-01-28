lines = [line.strip() for line in open('input').readlines()]
v = 0
for line in lines:
    a, b, c = line.split()
    x, y = [int(token) for token in a.split('-')]
    b = b[0]
    if (c[x - 1] == b) ^ (c[y - 1] == b):
        v += 1
print(v)
