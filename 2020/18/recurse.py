# EBNF
#
# E3 = NUM | '(' + E0 + ')'
# E2 = ['-'E3] | E3
# E1 = E2 [*/ E2]*
# E0 = E1 [+- E1]*

operators = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x // y,
}

def expr3(idx, tokens):
    try:
        return idx + 1, int(tokens[idx])
    except ValueError:
        assert tokens[idx] == '('
        idx, val = expr0(idx + 1, tokens)
        return idx + 1, val

def expr2(idx, tokens):
    if tokens[idx] == '-':
        idx, val = expr3(idx + 1, tokens)
        return idx, -1 * val
    return expr3(idx, tokens)

def expr1(idx, tokens):
    idx, val = expr2(idx, tokens)
    while idx < len(tokens) and (op := tokens[idx]) in ('*', '/'):
        idx, val_ = expr2(idx + 1, tokens)
        val = operators[op](val, val_)
    return idx, val

def expr0(idx, tokens):
    idx, val = expr1(idx, tokens)
    while idx < len(tokens) and (op := tokens[idx]) in ('+', '-'):
        idx, val_ = expr1(idx + 1, tokens)
        val = operators[op](val, val_)
    return idx, val

tokens = '- 3 + 4 * ( 6 - 2 ) + 4 / 2'.split()
idx, val = expr0(0, tokens)
assert idx == len(tokens)
print(val)
