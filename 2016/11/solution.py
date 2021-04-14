from collections import namedtuple
from copy import deepcopy
from itertools import combinations

floors = 4
pairs = 5

class Floor:
    def __init__(self, gens, chips):
        self.gens = gens
        self.chips = chips

    def __hash__(self):
        return hash((tuple(sorted(self.gens)), tuple(sorted(self.chips))))

    def __eq__(self, other):
        return self.gens == other.gens and self.chips == other.chips

class Building:
    def __init__(self):
        self.floors = [Floor(set(), set()) for _ in range(floors)]
        self.prev = None

    def __hash__(self):
        return hash(tuple(self.floors))

    def __eq__(self, other):
        return self.floors == other.floors

def valid_floor(floor):
    for chip in floor.chips:
        if chip in floor.gens:
            continue
        if len(floor.gens) != 0:  # there should not be any generator
            return False

    return True

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
    if len(floor.gens) >= 2:
        for i, j in combinations(floor.gens, 2):
            c = Change()
            c.gens.extend([i, j])
            yield c

    # pick one gen
    if floor.gens:
        for i in floor.gens:
            c = Change()
            c.gens.append(i)
            yield c

    # pick two chips
    if len(floor.chips) >= 2:
        for i, j in combinations(floor.chips, 2):
            c = Change()
            c.chips.extend([i, j])
            yield c

    # pick one chip
    if floor.chips:
        for i in floor.chips:
            c = Change()
            c.chips.append(i)
            yield c

    # pick one chip and one gen
    if floor.gens and floor.chips:
        for gen in floor.gens:
            for chip in floor.chips:
                if gen != chip:
                    continue

                c = Change()
                c.gens.append(gen)
                c.chips.append(chip)
                yield c

def end(building):
    top = building.floors[-1]
    return len(top.gens) == pairs and len(top.chips) == pairs

def valid_building(building):
    return all(valid_floor(floor) for floor in building.floors)

def apply(current, change):
    # new = deepcopy(current)

    new = Building()
    new.prev = (change.fro, current)
    for floor in range(floors):
        new.floors[floor].gens.update(current.floors[floor].gens)
        new.floors[floor].chips.update(current.floors[floor].chips)

    for gen in change.gens:
        new.floors[change.fro].gens.remove(gen)
        new.floors[change.to].gens.add(gen)

    for chip in change.chips:
        new.floors[change.fro].chips.remove(chip)
        new.floors[change.to].chips.add(chip)

    return new


def pgen(g):
    return chr(ord('A') + g)

def pchip(c):
    return chr(ord('a') + c)

def print_building(level, building):
    for idx, floor in enumerate(reversed(building.floors)):
        prefix = '*' if idx == floors - level - 1 else ' '
        pg = ''
        for g in range(pairs):
            ch = pgen(g) if g in floor.gens else ' '
            pg += ch

        pc = ''
        for c in range(pairs):
            ch = pchip(c) if c in floor.chips else ' '
            pc += ch

        print(prefix, pg, pc)
    print('===')

def print_chain(level, building):
    chain = []
    while True:
        chain.append((level, building))
        if not building.prev:
            break

        level, building = building.prev

    for idx, (level, building) in enumerate(reversed(chain), start=1):
        print(idx)
        print_building(level, building)

def move():
    # 0 promethium
    # 1 cobalt
    # 2 curium
    # 3 ruthenium
    # 4 plutonium
    building = Building()
    building.floors[0] = Floor(set([0]), set([0]))
    building.floors[1] = Floor(set([1, 2, 3, 4]), set())
    building.floors[2] = Floor(set(), set([1, 2, 3, 4]))
    building.floors[3] = Floor(set(), set())

    # building = Building()
    # building.floors[0] = Floor(set([]), set([0, 1]))
    # building.floors[1] = Floor(set([0]), set())
    # building.floors[2] = Floor(set([1]), set())
    # building.floors[3] = Floor(set(), set())

    # building = Building()
    # building.floors[0] = Floor(set([0, 1, 2]), set([0, 1, 2]))
    # building.floors[1] = Floor(set([3, 4, 5, 6]), set())
    # building.floors[2] = Floor(set(), set([3, 4, 5, 6]))
    # building.floors[3] = Floor(set(), set())

    from collections import deque
    d = deque()
    seen = set()
    d.append((0, building))
    seen.add((0, building))

    cnt = 0
    while d:
        l = len(d)
        for _ in range(l):
            level, building = d.popleft()
            # print_building(level, building)

            if end(building):
                print_chain(level, building)
                return cnt

            floor = building.floors[level]
            choices = list(possible(floor))
            for p in choices:
                p.fro = level
                if level != floors - 1:  # go up
                    p.to = level + 1
                    new = apply(building, p)
                    if valid_building(new) and (p.to, new) not in seen:
                        d.append((p.to, new))
                        seen.add((p.to, new))

                if level != 0:  # go down
                    p.to = level - 1
                    new = apply(building, p)
                    if valid_building(new) and (p.to, new) not in seen:
                        d.append((p.to, new))
                        seen.add((p.to, new))

        cnt += 1
        print('=' * 20, cnt, len(d), '=' * 20)

    return -1

moves = move()
print(moves)
