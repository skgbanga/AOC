from collections import *

lines = [line.strip() for line in open('input').readlines()]

nice = 0
for line in lines:
    c = Counter(line)
    cons = any(x == y for x, y in zip(line, line[1:]))
    vowels = sum(c[a] for a in 'aeiou') >= 3
    barr = any(s in line for s in ('ab', 'cd', 'pq', 'xy'))

    if cons and vowels and not barr:
        nice += 1

print(nice)


nice = 0
for line in lines:
    d = {}
    a = False
    for idx, _ in enumerate(line[:-1]):
        ss = line[idx:][:2]
        if ss not in d:
            d[ss] = (idx, idx + 1)
        else:
            s, e = d[ss]
            if idx > e:
                a = True
                break

    def check(ss):
        x, _, y = ss
        return x == y

    b = any(check(line[idx:][:3]) for idx, _ in enumerate(line[:-2]))

    if a and b:
        nice += 1

print(nice)
