# EBNF
#
# E2 = NUM | '(' + E0 + ')'
# E1 = E2 [*/ E2]*
# E0 = E1 [+- E1]*

operators = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x // y,
}
precedence = {'+' : 0, '-' : 0, '*' : 1, '/': 1}


from collections import deque
def solve(tokens):
    rpn = deque()
    stack = []
    for token in tokens:
        try:
            rpn.append(int(token))
        except ValueError:
            if token in precedence:
                if not stack:
                    stack.append(token)
                else:
                    while stack:
                        top = stack[-1]
                        if top == '(' or precedence[top] < precedence[token]:
                            break
                        rpn.append(stack.pop())
                    stack.append(token)
            else:
                if token == '(':
                    stack.append(token)
                else:
                    assert token == ')'
                    while (op := stack.pop()) != '(':
                        rpn.append(op)
    while stack:
        rpn.append(stack.pop())


    evals = []
    while rpn:
        token = rpn.popleft()
        if token in operators:
            b = evals.pop()
            a = evals.pop()
            evals.append(operators[token](a, b))
        else:
            evals.append(token)

    assert len(evals) == 1
    return evals[0]


tokens = '-3 + 4 * ( 6 - 2 ) + 4 / 2'.split()
val = solve(tokens)
print(val)
