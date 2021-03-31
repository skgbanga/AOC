import re
lines = [line.strip() for line in open('input').readlines()]

R = 6
C = 50
board = [[0] * C for _ in range(R)]

for line in lines:
    a, b = list(map(int, re.findall('\d+', line)))
    if line.startswith('rect'):
        for r in range(b):
            for c in range(a):
                board[r][c] = 1
    elif line.startswith('rotate row'):
        board[a][:] = board[a][-b:] + board[a][:-b]
    elif line.startswith('rotate column'):
        col = [board[r][a] for r in range(R)]
        col = col[-b:] + col[:-b]
        for r in range(R):
            board[r][a] = col[r]
    else:
        assert False

def show():
    for r in range(R):
        for c in range(C):
            ch = '.' if board[r][c] == 1 else ' '
            print(ch, end=' ')
        print()


show()
s = sum(sum(row) for row in board)
print(s)
