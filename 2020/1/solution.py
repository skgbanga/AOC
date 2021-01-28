nums = [int(line.strip()) for line in open('input').readlines()]
lookup = set(nums)

for num in nums:
    other = 2020 - num
    if other in lookup:
        print(other * num)
        break

for i, a in enumerate(nums):
    for _, b in enumerate(nums[i:]):
        other = 2020 - (a + b)
        if other in lookup:
            print(other * a * b)
            exit(1)
