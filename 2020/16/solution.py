# from itertools import product

lines = [line for line in open('input', 'r').readlines()]

fields = {}
my = []
others = []
state = 'fields'
for line in lines:
    line = line.strip()
    if not line:
        if state == 'fields':
            state = 'my'
        elif state == 'my':
            state = 'others'
    else:
        if state == 'fields':
            field, ranges = line.split(':')
            tokens = [token.strip() for token in ranges.split()]
            a, _, b = tokens
            fields[field] = [[int(x) for x in a.split('-')],
                             [int(x) for x in b.split('-')]]

        if state == 'my':
            if not line.startswith('y'):
                my = [int(num) for num in line.split(',')]

        if state == 'others':
            if not line.startswith('n'):
                others.append([int(num) for num in line.split(',')])


# print(fields)
# print(my)
# print(others)


def score(ticket):
    s = 0
    for value in ticket:
        ok = False
        for _, ranges in fields.items():
            for r in ranges:
                a, b = r
                if a <= value <= b:
                    ok = True

        if not ok:
            s += value

    return s

# part1
print(sum(score(ticket) for ticket in others))

valid = [ticket for ticket in others if score(ticket) == 0]

field_idx  = {}
for field, ranges in fields.items():
    for idx in range(len(valid[0])):
        ok = True
        for ticket in valid:
            if not any(a <= ticket[idx] <= b for a, b in ranges):
                ok = False

        if ok:
            field_idx.setdefault(field, []).append(idx)



# # solution1 - hoping for the best
# final = {}
# mark = set()
# while True:
#     for field, choices in field_idx.items():
#         choices = [c for c in choices if c not in mark]
#         if len(choices) == 1:
#             final[field] = choices[0]
#             mark.add(choices[0])
#             choices = []
#         field_idx[field] = choices
#     if len(final) == 20:
#         break

# solution2 with back-tracking
keys = list(field_idx.keys())
values = list(field_idx.values())


class State:
    def __init__(self):
        self.stack = []
    def append(self, value):
        print("Appening", value)
        self.stack.append(value)
    def pop(self):
        value = self.stack.pop()
        print("Popped", value)
    def __contains__(self, value):
        return value in self.stack

def evaluate(idx, state):
    if idx == len(values) - 1:  # base case
        for choice in values[idx]:
            if choice not in state:
                state.append(choice)
                return True
        return False
    else:
        for choice in values[idx]:
            if choice not in state:
                state.append(choice)
                result = evaluate(idx + 1, state)
                if result:
                    return True
                else:
                    state.pop()

        return False

state = []
result = evaluate(0, state)
print(result, state)

# m = 1
# for field, idx in final.items():
#     if field.startswith('departure'):
#         m *= my[idx]
# print(m)
