import math


def prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


b = 108400
c = b + 17000

s = 0
while b != c:
    if not prime(b):
        s += 1
    b += 17

print(s)
