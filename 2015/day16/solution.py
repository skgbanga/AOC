lines = [line.strip() for line in open('input').readlines()]


e = {
'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1,
}

def check(keys, values):
    for k, v in zip(keys, values):
        if k in ('cats', 'trees'):
            if v <= e[k]:
                return False
        elif k in ('goldfish', 'pomeranians'):
            if v >= e[k]:
                return False
        else:
            if e[k] != v:
                return False

    return True

for line in lines:
    tokens = line.split()
    keys = [tokens[i][:-1] for i in (2, 4, 6)]
    values = [int(tokens[i].strip(',')) for i in (3, 5, 7)]
    if check(keys, values):
        print(tokens[1])

