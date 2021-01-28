line = open('input').readlines()[0]
# line = '3,0,4,0,99'
nums = [int(token) for token in line.split(',')]

idx = 0
while idx < len(nums):
    ins = nums[idx]
    if ins == 99:
        break
    elif ins == 3:
        nums[nums[idx + 1]] = int(input())
        idx += 2
    elif ins == 4:
        print(nums[nums[idx + 1]])
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
