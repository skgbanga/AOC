def show_block(block):
    for row in block:
        for c in row:
            print(f'{c:02}', end=' ')
        print()
    print("===")


def rotate(old):
    S = len(old)
    new = [[0] * S for _ in range(S)]

    def rotate_frame(start, size):
        rg = range(0, size)
        end = start + size - 1

        for idx in rg:
            new[start + idx][end]   = old[start][start + idx]

        for idx in rg:
            new[end][end - idx]     = old[start + idx][end]

        for idx in rg:
            new[end - idx][start]   = old[end][end - idx]

        for idx in rg:
            new[start][start + idx] = old[end - idx][start]
        show_block(old)
        show_block(new)

    start = 0
    for s in range(S, 0, -2):
        rotate_frame(start, s)
        start += 1

    return new


dim = 10
old = [[0] * dim for _ in range(dim)]

x = 0
for r in range(dim):
    for c in range(dim):
        old[r][c] = x
        x += 1

new = rotate(old)
