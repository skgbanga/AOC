line = [line.strip() for line in open("input").readlines()][0]


def dance(data):
    for token in line.split(","):
        s = token[0]
        if s == "s":
            num = int(token[1:])
            assert num < 16
            data = data[-num:] + data[: len(data) - num]
        elif s == "x":
            i, j = map(int, token[1:].split("/"))
            data[i], data[j] = data[j], data[i]
        elif s == "p":
            a, b = token[1:].split("/")
            i = data.index(a)
            j = data.index(b)
            data[i], data[j] = data[j], data[i]
        else:
            assert False

    return "".join(data)


data = "abcdefghijklmnop"
d = {}
for i in range(10):
    if data in d:
        print(f"Seen {data} at {i}")
        break
    d[data] = i
    data = dance(list(data))

print(data)
