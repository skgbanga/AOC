from contextlib import suppress

lines = [line.strip() for line in open('input').readlines()]

d = {
    'AND' : '__and__',
    'OR' : '__or__',
    'LSHIFT' : '__lshift__',
    'RSHIFT' : '__rshift__',
}

def isint(x):
    with suppress(Exception):
        int(x)
        return True

    return False

wires = {'b' : 956}
while True:
    updated = False
    for line in lines:
        tokens = line.split()
        if 'AND' in line or 'OR' in line:
            a, op, b, _, c = tokens
            with suppress(Exception):
                a = a if isint(a) else wires[a]
                b = b if isint(b) else wires[b]
                if c not in wires:
                    wires[c] = getattr(int(a), d[op])(int(b))
                    updated = True
        elif 'RSHIFT' in line or 'LSHIFT' in line:
            a, op, n, _, c = tokens
            if a in wires and c not in wires:
                wires[c] = getattr(wires[a], d[op])(int(n))
                updated = True
        elif 'NOT' in line:
            _, a, _, c = tokens
            if a in wires and c not in wires:
                wires[c] = ~wires[a]
                updated = True
        else:
            value, _, w = tokens
            with suppress(Exception):
                value = value if isint(value) else wires[value]
                if w not in wires:
                    wires[w] = int(value)
                    updated = True
        
    if not updated:
        break

print(wires['a'])
