lines = [line.strip() for line in open('input').readlines()]
nums = [int(num) for num in lines[0].split(',')]

from copy import deepcopy

master = deepcopy(nums)
for noun in range(100):
    for verb in range(100):
        nums = deepcopy(master)
        nums[1] = noun
        nums[2] = verb

        idx = 0
        while idx < len(nums):
            a = nums[idx]
            if a == 99:
                break
            elif a == 1:
                nums[nums[idx + 3]] = nums[nums[idx + 1]] + nums[nums[idx + 2]]
                idx += 4
            elif a == 2:
                nums[nums[idx + 3]] = nums[nums[idx + 1]] * nums[nums[idx + 2]]
                idx += 4
            else:
                assert False


        if nums[0] == 19690720:
            print('Found', noun, verb)
            break
