import sys
import re

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
pos = []
for line in lines:
    nums = [int(x) for x in re.findall('[-]*\d+', line)]
    pos.append(nums)

N = len(pos)

vel = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
]

def energy():
    e = 0
    for i in range(N):
        pot = sum(abs(pos[i][idx]) for idx in range(3))
        kin = sum(abs(vel[i][idx]) for idx in range(3))
        e += pot * kin
    return e

state = set()
counter = 0
while True:
    col = []
    for p, v in zip(pos, vel):
        col.extend(p)
        col.extend(v)
    t = tuple(col)
    if t in state:
        print('Ans is ', counter)
        break

    state.add(t)
    counter += 1
    # apply gravity
    for i in range(N):
        for j in range(i + 1, N):
            a = pos[i]
            b = pos[j]
            for idx in range(3):
                ai = 0
                bi = 0
                if a[idx] < b[idx]:
                    ai = +1
                    bi = -1
                elif a[idx] > b[idx]:
                    ai = -1
                    bi = +1
                vel[i][idx] += ai
                vel[j][idx] += bi

    # apply velocity
    for i in range(N):
        for idx in range(3):
            pos[i][idx] += vel[i][idx]


    # for p, v in zip(pos, vel):
    #     print(p, v)
    # print()

    if counter % 10_000 == 0:
        print(counter)


# print(energy())
