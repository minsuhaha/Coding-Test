import sys
import heapq
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start_node, end_node):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, weight in graph[node]:
            cost = distance[node] + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (distance[next_node], next_node))

    return distance[end_node]

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

max_t = 0
for i in range(1, N+1):
    if i == X:
        continue
    max_t = max(max_t, dijkstra(i, X) + dijkstra(X, i)) 

print(max_t)
