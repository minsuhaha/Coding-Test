import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start_node, end_node):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, ((0, start_node)))
    distance[start_node] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for n, v in graph[node]:
            cost = distance[node] + v
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, ((distance[n], n)))
    
    return distance[end_node] 

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

res1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
res2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

result = min(res1, res2)
if result == INF:
    print(-1)
else:
    print(result)
