def knots(s):
    lens = [ord(ch) for ch in s]
    lens.extend([17, 31, 73, 47, 23])

    N = 256
    ROUNDS = 64
    nums = list(range(N))

    def idx(n):
        return n % N

    skip = 0
    current = 0
    for _ in range(ROUNDS):
        for l in lens:
            i = current
            j = current + l - 1
            while i < j:
                nums[idx(i)], nums[idx(j)] = nums[idx(j)], nums[idx(i)]
                i += 1
                j -= 1
            current += l + skip
            skip += 1

    from more_itertools import chunked

    s = ""
    for chunk in chunked(nums, 16):
        ch = chunk[0]
        for c in chunk[1:]:
            ch = ch ^ c
        s += f"{ch:02x}"

    return s


start = "uugsqrei"
hashes = []
for i in range(128):
    s = start + "-" + str(i)
    hashes.append(knots(s))


def hextobin(ch):
    n = ord(ch) - 97 + 10 if ch in "abcdef" else ord(ch) - 48
    return f"{n:04b}"


board = []
for h in hashes:
    line = "".join(hextobin(ch) for ch in h)
    board.append(line)


from collections import deque


R = 128
C = 128

g = 0
seen = set()
for r in range(R):
    for c in range(C):
        if (r, c) in seen or board[r][c] == "0":
            continue

        assert board[r][c] == "1"
        d = deque([(r, c)])
        seen.add((r, c))
        while d:
            dr, dc = d.popleft()
            for rr, cc in [(dr + 1, dc), (dr - 1, dc), (dr, dc + 1), (dr, dc - 1)]:
                if 0 <= rr < R and 0 <= cc < C and (rr, cc) not in seen:
                    if board[rr][cc] == "1":
                        d.append((rr, cc))
                        seen.add((rr, cc))

        g += 1

print(g)
