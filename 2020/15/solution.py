from collections import deque

# solution 1
nums = [14,3,1,0,9,5]

seen = {}

def update(last, turn):
    if last in seen:
        cnt, xs = seen[last]
        xs.append(turn)
        seen[last] = (cnt + 1, xs)
    else:
        d = deque(maxlen=2)
        d.append(turn)
        seen[last] = (1, d)

for turn, last in enumerate(nums, start=1):
    update(last, turn)


while turn < 2020:
    turn += 1
    cnt, when = seen[last]
    if cnt == 1:
        last = 0
        update(last, turn)
    else:
        last = when[1] - when[0]
        update(last, turn)


print(last)


# solution 2
nums = [14, 3, 1, 0, 9, 5]

seen = {}
for idx, num in enumerate(nums, start=1):
    seen[num] = idx

n = 0
for idx in range(idx + 1, 2020):
    c = n
    if n in seen:
        n = idx - seen[n]
    else:
        n = 0

    seen[c] = idx

print(n)
