def tsp_bruteforce(dist_matrix):
    n = len(dist_matrix)
    best = (math.inf, None)
    for perm in itertools.permutations(range(1,n)):
        cost = dist_matrix[0][perm[0]]
        for i in range(len(perm)-1):
            cost += dist_matrix[perm[i]][perm[i+1]]
        cost += dist_matrix[perm[-1]][0]
        if cost < best[0]:
            best = (cost, (0,)+perm+(0,))
    return best
