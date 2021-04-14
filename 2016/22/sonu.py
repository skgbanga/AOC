def calcstates(state):
    global xmax, ymax, setlargelocs, booldone
    (xd, yd), (xe, ye) = state

    sstates = set()
    for nx, ny in zip((xe + 1, xe - 1, xe, xe), (ye, ye, ye - 1, ye + 1)):
        if ((nx, ny) not in setlargelocs) and (nx >=0) and (ny >= 0) and (nx <= xmax) and (ny <= ymax):
            if (nx, ny) == (xd, yd):
                sstates.add(((xe, ye), (nx, ny)))
                if (xe, ye) == (0, 0):
                    booldone = True
            else:
                sstates.add(((xd, yd), (nx, ny)))
    
    return sstates

with open('input', 'r') as f:
    lines = [s.split() for s in f.read().strip().splitlines()][2:]
    
ddata = {}
for a, _, b, c, _ in lines:
    _, x, y = a.split('-')
    x, y = map(lambda n: int(n[1:]), (x, y))
    b, c = map(lambda n: int(n[:-1]), (b, c))
    ddata.setdefault((x, y), (b, c))

xmax, _ = max(ddata.keys(), key = lambda x: x[0])
_, ymax = max(ddata.keys(), key = lambda x: x[1])

print(xmax, ymax)

datatomove, _ = ddata[(xmax, 0)]
print(datatomove)
for (x, y), (usage, avail) in ddata.items():
    if avail >= datatomove:
        availthreshold = avail
        emptyloc = (x, y)
        break

print(availthreshold)
print(x, y)

setlargelocs = set()
for (x, y), (usage, avail) in ddata.items():
    if usage > availthreshold:
        setlargelocs.add((x, y))

print(len(setlargelocs))

# A state is defined as ((xd, yd), (xe, ye)),
# where (xd, yd) is location of data to be moved,
# and (xe, ye) is the empty location
states = set()
states.add(((xmax, 0), emptyloc))
steps = 0
booldone = False
seen = set()
while not booldone:
    nextstates = set()
    for state in states:
        if state not in seen:
            seen.add(state)
            nextstates.update(calcstates(state))

    steps += 1
    states = nextstates.copy()

print(steps)
