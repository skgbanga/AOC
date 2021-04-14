N = 3017957

elves = [1] * N

def part1():
    i = 0
    while True:
        while elves[i] == 0:
            i = (i + 1) % N

        j = (i + 1) % N
        while elves[j % N] == 0:
            j = (j + 1) % N

        if j == i:
            break

        elves[i] += elves[j]
        elves[j] = 0
        i = (j + 1) % N

    print(i + 1)


def part2():
    elves = [(i, 1) for i in range(N)]
    while len(elves) != 1:
        L = len(elves)
        i = 0
        j = L // 2
        jinc = 1 if L % 2 == 0 else 2
        while j < L:
            elves[i] = (elves[i][0], elves[i][1] + elves[j][1])
            elves[j] = (elves[j][0], 0)
            i += 1
            j += jinc
            jinc = 1 if jinc == 2 else 2

        elves = elves[i:] + elves[:i]
        elves = [(a, b) for a, b in elves if b != 0]

    return elves[0][0] + 1


ans = part2()
print(ans)
