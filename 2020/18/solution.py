# EBNF
#
# E2 = NUM | '(' + E0 + ')'
# E1 = E2 [+ E2]*
# E0 = E1 [* E1]*

lines = [line.strip() for line in open('input').readlines()]

def expr2(idx, tokens):
    token = tokens[idx]
    try:
        val = int(token)
        return idx + 1, val
    except ValueError:
        assert token in ('(', ')')
        idx, val = expr0(idx + 1, tokens)
        return idx + 1, val

def expr1(idx, tokens):
    n, val = expr2(idx, tokens)
    while n < len(tokens) and tokens[n] == '+':
        n, val_ = expr2(n + 1, tokens)
        val += val_
    return n, val

def expr0(idx, tokens):
    n, val = expr1(idx, tokens)
    while n < len(tokens) and tokens[n] == '*':
        n, val_ = expr1(n + 1, tokens)
        val *= val_
    return n, val


s = 0
for line in lines:
    line = line.replace('(', ' ( ').replace(')', ' ) ')
    tokens = [token.strip() for token in line.split()]
    n, val = expr0(0, tokens)
    assert n == len(tokens)
    s += val
print(s)
