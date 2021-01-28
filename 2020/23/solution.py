# The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
# The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
# The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
# The crab selects a new current cup: the cup which is immediately clockwise of the current cup.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

circle = '963275481'
d = {}
node = Node(int(circle[0]))
d[node.val] = node
curr = node
for c in circle[1:]:
    n = Node(int(c))
    d[n.val] = n
    node.next = n
    node = n

for i in range(10, 1_000_001):
    n = Node(i)
    d[n.val] = n
    node.next = n
    node = n

node.next = curr
largest = 1_000_000

def show():
    s = curr
    for _ in range(9):
        print(s.val, end='')
        s = s.next
    print()


for i in range(10_000_000):
    selected = []
    for _ in range(3):
        selected.append(curr.next.val)
        d.pop(curr.next.val)
        curr.next = curr.next.next

    dst = curr.val - 1
    if dst == 0:
        dst = largest
    while dst in selected:
        dst = dst - 1
        if dst == 0:
            dst = largest

    tmp = d[dst]
    for s in selected:
        n = Node(s)
        d[s] = n
        n.next = tmp.next
        tmp.next = n
        tmp = n

    curr = curr.next

n  = d[1]
print(n.next.val * n.next.next.val)
