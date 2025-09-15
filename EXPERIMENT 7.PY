def bfs_graph(graph, start):
    q = deque([start]); seen = {start}; order=[]
    while q:
        v=q.popleft(); order.append(v)
        for w in graph.get(v,[]):
            if w not in seen:
                seen.add(w); q.append(w)
    return order

def dfs_graph(graph, start):
    seen=set(); order=[]
    def dfs(v):
        seen.add(v); order.append(v)
        for w in graph.get(v,[]):
            if w not in seen: dfs(w)
    dfs(start); return order
