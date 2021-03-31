lines = [line.strip() for line in open('input').readlines()]
msg = [list(line) for line in lines]
msg = list(zip(*msg))

from collections import Counter
ans = ''
for col in msg:
    c = Counter(col)
    ans += c.most_common()[-1][0]

print(ans)
