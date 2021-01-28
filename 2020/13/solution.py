lines = [line.strip() for line in open('input').readlines()]

timestamp = int(lines[0])
times = lines[1].split(',')
def part1(times):
    times = times.copy()
    times = [int(time) for time in times if time != 'x']
    times.sort()

    wait = []
    for time in times:
        quo, rem = divmod(timestamp, time)
        if rem == 0:
            assert False
        wait.append((time * (quo + 1) - timestamp, time))


    wait.sort()
    x, y = wait[0]
    print(x * y)

part1(times)

# part2
# get remainders first
d = {}
for idx, time in enumerate(times):
    if time == 'x':
        continue
    d[int(time)] = idx


for key, value in d.items():
    d[key] = -1 * (value % key)


# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
def euclid(n1, n2):
    a, b = n1, n2
    u, v = 1, 0
    x, y = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a - b * q
        cx, cy = x, y
        x, y = u - q * x, v - q * y
        u, v = cx, cy

    assert a == 1
    return u, v
	

def crt2(p1, p2):
    n1, a1 = p1
    n2, a2 = p2
    m1, m2 = euclid(n1, n2)

    x = (a2 * m1 * n1 + a1 * m2 * n2) % (n1 * n2)
    return n1 * n2, x

def crt(items):
    assert len(items) >= 2
    x = crt2(items[0], items[1])
    for item in items[2:]:
        x = crt2(x, item)

    return x[1]

items = list(d.items())
print(crt(items))
