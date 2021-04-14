from collections import deque

import sys
import hashlib

# salt = 'abc'
salt = 'qzyelonm'

found = []

choices = deque()

def newhash(s):
    h = s
    for _ in range(2017):
        h = hashlib.md5(h.encode()).hexdigest()
    return h

m = 0
idx = 0
while len(found) < 64 or choices:
    while choices:
        prev, *_ = choices[0]
        if idx - prev <= 1000:
            break
        choices.popleft()
    m = max(m, len(choices))

    h = newhash(salt + str(idx))
    for c in choices:
        if c[3] and c[1] * 5 in h:
            found.append((c[0], c[1], idx, h))
            c[3] = False

    if len(found) < 64:
        for a, b, c in zip(h, h[1:], h[2:]):
            if a == b == c:
                choices.append([idx, a, h, True])
                break

    idx += 1
    if idx % 10_000 == 0:
        print(idx, len(found))

print('max length of choices is ', m)
found.sort(key=lambda x: x[0])
print(found[63])
