def gen(start, mult):
    while True:
        p = (start * mult) % 2147483647
        yield p
        start = p


cnt = 0
s = 0
g1 = gen(65, 16807)
g2 = gen(8921, 48271)
for a, b in zip(g1, g2):
    if bin(a)[-16:] == bin(b)[-16:]:
        s += 1
    cnt += 1
    if cnt == 40_000_000:
        break

    if cnt % 10_000 == 0:
        print(cnt)

print(s)
