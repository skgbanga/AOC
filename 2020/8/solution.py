from copy import deepcopy
lines = [line.strip() for line in open('input').readlines()]

def circle(data):
    accum = 0
    seen = set()
    runner = 0

    while runner < len(data):
        if runner in seen:
            return True, accum

        seen.add(runner)
        line = data[runner]
        ins, num = line.split()
        if ins == 'nop':
            runner += 1
        elif ins == 'jmp':
            runner += int(num)
        elif ins == 'acc':
            accum += int(num)
            runner += 1

    return False, accum


# part1
print(circle(lines)[1])

# part2
for idx, line in enumerate(lines):
    data = deepcopy(lines)
    ins, num = line.split()
    if ins == 'acc':
        continue

    if ins == 'nop':
        data[idx] = f'jmp {num}'
    else:
        data[idx] = f'nop {num}'

    result, ans = circle(data)
    if not result:
        print(ans)
        break
