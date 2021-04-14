import re

lines = [line.strip() for line in open('input').readlines()]
pairs = []
for line in lines:
    a, b = map(int, re.findall('\d+', line))
    pairs.append((a, b))

# merge
pairs.sort(key=lambda x:x[0])
intervals = []
ca, cb = pairs[0]
for start, end in pairs[1:]:
    if start <= cb + 1:
        cb = max(cb, end)
    else:
        intervals.append((ca, cb))
        ca, cb = start, end

intervals.append((ca, cb))
print(intervals[0][1] + 1)

total = 4294967296
for a, b in intervals:
    total -= (b - a + 1)
print(total)
