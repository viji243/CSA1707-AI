def missionaries_cannibals(total=3):
    start = (total, total, 0, 0, 0)  # Ml, Cl, Mr, Cr, boat(0 left/1 right)
    target = (0, 0, total, total, 1)
    q = deque([(start, [])]); seen = {start}
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    while q:
        state, path = q.popleft()
        Ml, Cl, Mr, Cr, boat = state
        if state == target: return path
        if boat == 0: # move left->right
            for m,c in moves:
                if Ml>=m and Cl>=c:
                    nMl, nCl, nMr, nCr = Ml-m, Cl-c, Mr+m, Cr+c
                    if (nMl==0 or nMl>=nCl) and (nMr==0 or nMr>=nCr):
                        ns = (nMl,nCl,nMr,nCr,1)
                        if ns not in seen:
                            seen.add(ns); q.append((ns, path+[(f"{m}M{c}C ->", ns)]))
        else: # right->left
            for m,c in moves:
                if Mr>=m and Cr>=c:
                    nMl, nCl, nMr, nCr = Ml+m, Cl+c, Mr-m, Cr-c
                    if (nMl==0 or nMl>=nCl) and (nMr==0 or nMr>=nCr):
                        ns = (nMl,nCl,nMr,nCr,0)
                        if ns not in seen:
                            seen.add(ns); q.append((ns, path+[(f"<- {m}M{c}C", ns)]))
    return None
