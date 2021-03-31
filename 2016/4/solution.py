from collections import Counter

lines = [line.strip() for line in open('input').readlines()]


def rotate(c, sid):
    if c == '-':
        return ' '
    return chr((ord(c) - 97 + sid) % 26 + 97)



total = 0
for line in lines:
    idx = line.index('[')
    csum = line[idx + 1:-1]
    *tokens, sid = line[:idx].split('-')
    c = Counter(''.join(tokens))
    s = ''.join(a for a, _ in sorted(c.most_common(), reverse=True, key=lambda x : (x[1], -ord(x[0]))))[:5]
    if s == csum:
        code = []
        for ch in '-'.join(tokens):
            code.append(rotate(ch, int(sid)))
        print(''.join(code), int(sid))
        # total += int(sid)
# print(total)

