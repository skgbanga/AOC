from collections import Counter

lines = [line.strip() for line in open('input').readlines()]


d = []
for line in lines:
    tokens = line.split()
    d.append((tokens[0], int(tokens[3]), int(tokens[6]), int(tokens[-2])))

race = []
for item in d:
    name, speed, duration, sleep = item

    t = 0
    a = 0
    while t < 2503:
        dur = min(duration, 2503 - t)
        a += speed * dur
        t += dur

        dur = min(sleep, 2503 - t)
        t += dur
    race.append((name, a))


print(max((distance, name) for name, distance in race))


race = {}
for item in d:
    name, speed, duration, sleep = item
    ds = []
    t = 0
    a = 0
    while t < 2503:
        dur = min(duration, 2503 - t)
        for _ in range(dur):
            a += speed
            t += 1
            ds.append(a)

        dur = min(sleep, 2503 - t)
        for _ in range(dur):
            t += 1
            ds.append(a)

    race[name] = ds

c = Counter()
for i in range(2503):
    m = max(value[i] for value in race.values())
    for key, value in race.items():
        if value[i] == m:
            c[key] += 1

print(c.most_common(1))
