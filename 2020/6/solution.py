from collections import Counter

answers = []
with open('input', 'r') as f:
    group = []
    for line in f:
        line = line.strip()
        if not line:
            answers.append(group)
            group = []
        else:
            group.append(line)
    if group:
        answers.append(group)


def handle(group):
    s = set()
    for line in group:
        s.update(line)
    return len(s)


def handle2(group):
    c = Counter()
    for line in group:
        c.update(line)

    return sum(value == len(group) for value in c.values())



print(sum(handle(group) for group in answers))
print(sum(handle2(group) for group in answers))
