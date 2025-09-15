def vacuum_bfs(grid, start):
    # grid: list of list with 0=clean,1=dirty, -1=obstacle. start: (r,c)
    R, C = len(grid), len(grid[0])
    start_state = (start, tuple(tuple(row) for row in grid))
    q = deque([(start_state, [])]); seen = {start_state}
    while q:
        (pos, g), path = q.popleft()
        # check clean
        if all(all(cell!=1 for cell in row) for row in g):
            return path
        r,c = pos
        for dr,dc,act in [(-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R'),(0,0,'S')]:
            nr, nc = r+dr, c+dc
            if dr==0 and dc==0:
                # suck
                gg = [list(row) for row in g]
                if gg[r][c]==1:
                    gg[r][c]=0
                    ns = ((r,c), tuple(tuple(row) for row in gg))
                    if ns not in seen:
                        seen.add(ns); q.append((ns, path+[('suck', ns)]))
                continue
            if 0<=nr<R and 0<=nc<C and g[nr][nc]!=-1:
                ns = ((nr,nc), g)
                if ns not in seen:
                    seen.add(ns); q.append((ns, path+[(act, ns)]))
    return None

