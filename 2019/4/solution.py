start=109165
end=576723


# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).


def same(s):
    r = set()
    for a, b in zip(s, s[1:]):
        if a == b:
            r.add(a)
    return r

def increasing(s):
    for a, b in zip(s, s[1:]):
        if a > b:
            return False
    return True


def check(s, r):
    for c in r:
        idx = s.index(c)
        a = idx + 2
        if a >= len(s) or s[a] != c:
            return True

    return False


cnt = 0
for i in range(start, end):
    s = str(i)
    r = same(s)
    if not r:
        continue

    if not check(s, r):
        continue

    if not increasing(s):
        continue
    cnt += 1

print(cnt)
