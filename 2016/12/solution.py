from collections import defaultdict
lines = [line.strip() for line in open('input').readlines()]

def isint(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

mem = defaultdict(int)
mem['c'] = 1

ip = 0
while ip < len(lines):
    line = lines[ip]
    if line.startswith('cpy'):
        _, a, b = line.split()
        a = int(a) if isint(a) else mem[a]
        mem[b] = a
    elif line.startswith('inc'):
        _, a = line.split()
        mem[a] += 1
    elif line.startswith('dec'):
        _, a = line.split()
        mem[a] -= 1
    elif line.startswith('jnz'):
        _, a, b = line.split()
        a = int(a) if isint(a) else mem[a]
        if a != 0:
            ip += int(b)
            continue
    ip += 1

print(mem['a'])
        
