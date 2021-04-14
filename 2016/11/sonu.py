from itertools import combinations

# check if sets of generators and microchips, sg and sm, can co-exist on a floor
def checkstate(sg, sm):
    return (not sg) or sm.issubset(sg)

# return a set of all possible previous states for the current state sc
# sg is a tuple of generators, sm is a tuple of microchips for current floor of elevator in sc
# sgsm is a list of lists of pair of tuples (converted to sets) that could potentially be moved from current floor to another
# [[sg_to_move, sm_to_move], [...], ...]
def prevstates(sc):
    pstates = []
    pos = sc[0]
    sg = set(sc[2 * pos - 1])
    sm = set(sc[2 * pos])
    sgsm =  [[set(i), set()] for i in combinations(sg, 2) if checkstate(sg - set(i), sm)]
    sgsm += [[set(i), set()] for i in combinations(sg, 1) if checkstate(sg - set(i), sm)]
    sgsm += [[set(), set(i)] for i in combinations(sm, 2) if checkstate(sg, sm - set(i))]
    sgsm += [[set(), set(i)] for i in combinations(sm, 1) if checkstate(sg, sm - set(i))]
    sgsm += [[set(i), set(i)] for i in combinations(sg.intersection(sm), 1) if checkstate(sg - set(i), sm - set(i))]

    prev_pos_list = []
    if pos > 1:
        prev_pos_list += [pos - 1]
    if pos < 4:
        prev_pos_list += [pos + 1]
    
    for pos1 in prev_pos_list:
        sgp = set(sc[2 * pos1 - 1])
        smp = set(sc[2 * pos1])
        pstate = [pos1] + [() for _ in range(8)]
        for i in range(1, 5):
            if (i != pos) or (i != pos1):
                pstate[2 * i] = sc[2 * i]
                pstate[2 * i - 1] = sc[2 * i - 1]
        for sgi, smi in sgsm:
            sgu, smu = sgp.union(sgi), smp.union(smi)
            if checkstate(sgu, smu):
                pstate[2 * pos - 1] = tuple(sorted(sg - sgi))
                pstate[2 * pos] = tuple(sorted(sm - smi))
                pstate[2 * pos1 - 1] = tuple(sorted(sgu))
                pstate[2 * pos1] = tuple(sorted(smu))
                pstates.append(tuple(pstate))

    return set(pstates)

# this problem will give the same answer if sinit and sfinal are exchanged with each other
# a state is stored as (pos, (tg1s), (tm1s), (tg2s), (tm2s) ....), where pos is elevator position, 
# and tgs and tms are tuples of generators and microchips, stored in ascending order
# set seen is used to store previously computed states, to save time and to keep the current set of all states setstates small 
sinit = (1, (1,), (1,), (2, 3, 4, 5), (), (), (2, 3, 4, 5), (), ())
sfinal = (4, (), (), (), (), (), (), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5))
# sinit = (1, (1, 6, 7,), (1, 6, 7), (2, 3, 4, 5), (), (), (2, 3, 4, 5), (), ())
# sfinal = (4, (), (), (), (), (), (), (1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 7))

seen = set()
setstates = set([sfinal])
steps = 0
while sinit not in setstates:
    setpstates = set()
    for state in setstates:
        if state not in seen:
            seen.add(state)
            setpstates.update(prevstates(state))
    steps += 1
    setstates = setpstates
    print(steps, len(setstates))
    
print(steps)
