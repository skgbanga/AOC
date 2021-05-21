lines = [line.strip() for line in open("input").readlines()]


ports = []
for line in lines:
    a, b = list(map(int, line.split("/")))
    ports.append((a, b))


n = float("-inf")
m = float("-inf")
state = []
ends = []


def traverse():
    global n
    global m
    for (a, b) in ports:
        if (a, b) not in state and (b, a) not in state:
            if len(state) == 0:
                if a == 0 or b == 0:
                    state.append((a, b))
                    ends.append(a if a != 0 else b)
                    traverse()
            else:
                end = ends[-1]
                if a == end or b == end:
                    state.append((a, b))
                    ends.append(a if a != end else b)
                    traverse()

    if state:
        if len(state) >= n:
            n = len(state)
            s = sum(a + b for a, b in state)
            m = max(m, s)
        state.pop()
        ends.pop()


traverse()
print(m)
