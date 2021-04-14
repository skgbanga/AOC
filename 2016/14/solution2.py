from collections import deque

import sys
import hashlib

# salt = 'abc'
salt = 'qzyelonm'

found = []

def newhash(s):
    h = s
    for _ in range(2017):
        h = hashlib.md5(h.encode()).hexdigest()
    return h

# def newhash(s):
#     return hashlib.md5(s.encode()).hexdigest()


d = {}
idx = 0
while len(found) < 64:
    if idx not in d:
        d[idx] = newhash(salt + str(idx))
    h = d[idx]
    for a, b, c in zip(h, h[1:], h[2:]):
        if a == b == c:
            for j in range(idx + 1, idx + 1001):
                if j not in d:
                    d[j] = newhash(salt + str(j))
                hh = d[j]
                if a * 5 in hh:
                    found.append(idx)
            break

    idx += 1

print(len(found))
print(found[63])
