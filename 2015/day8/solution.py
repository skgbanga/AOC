full = [line.strip('\n') for line in open('input', 'r').readlines()]
real = [line.strip()[1:-1] for line in open('input', 'r', encoding='unicode_escape').readlines()]

# part1
b = sum(len(line) for line in full)
c = sum(len(line) for line in real)
print(b, c, b - c)


# another way to do part1
# which we might do in languages like C++
with open('input', 'rb') as f:
    data = f.read()

lines = []
idx = 0
line = []
while idx < len(data):
    c = data[idx]
    if c == ord('"'):   # if c == b'\"' does not work since c is an integer
        idx += 1
        continue

    if c == ord('\n'):
        lines.append(''.join(line))
        line = []
        idx += 1
        continue

    if c != ord('\\'):
        line.append(chr(c))
        idx += 1
    else:
        # we are in escape world now
        idx += 1
        c = data[idx]
        if c == ord('\\') or c == ord('\"'):
            line.append(chr(c))
            idx += 1
        elif c == ord('x'):
            idx += 1
            num = int(data[idx:][:2], 16)
            idx += 2
            line.append(chr(num))
        else:
            assert False, f"Got a weird character after escape {c}"


assert not line
c = sum(len(line) for line in lines)
print(b, c, b - c)

# part2
new = []
for r in full:
    x = ""
    for c in r:
        if c == '\"':
            x += '\\\"'
        elif c == "\\":
            x += "\\\\"
        else:
            x += c
    new.append(x)


s = sum(len(line) for line in new) + len(new) * 2
print(s, b, s - b)
