lines = [line.strip() for line in open("input").readlines()]

from collections import Counter

s2 = 0
s3 = 0
for line in lines:
    c = Counter(line)
    s2 += any(v == 2 for v in c.values())
    s3 += any(v == 3 for v in c.values())

print(s2 * s3)


for i, a in enumerate(lines):
    for j, b in enumerate(lines):
        if i == j:
            continue

        d = sum(ch1 != ch2 for ch1, ch2 in zip(a, b))
        if d == 1:
            print(''.join(ch for ch, ch1 in zip(a, b) if ch == ch1))
            exit(1)
