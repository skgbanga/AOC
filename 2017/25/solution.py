from collections import defaultdict


tape = defaultdict(int)


state = "A"
cursor = 0

for _ in range(12656374):
    v = tape[cursor]
    if state == "A":
        if v == 0:
            tape[cursor] = 1
            cursor += 1
            state = "B"
        else:
            tape[cursor] = 0
            cursor -= 1
            state = "C"
    elif state == "B":
        if v == 0:
            tape[cursor] = 1
            cursor -= 1
            state = "A"
        else:
            tape[cursor] = 1
            cursor -= 1
            state = "D"
    elif state == "C":
        if v == 0:
            tape[cursor] = 1
            cursor += 1
            state = "D"
        else:
            tape[cursor] = 0
            cursor += 1
            state = "C"
    elif state == "D":
        if v == 0:
            tape[cursor] = 0
            cursor -= 1
            state = "B"
        else:
            tape[cursor] = 0
            cursor += 1
            state = "E"
    elif state == "E":
        if v == 0:
            tape[cursor] = 1
            cursor += 1
            state = "C"
        else:
            tape[cursor] = 1
            cursor -= 1
            state = "F"
    elif state == "F":
        if v == 0:
            tape[cursor] = 1
            cursor -= 1
            state = "E"
        else:
            tape[cursor] = 1
            cursor += 1
            state = "A"


print(sum(v for v in tape.values()))
