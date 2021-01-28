from collections import Counter
from itertools import product
import pickle


lines = [line.strip() for line in open('input').readlines()]

rules = {}
msgs = []
start = False
for line in lines:
    if not line:
        start = True
        continue

    if start:
        msgs.append(line)
    else:
        a, b = [token.strip() for token in line.split(':')]
        rules[int(a)] = b

for msg in msgs:
    c = Counter(msg)
    assert len(c) == 2, c
    assert 'a' in c
    assert 'b' in c


d = {}
while True:
    updated = False
    for rule, value in rules.items():
        if rule in d:
            continue
        value = value.strip('"')
        if value in ('a', 'b'):
            updated = True
            d.setdefault(rule, set()).add(value)
            continue
        nums = []
        for mr in value.split('|'):
            nums.extend(int(num) for num in mr.split())
        if all(n in d for n in nums):
            updated = True
            s = set()
            for mr in value.split('|'):
                ds = [d[int(num)] for num in mr.split()]
                s.update(''.join(i) for i in product(*ds))
            d[rule] = s
    if not updated:
        break

m = {}
x = 0
for msg in msgs:
    found = False
    for num, choices in d.items():
        if msg in choices:
            x += 1
            found = True
            if num in (0, 42, 31, 8, 11):
                m.setdefault(num, []).append(msg)
    if not found:
        m.setdefault(-1, []).append(msg)

print(len(m[0]))
def count(msg, n):
    m = 0
    while True:
        found = False
        for c in d[n]:
            if msg.startswith(c):
                msg = msg[len(c):]
                found = True
                m += 1
                break

        if not found:
            break

    return m, msg

def solve(msg):
    m, msg = count(msg, 42)
    n, msg = count(msg, 31)

    if msg:
        return False, 0, 0
    else:
        return True, m, n

extra = 0
unmatched = m[-1]
for msg in unmatched:
    result, m, n = solve(msg)
    if result and n > 0 and m > n:
        extra += 1
print(extra)
