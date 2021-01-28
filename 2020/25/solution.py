card_public_key = 18499292
door_public_key = 8790390

def transform(subject):
    n = 0
    v = 1
    while True:
        n += 1
        v = v * subject
        v = v % 20201227
        yield v, n


found = 0
for v, n in transform(7):
    if v == card_public_key:
        card_loop_number = n
        found += 1
    elif v == door_public_key:
        door_loop_number = n
        found += 1

    if found == 2:
        break


print(card_loop_number)
print(door_loop_number)

for v, n in transform(card_public_key):
    if n == door_loop_number:
        print(v)
        break

for v, n in transform(door_public_key):
    if n == card_loop_number:
        print(v)
        break
