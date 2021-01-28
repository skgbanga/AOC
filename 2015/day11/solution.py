import string

def valid(pwd):
    if any(c in 'iol' for c in pwd):
        return False

    def cons():
        for idx in range(len(pwd) - 2):
            r = pwd[idx:][:3]
            if r in string.ascii_lowercase:
                return True

        return False

    if not cons():
        return False

    s = set()
    for a, b in zip(pwd, pwd[1:]):
        if a == b:
            s.add(a * 2)

    if len(s) < 2:
        return False

    return True


start = "vzbxkghb"


def next(s):
    o = list(s)
    idx = len(o) - 1
    while idx >= 0:
        if o[idx] == 'z':
            o[idx] = 'a'
            idx -= 1
        else:
            o[idx] = chr(ord(o[idx]) + 1)
            return ''.join(o)

    # "zzzzzzzz"
    assert False

while not valid(start):
    start = next(start)

print(start)
