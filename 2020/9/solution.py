from collections import deque

nums = [int(line.strip()) for line in open('input').readlines()]

d = deque(nums[:25], maxlen=25)

def check(num):
    n = len(d)
    for i in range(n):
        for j in range(i + 1, n):
            if d[i] + d[j] == num:
                return True

    return False


# part 1
def errand():
    for idx, num in enumerate(nums[25:], start=25):
        if not check(num):
            return num, idx

        d.append(num)

num, idx = errand()
print(num)

# part2
def weakness():
    for size in range(1, idx):
        for i in range(idx - size):
            r = nums[i:][:size]
            if sum(r) == num:
                return min(r) + max(r)

s = weakness()
print(s)
