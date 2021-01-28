lines = [line.strip() for line in open('input').readlines()]

area = 0
ribbon = 0
for line in lines:
    l, w, h = [int(t) for t in line.split('x')]
    areas = [l*w, w*h, h*l]
    area += 2 * sum(areas) + min(areas)

    sides = [l, w, h]
    sides.sort()
    a, b = sides[:2]
    ribbon += 2 * (a + b) + l * w * h

print(area)
print(ribbon)
