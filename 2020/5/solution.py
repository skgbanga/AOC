lines = [line.strip() for line in open('input').readlines()]


def seat(num):
    table = str.maketrans('BFRL', '1010')
    num = num.translate(table)
    return int(num[:7], 2) * 8 + int(num[7:], 2)

seats = [seat(num) for num in lines]
seats.sort()
print(seats[-1])
for a, b in zip(seats, seats[1:]):
    if b != a + 1:
        print(a, b)
