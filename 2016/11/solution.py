from copy import deepcopy

floors = 4
n = 5

class Floor:
    def __init__(self, n):
        self.gens  = [0] * n
        self.chips = [0] * n

    def valid(self):
        for i, chip in enumerate(self.chips):
            if not chip:
                continue

            if self.gens[i]:
                continue

            # we have a chip on this floor which doesn't have a generator
            # on the same floor. make sure there is no other generator
            if sum(self.gens) != 0:
                return False

        return True

    def __eq__(self, other):
        return self.gens == other.gens and self.chips == other.chips

class Change:
    def __init__(self):
        self.gens = []
        self.chips = []
        self.fro = -1
        self.to = -1

    def __str__(self):
        return f'From: {self.fro}, To: {self.to}, gen: {self.gens}, chips: {self.chips}'


def possible(floor):
    # pick two gens
    if sum(floor.gens) >= 2:
        for i in range(n):
            if not floor.gens[i]:
                continue
            for j in range(i + 1, n):
                c = Change()
                c.gens.extend([i, j])
                yield c

    # pick one gen
    if sum(floor.gens):
        for i in range(n):
            if not floor.gens[i]:
                continue
            c = Change()
            c.gens.append(i)
            yield c

    # pick two chips
    if sum(floor.chips) >= 2:
        for i in range(n):
            if not floor.chips[i]:
                continue
            for j in range(i + 1, n):
                c = Change()
                c.chips.extend([i, j])
                yield c

    # pick one chip
    if sum(floor.chips):
        for i in range(n):
            if not floor.chips[i]:
                continue
            c = Change()
            c.chips.append(i)
            yield c

    # pick one chip and one gen
    if sum(floor.gens) and sum(floor.chips):
        for i, gen in enumerate(floor.gens):
            for j, chip in enumerate(floor.chips):
                if gen and chip:
                    c = Change()
                    c.gens.append(i)
                    c.chips.append(j)
                    yield c


def end(building):
    top = building[-1]
    return sum(top.gens) == n and sum(top.chips) == n


def valid(state):
    return all(floor.valid() for floor in state)

def apply(current, change):
    new = deepcopy(current)
    for gen in change.gens:
        new[change.fro].gens[gen] = 0
        new[change.to].gens[gen] = 1

    for chip in change.chips:
        new[change.fro].chips[chip] = 0
        new[change.to].chips[chip] = 1

    return new


def print_building(level, building):
    for idx, floor in enumerate(reversed(building)):
        prefix = '*' if idx == floors - level - 1 else ' '
        print(prefix, floor.gens, floor.chips)
    print('===')

def move():
    building = [Floor(n) for _ in range(floors)]

    # 0 promethium
    # 1 cobalt
    # 2 curium
    # 3 ruthenium
    # 4 plutonium
    building[0].chips[0] = 1
    building[0].gens[0] = 1

    building[1].gens[1] = 1
    building[1].gens[2] = 1
    building[1].gens[3] = 1
    building[1].gens[4] = 1

    building[2].chips[1] = 1
    building[2].chips[2] = 1
    building[2].chips[3] = 1
    building[2].chips[4] = 1

    from collections import deque
    d = deque()
    seen = []
    d.append((0, building))
    seen.append((0, building))

    cnt = 0
    while d:
        l = len(d)
        for _ in range(l):
            level, building = d.popleft()
            print_building(level, building)

            if sum(building[-1].gens) == n and sum(building[-1].chips) == n:
                return cnt

            floor = building[level]
            choices = list(possible(floor))
            print("Choices ", len(choices))
            for p in choices:
                p.fro = level
                if level != floors - 1:  # go up
                    p.to = level + 1
                    new = apply(building, p)
                    if valid(new) and (p.to, new) not in seen:
                        d.append((p.to, new))
                        seen.append((p.to, new))

                if level != 0:  # go down
                    p.to = level - 1
                    new = apply(building, p)
                    if valid(new) and (p.to, new) not in seen:
                        d.append((p.to, new))
                        seen.append((p.to, new))

        cnt += 1
        print(cnt, len(d))

    return -1

moves = move()
print(moves)
