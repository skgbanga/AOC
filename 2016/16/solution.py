init = "11110010111001001"
size = 35651584

a = init
while len(a) < size:
    b = a[::-1].translate(str.maketrans({'0' : 1, '1' : '0'}))
    a = a + '0' + b

a = a[:size]

c = ''
while len(c) % 2 == 0:
    c = ''.join('1' if x == y else '0' for x, y in zip(a[::2], a[1::2]))
    a = c

print(''.join(c))
