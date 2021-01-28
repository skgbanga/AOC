from collections import Counter

lines = [int(line.strip()) for line in open('input').readlines()]
lines.sort()

def solve(target, weights):
    if not weights or weights[0] > target:
        return 0, []

    if target == weights[0]:
        cnt = weights.count(target)
        return cnt, [[target] for _ in range(cnt)]

    remaining = target - weights[0]
    a, b = solve(target, weights[1:])
    c, d = solve(remaining, weights[1:])
    return a + c, b + [i + [weights[0]] for i in d]


n, ways = solve(150, lines)
s = min(len(x) for x in ways)
print(n)  # part1
print(sum(1 for key in ways if len(key) == s))  # part2
