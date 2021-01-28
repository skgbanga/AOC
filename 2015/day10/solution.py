lines = [line.strip() for line in open('input').readlines()]
num = lines[0]

def conway(n):
    l = []
    cnt = 1
    for a, b in zip(n, n[1:]):
        if a == b:
            cnt += 1
        else:
            l.extend([str(cnt), a])
            cnt = 1
    l.extend([str(cnt), n[-1]])

    return ''.join(l)


for _ in range(40):
    num = conway(num)

print(len(num))
