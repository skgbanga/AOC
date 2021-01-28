lines = [line.strip() for line in open('input').readlines()]
R = 6
C = 25

pixels = [int(x) for x in lines[0]]
layers = []
idx = 0
while idx < len(pixels):
    layer = []
    for _ in range(R):
        row = pixels[idx: idx + C]
        layer.append(row)
        idx += C
    layers.append(layer)

from collections import Counter
def key(layer):
    c = Counter()
    for row in layer:
        c.update(row)
    return c[0]

layer = min(layers, key=key)

c = Counter()
for row in layer:
    c.update(row)
print(c[1] * c[2])

img = [[None] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        for layer in layers:
            if layer[r][c] != 2:
                img[r][c] = layer[r][c]
                break
        assert img[r][c] is not None


for row in img:
    print(''.join(' ' if x == 0 else '1' for x in row))
