from more_itertools import chunked

lines = [line.strip() for line in open('input').readlines()]
triangles = [list(map(int, line.split())) for line in lines]
triangles = list(zip(*triangles))

def valid(t):
    a, b, c = sorted(t)
    return a + b > c

print(sum(valid(t) for row in triangles for t in chunked(row, 3)))
