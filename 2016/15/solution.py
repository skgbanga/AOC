import re
lines = [line.strip() for line in open('input').readlines()]

discs = []
for line in lines:
    _, total, _, start = map(int, re.findall('\d+', line))
    discs.append((start, total))


def found(time):
    start, total = discs[0]
    p = (start + time + 1) % total
    for idx, (start, total) in enumerate(discs[1:], start=2):
        if p != (start + time + idx) % total:
            return False
    return True

time = 0
while True:
    if found(time):
        print(time)
        break
    time += 1
