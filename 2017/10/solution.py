lines = [line.strip() for line in open("input").readlines()]
line = lines[0]
lens = [ord(ch) for ch in line]
lens.extend([17, 31, 73, 47, 23])

N = 256
ROUNDS = 64
nums = list(range(N))


def idx(n):
    return n % N


skip = 0
current = 0
for _ in range(ROUNDS):
    for l in lens:
        i = current
        j = current + l - 1
        while i < j:
            nums[idx(i)], nums[idx(j)] = nums[idx(j)], nums[idx(i)]
            i += 1
            j -= 1
        current += l + skip
        skip += 1

from more_itertools import chunked

s = ""
for chunk in chunked(nums, 16):
    ch = chunk[0]
    for c in chunk[1:]:
        ch = ch ^ c
    s += f"{ch:02x}"

print(len(s), s)
