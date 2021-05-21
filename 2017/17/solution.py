class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(0)
head.next = head


N = 386

current = head
for i in range(1, 50000001):
    for _ in range(N):
        current = current.next

    n = Node(i)
    n.next = current.next
    current.next = n

    current = n

h = head
for _ in range(50000000):
    if h.value == 0:
        print(h.next.value)
        break
    else:
        h = h.next
