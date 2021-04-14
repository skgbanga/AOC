# A state is stored as ((x1, y1), (x2, y2), (x3, y3), ..., (xa, xb)) 
# (xn, yn) are visited locations with numbers in ascending order, (xa, xb) is a general location that was visited last
# starting state is ((x0, y0), (x0, y0)) where (x0, y0) is the location of digit 0 that is marked as visited

def calcstates(state):
    global swalls, snums, booldone, zeroloc
    *listnumsvisited, (x, y) = state
    snumsvisited = set(listnumsvisited)
    sstates = set()
    for nx, ny in zip((x + 1, x - 1, x, x), (y, y, y - 1, y + 1)):
        if (nx, ny) not in swalls:
            if ((nx, ny) in snums) and ((nx, ny) not in snumsvisited):
                snumsvisited.add((nx, ny))
                nextstate = tuple(sorted(snumsvisited) + [(nx, ny)])
            else:
                nextstate = tuple(listnumsvisited + [(nx, ny)])
            
            if (snumsvisited == snums) and ((nx, ny) == zeroloc):
                booldone = True
            
            sstates.add(nextstate)

    return sstates

with open('/content/drive/My Drive/Colab Notebooks/Advent_of_Code_2016/data_day24.txt', 'r') as f:
    lines = f.read().strip().splitlines()
drive.flush_and_unmount() 
    
swalls = set()
snums = set()
states = set()

for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == '#':
            swalls.add((x, y))
        elif c.isdigit():
            snums.add((x, y))
            if c == '0':
                zeroloc = (x, y)
                states.add((zeroloc, zeroloc))

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
    print(steps, len(states))

print(steps)
