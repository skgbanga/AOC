# set X Y sets register X to the value of Y.
# sub X Y decreases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)


lines = [line.strip() for line in open("input").readlines()]

from collections import defaultdict

d = defaultdict(int)
d["a"] = 0


def get(ch):
    try:
        return int(ch)
    except:
        return d[ch]


mul = 0
n = len(lines)
pc = 0
while pc < n:
    line = lines[pc]
    # print(pc + 1, line, end=" ")
    ins, a, b = line.split(" ")
    if ins == "nop":
        pc += 1
    elif ins == "set":
        d[a] = get(b)
        pc += 1
    elif ins == "sub":
        d[a] = d[a] - get(b)
        pc += 1
    elif ins == "mul":
        d[a] = d[a] * get(b)
        pc += 1
        mul += 1
    else:
        z = get(a)
        if z == 0:
            pc += 1
        else:
            pc += get(b)
    print(dict(d))


print(mul, d["h"])
