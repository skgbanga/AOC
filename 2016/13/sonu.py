# return 1 if open space (even 1s), 0 if a wall (odd 1s)
def isopen(x, y):
    global d, input
    if x < 0 or y < 0:
        return 0
    n = x*x + 3*x + 2*x*y + y + y*y + input
    return 1 - (f'{n:b}'.count('1') % 2)


# return a set of all possible previous states for the current state (cx, cy)
def prevstates(cx, cy):
    global d
    pstates = []
    for x, y in zip([cx, cx, cx - 1, cx + 1], [cy - 1, cy + 1, cy, cy]):
        if d.setdefault((x, y), isopen(x, y)):
            pstates.append((x, y))

    return set(pstates)

input = 1350
#input = 10

# a state is stored as (x, y)
sinit, sfinal = (1, 1), (31, 39)
#sinit, sfinal = (1, 1), (7, 4)

d = {}
setstates = set([sinit])
steps = 0

while steps < 1:
    setpstates = set()
    for state in setstates:
        setpstates.update(prevstates(*state))
    steps += 1
    setstates.update(setpstates)
    print(steps, len(setstates), setstates)
    
print(steps)
