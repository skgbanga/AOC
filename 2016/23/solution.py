import time
import sys
from collections import defaultdict
lines = [line.strip() for line in open('input').readlines()]

def isint(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

mem = defaultdict(int)
mem['a'] = int(sys.argv[1])

d = {
    'inc' : 'dec',
    'tgl' : 'inc',
    'dec' : 'inc',
    'jnz' : 'cpy',
    'cpy' : 'jnz'
}

ip = 0
idx = 0
while ip < len(lines):
    line = lines[ip]
    if line.startswith('cpy'):
        _, a, b = line.split()
        a = int(a) if isint(a) else mem[a]
        if not isint(b):
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
        b = int(b) if isint(b) else mem[b]
        assert b < 0
        if a != 0:
            ip += int(b)
            continue
    elif line.startswith('tgl'):
        _, a = line.split()
        a = int(a) if isint(a) else mem[a]
        if ip + a < len(lines):
            ins = lines[ip + a]
            lines[ip + a] = d[ins[:3]] + ins[3:]
    else:
        assert False

    ip += 1

print(mem['a'])
