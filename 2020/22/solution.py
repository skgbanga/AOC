from copy import deepcopy
from collections import deque 
lines = [line.strip() for line in open('input').readlines()]


two = False
p1 = deque()
p2 = deque()
for line in lines:
    if not line:
        two = True
        continue
    if line.startswith('Player'):
        continue
    if two:
        p2.append(int(line))
    else:
        p1.append(int(line))


# while p1 and p2:
#     c1 = p1.popleft()
#     c2 = p2.popleft()
#     if c1 > c2:
#         p1.extend((c1, c2))
#     elif c2 > c1:
#         p2.extend((c2, c1))
#     else:
#         assert False


# p = p1 if p1 else p2

# l = len(p)
# s = 0
# for e in p:
#     s += l * e
#     l -= 1

# print(s)

# Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
# Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
# If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
# Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.

def solve(s1, s2):
    ph1 = []
    ph2 = []

    rn = 1
    while s1 and s2:
        if s1 in ph1 or s2 in ph2:
            return 1, s1

        ph1.append(deepcopy(s1))
        ph2.append(deepcopy(s2))
        c1 = s1.popleft()
        c2 = s2.popleft()
        if len(s1) >= c1 and len(s2) >= c2:
            ss1 = deque(s1[i] for i in range(c1))
            ss2 = deque(s2[i] for i in range(c2))
            result, _ = solve(ss1, ss2)
            if result == 1:
                s1.extend((c1, c2))
            else:
                assert result == 2
                s2.extend((c2, c1))
        else:
            if c1 > c2:
                s1.extend((c1, c2))
            elif c2 > c1:
                s2.extend((c2, c1))
            else:
                assert False

    if s1:
        return 1, s1
    else:
        return 2, s2

_, p = solve(p1, p2)
l = len(p)
s = 0
for e in p:
    s += l * e
    l -= 1
print(s)
