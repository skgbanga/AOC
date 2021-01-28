from collections import deque
lines = [line.strip() for line in open('input', 'r').readlines()]

mem = {}

def generate(addr):
    q = deque()
    q.append(addr)
    while True:
        top = q[0]
        if 'X' not in top:
            break
        top = q.popleft()
        idx = top.index('X')
        q.append(top[:idx] + '0' + top[idx + 1:])
        q.append(top[:idx] + '1' + top[idx + 1:])

    return q

m = 0
for line in lines:
    if line.startswith('mask'):
        *_, m  = line.split()
    elif line.startswith('mem'):
        addr, _, value = line.split()
        addr = int(addr[4:-1])
        value = int(value)
        # part1
        #
        # value = '{:0>36}'.format(bin(value)[2:])
        # v = []
        # for a, b in zip(m, value):
        #     if a == 'X':
        #         v.append(b)
        #     else:
        #         v.append(a)

        # mem[addr] = int(''.join(v), 2)
        addr = '{:0>36}'.format(bin(addr)[2:])
        v = []
        for a, b in zip(m, addr):
            if a == '0':
                v.append(b)
            else:
                v.append(a)  # 1 or X
        addrs = generate(''.join(v))
        for addr in addrs:
            addr = int(addr, 2)
            mem[addr] = value

print(sum(mem.values()))
