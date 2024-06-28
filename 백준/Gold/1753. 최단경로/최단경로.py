import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start_node):
    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for v, w in graph[node]:
            cost = distance[node] + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (distance[v], v))


V, E = map(int, input().split())
K = int(input()) # 시작 정점 번호
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)
for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)
