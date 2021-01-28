lines = [line.strip() for line in open('input').readlines()]
records = []
r = []
for line in lines:
    if not line:
        records.append(' '.join(r))
        r = []
    else:
        r.append(line)

if r:
    records.append(' '.join(r))

v = 0
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for record in records:
    cnt = 0
    tokens = record.split()
    for token in tokens:
        tag, value = token.split(':')
        if tag in required:
            cnt += 1
    if cnt == len(required):
        v += 1

print(v)

def valid_ht(x):
    if x.endswith('cm'):
        n = int(x[:-2])
        return 150 <= n <= 193
    if x.endswith('in'):
        n = int(x[:-2])
        return 59 <= n <= 76

    return False

def valid_hair(x):
    if not x.startswith('#') or len(x[1:]) != 6:
        return False

    for c in x[1:]:
        if c not in '0123456789abcdef':
            return False

    return True

def valid_num(x):
    if len(x) != 9:
        return False

    try:
        int(x)
        return True
    except:
        return False

fields = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': valid_ht,
        'hcl': valid_hair,
        'ecl': lambda x: x in 'amb blu brn gry grn hzl oth'.split(),
        'pid': valid_num,
        'cid': lambda x: True
}


def valid(record):
    keys = dict()
    tokens = record.split()
    for token in tokens:
        k, v = token.split(':')
        keys[k] = v

    for f, check in fields.items():
        if f == 'cid':
            continue

        if f not in keys:
            return False

        if not check(keys[f]):
            return False

    return True


ok = sum(1 for record in records if valid(record))
print(ok)
