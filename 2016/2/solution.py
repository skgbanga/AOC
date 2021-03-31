lines = [line.strip() for line in open('input').readlines()]

board = [
      [1],
   [2, 3, 4],
[5, 6, 7, 8, 9],
 ['A','B','C'],
     ['D']
]

def dist(r, c):
    return abs(r - 2) + abs(c - 2)

def col(r, c):
    return c - abs(r - 2)

code = []
r, c = 2, 0
for line in lines:
    for ch in line:
        pr, pc = r, c
        if ch == 'L':
            c -= 1
        elif ch == 'R':
            c += 1
        elif ch == 'U':
            r -= 1
        else:
            r += 1

        if dist(r, c) > 2:
            r, c = pr, pc

    code.append(board[r][col(r, c)])

print(''.join(str(s) for s in code))
