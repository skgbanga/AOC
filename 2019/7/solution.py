from collections import deque

line = open('input').readlines()[0]
# line = '3,0,4,0,99'
# line = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
initial = [int(token) for token in line.split(',')]

def evaluate(inputs, nums):
    idx = 0
    # while idx < len(nums):
    while True:
        ins = nums[idx]
        if ins == 99:
            break
        elif ins == 3:
            nums[nums[idx + 1]] = inputs.popleft()
            idx += 2
        elif ins == 4:
            yield nums[nums[idx + 1]]
            # return nums[nums[idx + 1]]
            # print(nums[nums[idx + 1]])
            idx += 2
        elif ins == 1:
            nums[nums[idx + 3]] = nums[nums[idx + 1]] + nums[nums[idx + 2]]
            idx += 4
        elif ins == 2:
            nums[nums[idx + 3]] = nums[nums[idx + 1]] * nums[nums[idx + 2]]
            idx += 4
        elif ins == 5:
            if nums[num[idx + 1]] != 0:
                idx = nums[nums[idx + 2]]
            else:
                idx += 3
        elif ins == 6:
            if nums[num[idx + 1]] == 0:
                idx = nums[nums[idx + 2]]
            else:
                idx += 3
        elif ins == 7:
            if nums[nums[idx + 1]] < nums[nums[idx + 2]]:
                nums[nums[idx + 3]] = 1
            else:
                nums[nums[idx + 3]] = 0
            idx += 4
        elif ins == 8:
            if nums[nums[idx + 1]] == nums[nums[idx + 2]]:
                nums[nums[idx + 3]] = 1
            else:
                nums[nums[idx + 3]] = 0
            idx += 4
        else:
            d = ins % 100
            if d == 1:
                m1 = (ins // 100) % 10
                m2 = (ins // 1000) % 10
                a = nums[nums[idx + 1]] if m1 == 0 else nums[idx + 1]
                b = nums[nums[idx + 2]] if m2 == 0 else nums[idx + 2]
                nums[nums[idx + 3]] = a + b
                idx += 4
            elif d == 2:
                m1 = (ins // 100) % 10
                m2 = (ins // 1000) % 10
                a = nums[nums[idx + 1]] if m1 == 0 else nums[idx + 1]
                b = nums[nums[idx + 2]] if m2 == 0 else nums[idx + 2]
                nums[nums[idx + 3]] = a * b
                idx += 4
            elif d == 4:
                m1 = (ins // 100) % 10
                a = nums[nums[idx + 1]] if m1 == 1 else nums[idx + 1]
                print(a)
                idx += 2
            elif d == 5:
                m1 = (ins // 100) % 10
                m2 = (ins // 1000) % 10
                a = nums[nums[idx + 1]] if m1 == 0 else nums[idx + 1]
                b = nums[nums[idx + 2]] if m2 == 0 else nums[idx + 2]
                if a != 0:
                    idx = b
                else:
                    idx += 3
            elif d == 6:
                m1 = (ins // 100) % 10
                m2 = (ins // 1000) % 10
                a = nums[nums[idx + 1]] if m1 == 0 else nums[idx + 1]
                b = nums[nums[idx + 2]] if m2 == 0 else nums[idx + 2]
                if a == 0:
                    idx = b
                else:
                    idx += 3
            elif d == 7:
                m1 = (ins // 100) % 10
                m2 = (ins // 1000) % 10
                a = nums[nums[idx + 1]] if m1 == 0 else nums[idx + 1]
                b = nums[nums[idx + 2]] if m2 == 0 else nums[idx + 2]
                if a < b:
                    nums[nums[idx + 3]] = 1
                else:
                    nums[nums[idx + 3]] = 0
                idx += 4
            elif d == 8:
                m1 = (ins // 100) % 10
                m2 = (ins // 1000) % 10
                a = nums[nums[idx + 1]] if m1 == 0 else nums[idx + 1]
                b = nums[nums[idx + 2]] if m2 == 0 else nums[idx + 2]
                if a == b:
                    nums[nums[idx + 3]] = 1
                else:
                    nums[nums[idx + 3]] = 0
                idx += 4
            else:
                assert False, f"d = {d}, ins = {ins}"

    # print('Exiting the loop')
    # assert False, 'Reached to the end without output instruction'

from collections import deque
from copy import deepcopy
import itertools


m = 0
for perm in itertools.permutations([5, 6, 7, 8, 9]):
    # construct gens
    inputs = []
    amps = []
    for _ in range(5):
        d = deque()
        inputs.append(d)
        amps.append(evaluate(d, initial.copy()))

    # seed the loop once
    for idx in range(5):
        inputs[idx].append(perm[idx])

    start = 0
    idx = 0
    try:
        while True:
            inputs[idx].append(start)
            start = next(amps[idx])
            idx = (idx + 1) % 5
    except StopIteration:
        m = max(m, start)

print(m)
