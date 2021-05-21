"""
snd X plays a sound with a frequency equal to the value of X.
set X Y sets register X to the value of Y.
add X Y increases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
"""

lines = [line.strip() for line in open("input").readlines()]

from enum import Enum, auto
from collections import defaultdict, deque


class Result(Enum):
    FINE = auto()
    FINISHED = auto()
    WAITING = auto()


class Program:
    def __init__(self, id, send, recv):
        self.d = defaultdict(int)
        self.d["p"] = id
        self.pc = 0
        self.last = 0
        self.send = send
        self.recv = recv
        self.count = 0

    def get(self, ch):
        try:
            return int(ch)
        except:
            return self.d[ch]

    def step(self):
        if self.pc >= len(lines):
            return Result.FINISHED

        line = lines[self.pc]
        tokens = line.split()
        ins = tokens[0]
        increment = 1
        if ins == "snd":
            self.send.append(self.get(tokens[1]))
            self.count += 1
        elif ins == "set":
            self.d[tokens[1]] = self.get(tokens[2])
        elif ins == "add":
            self.d[tokens[1]] += self.get(tokens[2])
        elif ins == "mul":
            self.d[tokens[1]] *= self.get(tokens[2])
        elif ins == "mod":
            self.d[tokens[1]] %= self.get(tokens[2])
        elif ins == "rcv":
            if len(self.recv) != 0:
                self.d[tokens[1]] = self.recv.popleft()
            else:
                return Result.WAITING
        elif ins == "jgz":
            if self.get(tokens[1]) > 0:
                increment = self.get(tokens[2])
        else:
            assert False

        self.pc += increment

        return Result.FINE


q1 = deque()
q2 = deque()
p0 = Program(0, q1, q2)
p1 = Program(1, q2, q1)

while True:
    r0 = p0.step()
    r1 = p1.step()
    if r0 == Result.WAITING and r1 == Result.WAITING:
        break

print(f"Program 1 sent {p1.count} values")
