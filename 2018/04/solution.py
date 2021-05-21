lines = [line.strip() for line in open("input").readlines()]

from datetime import datetime

data = []
for line in lines:
    s = line[line.index('[') + 1:line.index(']')]
    data.append((datetime.strptime(s, '%Y-%m-%d %H:%M'), line))

data.sort(key=lambda x : x[0])

from collections import defaultdict
g = defaultdict(list)
id = None
inter = []
for time, line in data:
    if "Guard" in line:
        import re
        id = list(map(int, re.findall("\d+", line)))[-1]
    elif "falls asleep" in line:
        inter.append(time.minute)
    elif "wakes up" in line:
        assert id
        inter.append(time.minute)
        g[id].append(inter)
        inter = []


from collections import Counter

counter = float('-inf')
minute = None
guard = None
for k, v in g.items():
    sleep = Counter()
    for a, b in v:
        for i in range(a, b):
            sleep[i] += 1

    minut, c = sleep.most_common(1)[0]
    if c > counter:
        counter = c
        minute = minut
        guard = k

print(minute * guard)
