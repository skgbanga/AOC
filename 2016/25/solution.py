'''
out x transmits x (either an integer or the value of a register) as the next value for the clock signal.
'''

from collections import defaultdict
lines = [line.strip() for line in open('input').readlines()]

def isint(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


d = {
    'inc' : 'dec',
    'tgl' : 'inc',
    'dec' : 'inc',
    'jnz' : 'cpy',
    'cpy' : 'jnz'
}

def run(init):
    s = ''

    mem = defaultdict(int)
    mem['a'] = init

    ip = 0
    while ip < len(lines):
        if len(s) == 100:
            return init, s

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
            if a != 0:
                ip += int(b)
                continue
        elif line.startswith('tgl'):
            _, a = line.split()
            a = int(a) if isint(a) else mem[a]
            if ip + a < len(lines):
                ins = lines[ip + a]
                lines[ip + a] = d[ins[:3]] + ins[3:]
        elif line.startswith('out'):
            _, a = line.split()
            a = int(a) if isint(a) else mem[a]
            s += str(a)
        else:
            assert False

        ip += 1



def main():
    from concurrent.futures import ProcessPoolExecutor, as_completed

    pos = list(range(200))
    with ProcessPoolExecutor() as executor:
        fs = []
        for p in pos:
            fs.append(executor.submit(run, p))
        for f in as_completed(fs):
            a, b = f.result()
            if b == '01' * 50:
                print(a)
                return

if __name__ == '__main__':
    main()
