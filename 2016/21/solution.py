import re

lines = [line.strip() for line in open('input').readlines()]

def scramble(data):
    for line in lines:
        if 'swap position' in line:
            a, b = map(int, re.findall('\d+', line))
            data[a], data[b] = data[b], data[a]
        elif 'swap letter' in line:
            _, _, a, _, _, b = line.split()
            for idx, ch in enumerate(data):
                if ch == a:
                    data[idx] = b
                elif ch == b:
                    data[idx] = a
        elif 'rotate left' in line:
            a = int(line.split()[2])
            data = data[a:] + data[:a]
        elif 'rotate right' in line:
            a = int(line.split()[2])
            data = data[-a:] + data[:-a]
        elif 'rotate based on position' in line:
            ch = line.split()[-1]
            idx = data.index(ch)
            rot = 1 + idx
            if idx >= 4:
                rot += 1
            for _ in range(rot):
                data = data[-1:] + data[:-1]
        elif 'reverse positions' in line:
            a, b = map(int, re.findall('\d+', line))
            while a < b:
                data[a], data[b] = data[b], data[a]
                a += 1
                b -= 1
        elif 'move position' in line:
            a, b = map(int, re.findall('\d+', line))
            ch = data.pop(a)
            data.insert(b, ch)
        else:
            assert False

    return ''.join(data)

from itertools import permutations
for perm in permutations('abcdefgh'):
    ans = scramble(list(perm))
    if ans == 'fbgdceah':
        print(''.join(perm))
        break
