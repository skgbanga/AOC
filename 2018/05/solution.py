import string

lines = [line.strip() for line in open("input").readlines()]


def solve(line):
    s = []
    for ch in line:
        if s and s[-1].swapcase() == ch:
            s.pop()
        else:
            s.append(ch)

    return len(s)


m = float("inf")
line = lines[0]
for ch in string.ascii_lowercase:
    data = [c for c in line if c not in (ch, ch.upper())]
    m = min(m, solve(data))

print(m)
