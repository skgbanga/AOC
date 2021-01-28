from copy import deepcopy

lines = [line.strip() for line in open('input').readlines()]

R = len(lines)
C = len(lines[0])

g = [list(line) for line in lines]

while True:
    change = False
    ng = deepcopy(g)

    for r in range(R):
        for c in range(C):
            occ = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue

                    rr = r + dr
                    cc = c + dc
                    # part2 
                    while 0 <= rr < R and 0 <= cc < C and g[rr][cc] == '.':
                        rr += dr
                        cc += dc

                    if 0 <= rr < R and 0 <= cc < C and g[rr][cc] == '#':
                        occ += 1

            pt = g[r][c]
            if pt == 'L' and occ == 0:
                ng[r][c] = '#'
                change = True
            elif pt == '#' and occ >= 5:
                ng[r][c] = 'L'
                change = True

    if not change:
        break

    g = deepcopy(ng)

cnt = 0
for row in g:
    cnt += sum(1 for c in row if c == '#')

print(cnt)
