lines = [line.strip() for line in open("input").readlines()]

import re


def man(nums):
    return sum(abs(x) for x in nums[:3])


ps = []
for line in lines:
    nums = list(map(int, re.findall("-*\d+", line)))
    nums.append(man(nums))
    ps.append(nums)

# for p in ps:
#     print(p)

# we run till manhattan distance of all particles start increasing
for rounds in range(1000):
    d = {}
    indices = set()

    for idx, nums in enumerate(ps):
        m = nums[-1]
        for i in range(3, 6):
            nums[i] += nums[i + 3]
        for i in range(3):
            nums[i] += nums[i + 3]
        nums[-1] = man(nums)

        t = tuple(nums[:3])
        if t in d:
            indices.add(idx)
            indices.add(d[t])
        else:
            d[t] = idx

    ps = [nums for idx, nums in enumerate(ps) if idx not in indices]

    rounds += 1
    print(len(ps), rounds)

# choose the min manhattan distance
print(len(ps))
