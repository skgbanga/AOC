board = [line[:-1] for line in open('input2').readlines()]

R = len(board)
C = len(board[0])

# NESW = 0123
d = 2
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# find the entrace point to figure out initial r, c
r = 0
line = board[0]
for idx, ch in enumerate(line):
    if ch == '|':
        c = idx
        break

steps = 0
chars = []
while True:
    nr, nc = r + dr[d], c + dc[d]
    if 0 <= nr < R and 0 <= nc < C:
        a = board[nr][nc]
        if a == ' ':
            print("Reached a space. need to exit")
            break
        elif a.isalpha():
            chars.append(a)
        elif a == '+':
            # we are changing the direction
            if d == 2 or d == 0:  # N, S
                d1 = board[nr][nc + 1]
                d2 = board[nr][nc - 1]
                if d1 != ' ':
                    assert d2 == ' '
                    d = 1
                else:
                    assert d2 != ' '
                    d = 3
            else:
                d1 = board[nr + 1][nc]
                d2 = board[nr - 1][nc]
                if d1 != ' ':
                    assert d2 == ' '
                    d = 2
                else:
                    assert d2 != ' '
                    d = 0
    else:
        print("outside board. exiting..")
        break

    r, c = nr, nc
    steps += 1

print("".join(chars), steps)
