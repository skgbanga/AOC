lines = [line.strip() for line in open("input").readlines()]

import re
from copy import deepcopy


def transition(d):
    for k, (current, direction, bound) in d.items():
        if current == 0:
            direction = 1
        elif current == bound - 1:
            direction = -1
        d[k] = (current + direction, direction, bound)


prev = None

def check(delay):
    global prev

    if delay == 0:
        state = {}
        for line in lines:
            a, b = map(int, re.findall("\d+", line))
            state[a] = (0, 1, b)
    else:
        state = prev
        transition(state)

    prev = deepcopy(state)

    pkt = 0
    m = max(state.keys())
    for i in range(m + 1):
        if i in state:
            c, _, b = state[i]
            if c == 0:
                return False

        transition(state)
        pkt += 1

    return True


delay = 0
while True:
    if check(delay):
        break
    delay += 1
    if delay % 1000 == 0:
        print(delay)

print(delay)
