from collections import Counter

lines = [line[:-1] for line in open('input').readlines()]

c = Counter()
allergens = {}
for line in lines:
    idx = line.find('(')
    ins = [token.strip() for token in line[:idx].split()]
    for i in ins:
        c[i] += 1

    alls = [token.strip(' ,') for token in line[idx + 1 + len('contains'): len(line) - 1].split()]
    for al in alls:
        allergens.setdefault(al, []).append(set(ins))

print("Number of allergens", len(allergens))


options = {}
for k, v in allergens.items():
    if len(v) == 1:
        options[k] = list(v[0])
    else:
        s = v[0] & v[1]
        for a in v[2:]:
            s = s & a
        options[k] = list(s)


match = {}
while True:
    found = False
    for k, v in options.items():
        if len(v) == 1:
            item = v[0]
            found = True
            for k1, v1 in options.items():
                if item in v1:
                    v1.remove(item)
            del options[k]
            match[k] = item
            break
    if not found:
        break

m = 0
for k, v in c.items():
    if k not in match.values():
        m += v
print(m)
print(','.join(x[1] for x in sorted(match.items(), key=lambda p:p[0])))
