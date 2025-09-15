def water_jug(capacities, target):
    start = tuple([0]*len(capacities))
    q = deque([(start, [])])
    seen = {start}
    while q:
        state, path = q.popleft()
        if target in state:
            return path, state
        # fill
        for i in range(len(capacities)):
            new = list(state); new[i]=capacities[i]
            t = tuple(new)
            if t not in seen:
                seen.add(t); q.append((t, path+[(f"fill {i}", t)]))
        # empty
        for i in range(len(capacities)):
            new = list(state); new[i]=0
            t = tuple(new)
            if t not in seen:
                seen.add(t); q.append((t, path+[(f"empty {i}", t)]))
        # pour i->j
        for i in range(len(capacities)):
            for j in range(len(capacities)):
                if i==j or state[i]==0 or state[j]==capacities[j]: continue
                amount = min(state[i], capacities[j]-state[j])
                new = list(state)
                new[i]-=amount; new[j]+=amount
                t = tuple(new)
                if t not in seen:
                    seen.add(t); q.append((t, path+[(f"pour {i}->{j}", t)]))
    return None

