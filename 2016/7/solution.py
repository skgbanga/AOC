lines = [line.strip() for line in open('input').readlines()]

def abas(s):
    ans = []
    for i in range(len(s)):
        ss = s[i:i + 3]
        if len(ss) == 3:
            a, b, c = ss
            if a == c and a != b:
                ans.append(ss)
    return ans

def check(ss, ops):
    for op in ops:
        assert len(op) == 3, f"{op}"
        a, b, c = op
        for s in ss:
            if f'{b}{a}{b}' in s:
                return True

    return False

cnt = 0
for line in lines:
    outs = []
    ins = []
    while line:
        try:
            start = line.index('[')
        except ValueError:
            outs.append(line)
            break

        outs.append(line[:start])
        end = line.index(']')
        ins.append(line[start + 1:end])
        line = line[end + 1:]

    ops = []
    for s in outs:
        ops.extend(abas(s))
    cnt += check(ins, ops)

print(cnt)
