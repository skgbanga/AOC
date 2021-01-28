nums = [int(line.strip()) for line in open('input').readlines()]

# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

s = 0
for num in nums:
    while True:
        num = num // 3 - 2
        if num <= 0:
            break
        s += num

print(s)

