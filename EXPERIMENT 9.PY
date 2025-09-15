def map_coloring(graph, colors):
    nodes = list(graph.keys())
    assignment = {}
    def backtrack(i=0):
        if i==len(nodes): return assignment.copy()
        node = nodes[i]
        for c in colors:
            if all(assignment.get(nb)!=c for nb in graph[node]):
                assignment[node]=c
                res = backtrack(i+1)
                if res: return res
                del assignment[node]
        return None
    return backtrack()
