import hashlib

door = "cxdnnyjw"
pwd = [None] * 8
idx = 0
cnt = 0
while cnt != 8:
    p = door + str(idx)
    h = hashlib.md5(p.encode()).hexdigest()
    if h.startswith("00000"):
        pos = h[5]
        if '0' <= pos <= '7' and not pwd[int(pos)]:
            pwd[int(pos)] = h[6]
            cnt += 1
    idx += 1
    if idx % 1_000_000 == 0:
        print(idx, pwd)

print(''.join(pwd))
