from collections import defaultdict

line = open('input').readlines()[0]
nums = defaultdict(int)
for idx, token in enumerate(line.split(',')):
    nums[idx] = int(token)

base = 0
def value(m, idx):
    if m == 0:  # position
        return nums[nums[idx]]
    elif m == 1:  # immediate
        return nums[idx]
    elif m == 2:  # relative
        return nums[base + nums[idx]]
    else:
        assert False


idx = 0
def execute(ins, modes):
    global idx
    global base
    m1, m2, m3 = modes
    if ins == 1:
        a = value(m1, idx + 1)
        b = value(m2, idx + 2)
        c = nums[idx + 3] if m3 == 0 else nums[idx + 3] + base
        nums[c] = a + b
        idx += 4
    elif ins == 2:
        a = value(m1, idx + 1)
        b = value(m2, idx + 2)
        c = nums[idx + 3] if m3 == 0 else nums[idx + 3] + base
        nums[c] = a * b
        idx += 4
    elif ins == 3:
        if m1 == 0:
            a = nums[idx + 1]
        else:
            assert m1 == 2
            a = nums[idx + 1] + base
        nums[a] = int(input())
        idx += 2
    elif ins == 4:
        a = value(m1, idx + 1)
        print(a)
        idx += 2
    elif ins == 5:
        a = value(m1, idx + 1)
        b = value(m2, idx + 2)
        if a != 0:
            idx = b
        else:
            idx += 3
    elif ins == 6:
        a = value(m1, idx + 1)
        b = value(m2, idx + 2)
        if a == 0:
            idx = b
        else:
            idx += 3
    elif ins == 7:
        a = value(m1, idx + 1)
        b = value(m2, idx + 2)
        c = nums[idx + 3] if m3 == 0 else nums[idx + 3] + base
        if a < b:
            nums[c] = 1
        else:
            nums[c] = 0
        idx += 4
    elif ins == 8:
        a = value(m1, idx + 1)
        b = value(m2, idx + 2)
        c = nums[idx + 3] if m3 == 0 else nums[idx + 3] + base
        if a == b:
            nums[c] = 1
        else:
            nums[c] = 0
        idx += 4
    elif ins == 9:
        a = value(m1, idx + 1)
        base += a
        idx += 2
    elif ins == 99:
        return False
    else:
        assert False, f"d = {d}, ins = {ins}"

    return True

while True:
    ins = nums[idx]
    m1 = (ins // 100) % 10
    m2 = (ins // 1000) % 10
    m3 = (ins // 10000) % 10
    modes = [m1, m2, m3]

    ins = ins % 100
    if not execute(ins, modes):
        break
