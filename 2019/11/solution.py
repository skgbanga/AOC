from collections import defaultdict, deque

class Runner:
    def __init__(self):
        line = open('input').readlines()[0]
        self.nums = defaultdict(int)
        for idx, token in enumerate(line.split(',')):
            self.nums[idx] = int(token)
        self.idx = 0
        self.base = 0
        self.finished = False

    def value(self, m, idx):
        if m == 0:  # position
            return self.nums[self.nums[idx]]
        elif m == 1:  # immediate
            return self.nums[idx]
        elif m == 2:  # relative
            return self.nums[self.base + self.nums[idx]]
        else:
            assert False

    def execute(self, data=None):
        ins = self.nums[self.idx]
        m1 = (ins // 100) % 10
        m2 = (ins // 1000) % 10
        m3 = (ins // 10000) % 10

        ins = ins % 100
        if ins == 1:
            a = self.value(m1, self.idx + 1)
            b = self.value(m2, self.idx + 2)
            c = self.nums[self.idx + 3] if m3 == 0 else self.nums[self.idx + 3] + self.base
            self.nums[c] = a + b
            self.idx += 4
        elif ins == 2:
            a = self.value(m1, self.idx + 1)
            b = self.value(m2, self.idx + 2)
            c = self.nums[self.idx + 3] if m3 == 0 else self.nums[self.idx + 3] + self.base
            self.nums[c] = a * b
            self.idx += 4
        elif ins == 3:
            if m1 == 0:
                a = self.nums[self.idx + 1]
            else:
                assert m1 == 2
                a = self.nums[self.idx + 1] + self.base
            self.nums[a] = data
            self.idx += 2
        elif ins == 4:
            a = self.value(m1, self.idx + 1)
            self.idx += 2
            return True, a
        elif ins == 5:
            a = self.value(m1, self.idx + 1)
            b = self.value(m2, self.idx + 2)
            if a != 0:
                self.idx = b
            else:
                self.idx += 3
        elif ins == 6:
            a = self.value(m1, self.idx + 1)
            b = self.value(m2, self.idx + 2)
            if a == 0:
                self.idx = b
            else:
                self.idx += 3
        elif ins == 7:
            a = self.value(m1, self.idx + 1)
            b = self.value(m2, self.idx + 2)
            c = self.nums[self.idx + 3] if m3 == 0 else self.nums[self.idx + 3] + self.base
            if a < b:
                self.nums[c] = 1
            else:
                self.nums[c] = 0
            self.idx += 4
        elif ins == 8:
            a = self.value(m1, self.idx + 1)
            b = self.value(m2, self.idx + 2)
            c = self.nums[self.idx + 3] if m3 == 0 else self.nums[self.idx + 3] + self.base
            if a == b:
                self.nums[c] = 1
            else:
                self.nums[c] = 0
            self.idx += 4
        elif ins == 9:
            a = self.value(m1, self.idx + 1)
            self.base += a
            self.idx += 2
        elif ins == 99:
            self.finished = True
        else:
            assert False, f"ins = {ins}"

        return False, 0

# First, it will output a value indicating the color to paint the panel the robot is over: 
# 0 means to paint the panel black,
# and 1 means to paint the panel white.

# Second, it will output a value indicating the direction the robot should turn:
# 0 means it should turn left 90 degrees
# and 1 means it should turn right 90 degrees.



def run(painted):
    x, y = 0, 0
    d = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]


    runner = Runner()
    while True:
        # print('Running for ', x, y)
        if (x, y) in painted:
            color = painted[(x, y)]
            if color == 'black':
                data = 0
            else:
                assert color == 'white'
                data = 1
        else:
            if x == 0 and y == 0:
                data = 1
            else:
                data = 0
            # data = 0  # all panels start as black

        while True:
            result, value = runner.execute(data)
            if runner.finished:
                return

            if result:
                if value == 0:
                    painted[(x, y)] = 'black'
                else:
                    assert value == 1
                    painted[(x, y)] = 'white'
                break

        while True:
            assert not runner.finished
            result, value = runner.execute()
            if runner.finished:
                return
            if result:
                if value == 0:
                    d = (d - 1) % 4
                else:
                    assert value == 1
                    d = (d + 1) % 4
                x += dx[d]
                y += dy[d]
                break

painted = {}
run(painted)

print(len(painted))

Xmin = min(x for x, _ in painted.keys())
Xmax = max(x for x, _ in painted.keys())
Ymin = min(y for _, y in painted.keys())
Ymax = max(y for _, y in painted.keys())

for y in range(Ymax, Ymin - 1, -1):
    for x in range(Xmin, Xmax + 1):
        if (x, y) in painted and painted[(x, y)] == 'white':
            print('.', end='')
        else:
            print(' ', end='')
    print()
