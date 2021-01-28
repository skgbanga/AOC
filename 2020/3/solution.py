import math
grid = [line.strip() for line in open('input').readlines()]

def traverse(right, down):
    R = len(grid)
    C = len(grid[0])
    trees = 0
    r, c = 0, 0
    while r < R:
        if grid[r][c] == '#':
            trees += 1
        r += down
        c += right
        c %= C

    return trees

# print(traverse(3, 1))


m = 1
for cords in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    m = m * traverse(*cords)

print(m)
