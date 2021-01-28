lines = [line.strip() for line in open('input').readlines()]

data = {}
for line in lines:
    tokens = line.split()
    data[tokens[0][:2].lower()] = {
            'c' : int(tokens[2][:-1]),
            'd' : int(tokens[4][:-1]),
            'f' : int(tokens[6][:-1]),
            't' : int(tokens[8][:-1]),
            'calories' : int(tokens[-1])
    }


x = 0

# there's got to be a better way!
for a in range(101):
    for b in range(101 - a):
        for c in range(101 - (a + b)):
            for d in range(101 - (a + b + c)):
                if a + b + c + d == 100:
                    # find flavor value
                    m = 1
                    for fl in ('c', 'd', 'f', 't'):
                        y = 0
                        for a1, a2 in zip((a, b, c, d), data.keys()):
                            y += a1 * data[a2][fl]
                        m = m * max(0, y)

                    # filter by calories
                    cals = 0
                    for a1, a2 in zip((a, b, c, d), data.keys()):
                        cals += a1 * data[a2]['calories']
                    if cals == 500:
                        x = max(x, m)

print(x)
