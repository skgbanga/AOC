def rotate(old):
    S = len(old)
    new = [[0] * S for _ in range(S)]

    def rotate_frame(start, size):
        rg = range(start, start + size)
        end = start + size - 1
        for idx in rg:
            new[start + idx][end] = old[start][start + idx]
        for idx in rg:
            new[end][end - idx] = old[start + idx][end]
        for idx in rg:
            new[end - idx][start] = old[end][end - idx]
        for idx in rg:
            new[start][start + idx] = old[end - idx][start]

    start = 0
    for s in range(S, 0, -2):
        rotate_frame(start, s)
        start += 1
    return new


def flip_vertical(old):
    S = len(old)
    new = [[0] * S for _ in range(S)]
    for c in range(S):
        o = S - c - 1
        for r in range(S):
            new[r][o] = old[r][c]
    return new

def flip_horizontal(old):
    S = len(old)
    new = [[0] * S for _ in range(S)]
    for r in range(S):
        o = S - r - 1
        for c in range(S):
            new[o][c] = old[r][c]
    return new
