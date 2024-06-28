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

        for n, v in graph[node]:
            cost = distance[node] + v
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (distance[n], n))


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


dijkstra(1)
print(distance[N])
