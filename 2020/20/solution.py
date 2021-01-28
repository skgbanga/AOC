import math
lines = [line.strip() for line in open('sample').readlines()]

tiles = {}
num = 0
grid = []
for line in lines:
    if not line:
        tiles[num] = grid
        num = 0
        grid = []
        continue

    if line.startswith('Tile'):
        num = int(line.split()[-1][:-1])
    else:
        row = []
        for c in line:
            if c == '#':
                row.append(1)
            else:
                c == '.'
                row.append(0)
        grid.append(row)

tiles[num] = grid

def count(block):
    x = 0
    for row in block:
        for c in row:
            x += (c == 1)
    return x


def show_block(block):
    for row in block:
        for c in row:
            print(c, end='')
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

    start = 0
    for s in range(S, 0, -2):
        rotate_frame(start, s)
        start += 1

    # assert count(old) == count(new), f'{count(old)} != {count(new)}'
    return new


def flip_vertical(old):
    S = len(old)
    new = [[0] * S for _ in range(S)]
    for c in range(S):
        o = S - c - 1
        for r in range(S):
            new[r][o] = old[r][c]
    assert count(old) == count(new)
    return new

# def flip_horizontal(old):
#     S = len(old)
#     new = [[0] * S for _ in range(S)]
#     for r in range(S):
#         o = S - r - 1
#         for c in range(S):
#             new[o][c] = old[r][c]
#     assert count(old) == count(new)
#     return new

def col(tile, d):
    return [row[d] for row in tile]

def edges(tile):
    return tile[0], col(tile, -1), tile[-1][::-1], col(tile, 0)[::-1]

def handle(num, tile):
    dirs = {}
    for n, candidate in tiles.items():
        if n == num:
            continue
        for idx, edge in enumerate(edges(tile)):
            for c in edges(candidate):
                if edge == c or edge == c[::-1]:
                    dirs[idx] = n
    return dirs

neighbors = {}
for num, tile in tiles.items():
    neighbors[num] = handle(num, tile)


# for k, v in neighbors.items():
#     print(k, len(v), v)


# find top left corner
for k, v in neighbors.items():
    if len(v) == 2 and 1 in v and 2 in v:
        start = k

# print(start)

def adjust(side, tedge, neighbor):
    tile = tiles[neighbor]
    if side == 1:
        target = 3
    elif side == 2:
        target = 0
    else:
        assert False


    def rots(idx):
        nonlocal tile
        cnt = 0
        while idx != target:
            cnt += 1
            tile = rotate(tile)
            idx = (idx + 1) % 4

        # we did cnt rotations, move neighbors by that much amount
        d = {}
        for k, v in neighbors[neighbor].items():
            d[(k + cnt) % 4] = v
        neighbors[neighbor] = d


    for idx, edge in enumerate(edges(tile)):
        if tedge == edge:
            tile = flip_vertical(tile)
            n1 = neighbors[neighbor].get(1, None)
            n3 = neighbors[neighbor].get(3, None)
            if n1:
                neighbors[neighbor][3] = n1
            if n3:
                neighbors[neighbor][1] = n3

            if idx == 1:
                idx = 3
            elif idx == 3:
                idx = 1
            
            rots(idx)
            return tile
        elif tedge == edge[::-1]:
            rots(idx)
            return tile

    assert False

dim = int(math.sqrt(len(tiles)))
board = [[(0, 0)] * dim for _ in range(dim)]
board[0][0] = (start, tiles[start])


def show():
    print('=' * 40)
    for r in range(dim):
        for c in range(dim):
            print(board[r][c][0], end=' ')
        print()

for r in range(dim):
    for c in range(dim):
        if r == 0 and c == 0:
            continue # already handled
        if c == 0:
            # look above
            upper_num, upper_grid = board[r - 1][c]
            upper_edges = edges(upper_grid)
            tile = adjust(2, upper_edges[2], neighbors[upper_num][2])
            board[r][c] = (neighbors[upper_num][2], tile)
        else:
            # look left
            left_num, left_grid = board[r][c - 1]
            left_edges = edges(left_grid)
            tile = adjust(1, left_edges[1], neighbors[left_num][1])
            board[r][c] = (neighbors[left_num][1], tile)


show()

tile_dim = len(board[0][0][1])
final_dim = (tile_dim - 2) * dim
print("dim: ", dim)
print("tile dim: ", tile_dim)
print("final dim: ", final_dim)

M = [[0] * final_dim for _ in range(final_dim)]

x, y = 0, 0
for r in range(dim):
    for c in range(dim):
        x = r * (tile_dim - 2)
        y = c * (tile_dim - 2)
        block = board[r][c][1]
        for sr in range(1, tile_dim - 1):
            for sc in range(1, tile_dim - 1):
                M[x + sr - 1][y + sc - 1] = block[sr][sc]



xs = 0
for r in range(final_dim):
    for c in range(final_dim):
        xs += (M[r][c] == 1)
print("Total 1's", xs)


monster = []
with open('monster', 'r') as f:
    for line in f:
        line = line[:-1]
        row = []
        for c in line:
            if c == ' ':
                row.append(2)
            else:
                assert c == '#'
                row.append(1)
        monster.append(row)


def match(x, y, P):
    for r in range(len(monster)):
        for c in range(len(monster[0])):
            if monster[r][c] == 1 and P[x + r][y + c] != 1:
                return False

    return True


for _ in range(4):
    M = rotate(M)
    m = 0
    for r in range(final_dim - len(monster)):
        for c in range(final_dim - len(monster[0])):
            m += match(r, c, M)

    if m != 0:
        print("Monsters found ==", m)

# flip
M = flip_vertical(M)
for _ in range(4):
    M = rotate(M)
    m = 0
    for r in range(final_dim - len(monster)):
        for c in range(final_dim - len(monster[0])):
            m += match(r, c, M)

    if m != 0:
        print("Monsters found ==", m)
