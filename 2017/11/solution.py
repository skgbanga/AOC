line = open("input").read().strip()

m = {
    "n": (0, 1),
    "s": (0, -1),
    "nw": (0.5, 0.5),
    "sw": (0.5, -0.5),
    "ne": (-0.5, 0.5),
    "se": (-0.5, -0.5),
}

x, y = 0, 0

f = 0
for dd in line.split(","):
    dx, dy = m[dd]
    x, y = x + dx, y + dy
    f = max(abs(x) + abs(y), f)

print(f)
