lines = [line.strip() for line in open('input').readlines()]

f = 0
d = set()
d.add(f)
while True:
    for line in lines:
        f += int(line)
        if f in d:
            print(f)
            exit(1)
        d.add(f)
