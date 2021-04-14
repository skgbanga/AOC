seed = 1350

def open_space(x, y):
    z = x*x + 3*x + 2*x*y + y + y*y
    z += seed
    b = bin(z)[2:]
    return b.count('1') % 2 == 0


def move():
    from collections import deque
    r, c = 1, 1
    d = deque([(r, c)])
    seen = set([(r, c)])

    cnt = 0
    while d:
        cnt += 1
        n = len(d)
        for _ in range(n):
            r, c = d.popleft()
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if rr == 31 and cc == 39:
                    print('Reached ', cnt)
                    return

                if rr >= 0 and cc >= 0:
                    if (rr, cc) not in seen and open_space(rr, cc):
                        d.append((rr, cc))
                        seen.add((rr, cc))

        print(cnt, len(seen))
        if cnt == 50:
            return

move()
