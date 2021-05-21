import math
from more_itertools import chunked

lines = [rule for rule in open("input").read().splitlines()]
rules = {}
for line in lines:
    a, b = [token.strip() for token in line.split("=>")]
    rules[a] = b

s = """
.#.
..#
###
"""

pic = [line for line in s.splitlines() if line]


def linear(m):
    return "/".join("".join(row) for row in m)


def square(m):
    return [list(row) for row in m.split("/")]


def copy(r, c, s):
    mat = [["."] * s for _ in range(s)]
    for rr in range(s):
        for cc in range(s):
            mat[rr][cc] = pic[r + rr][c + cc]
    return mat


def rotate(mat):
    from copy import deepcopy

    mat2 = deepcopy(mat)

    S = len(mat)
    for _ in range(4):
        for r in range(S):
            for c in range(S):
                mat2[c][S - r - 1] = mat[r][c]
        yield mat2
        mat = deepcopy(mat2)


def flip(r, c, s):
    mat = copy(r, c, s)
    i = 0
    j = s - 1
    while i < j:
        for rr in range(s):
            mat[rr][i], mat[rr][j] = mat[rr][j], mat[rr][i]
        i += 1
        j -= 1

    return mat


def show(mat):
    for row in mat:
        print("".join(row))
    print("=" * 10)


for i in range(5):
    R, C = len(pic), len(pic[0])
    assert R == C, f"{R}, {C}"

    S = 2 if R % 2 == 0 else 3

    squares = []

    def add(r, c):
        for mat in [copy(r, c, S), flip(r, c, S)]:
            for m in rotate(mat):
                if value := rules.get(linear(m), None):
                    squares.append(square(value))
                    return

        assert False, "No rule found"

    for r in range(0, R, S):
        for c in range(0, C, S):
            add(r, c)

    # convert square back to pic
    pic = []
    R = len(squares[0])
    n = int(math.sqrt(len(squares)))
    for chunk in chunked(squares, n):
        for r in range(R):
            row = []
            for ch in chunk:
                for c in range(R):
                    row.append(ch[r][c])
            pic.append(row)

print(sum(row.count("#") for row in pic))
