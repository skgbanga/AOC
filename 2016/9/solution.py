import re
lines = [line.strip() for line in open('input').readlines()]
assert len(lines) == 1
line = lines[0]


def recurse(msg):
    n = 0
    idx = 0
    while idx < len(msg):
        ch = msg[idx]
        if ch == '(':
            end = msg.index(')', idx)
            a, b = map(int, re.findall('\d+', msg[idx + 1:end + 1]))
            n += b * recurse(msg[end + 1: end + 1 + a])
            # msg += line[end + 1: end + 1 + a] * b
            idx = end + 1 + a
        else:
            n += 1
            idx += 1
    return n


print(recurse(line))
