from collections import Counter

nums = [int(line.strip()) for line in open('input').readlines()]

# part1
nums.sort()
nums = [0] + nums + [nums[-1] + 3]
c = Counter(b - a for a, b in zip(nums, nums[1:]))
print(c[1] * c[3])


# part2
seq = []
for a, b in zip(nums, nums[1:]):
    seq.append(b - a)

freq = [[seq[0], 1]]
for a in seq[1:]:
    last, cnt = freq[-1]
    if a == 3:
        freq.append([3, 1])
    else:
        assert a == 1
        if a == last:
            freq[-1][1] += 1
        else:
            freq.append([1, 1])


d = {
        1: 1,
        2: 2,
        3: 4,
        4: 7
}

m = 1
for _, b in freq:
    m *= d[b]


# better part2
# Duh!!!
d = {}
def solve(n):
    if n == 0:
        return 1

    if n in d:
        return d[n]

    ans = 0
    for i in range(max(0, n - 3), n):
        if nums[n] - nums[i] <= 3:
            ans += solve(i)

    d[n] = ans
    return ans

n = len(nums)
print(solve(n - 1))


# iterative solution
n = len(nums)
d = [1]
for i in range(1, n):
    ans = 0
    for j in range(i):
        if nums[i] - nums[j] <= 3:
            ans += d[j]

    d.append(ans)

print(d[n - 1])
