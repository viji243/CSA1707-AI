def manhattan(state, goal):
    # state and goal are tuples of length 9 (0 as blank)
    dist = 0
    for i, v in enumerate(state):
        if v == 0: continue
        gi = goal.index(v)
        dist += abs(i//3 - gi//3) + abs(i%3 - gi%3)
    return dist
