h = 0
b = 108400
c = 108400 + 17000
for x in range(108400, c + 1, 17):
    for i in range(2,x):
        if x % i == 0:
            h += 1
            break
print(h)
