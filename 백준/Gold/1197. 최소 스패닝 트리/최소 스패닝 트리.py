import sys, heapq
input = sys.stdin.readline


def mst(start_node):
    q = []
    heapq.heappush(q, (0, start_node))
    mst_weight = 0
    edge_cnt = 0

    while q:
        weight, node = heapq.heappop(q)

        if visited[node]:
            continue
        
        visited[node] = True
        mst_weight += weight

        edge_cnt += 1
        if edge_cnt == v:
            return mst_weight
            
        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(q, (next_weight, next_node))


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [False] * (v+1)
print(mst(1))
