x1 = 0
x2 = 10
v1 = 0
v2 = 0


state = set()
counter = 0
while True:
    if (x1, x2, v1, v2) in state:
        print('counter', counter)
        print(x1, x2, v1, v2)
        break
    counter += 1
    state.add((x1, x2, v1, v2))


    a1 = 0
    a2 = 0
    if x1 < x2:
        a1 = +1
        a2 = -1
    elif x2 < x1:
        a1 = -1
        a2 = +1
    v1 += a1
    v2 += a2

    x1 += v1
    x2 += v2
    print(x1, x2, v1, v2)
