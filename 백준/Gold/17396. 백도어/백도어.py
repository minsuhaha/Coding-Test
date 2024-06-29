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

        for next_node, weight in graph[node]:
            cost = distance[node] + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (distance[next_node], next_node))

N, M = map(int, input().split())
see = list(map(int, input().split()))
see[-1] = 0 # 도착지점 0으로 변경
graph = [[] for _ in range(N)]
distance = [INF] * N
for _ in range(M):
    a, b, t = map(int, input().split())
    if see[a] or see[b] == 1:
        continue
    graph[a].append((b, t))
    graph[b].append((a, t))

dijkstra(0)
print(-1 if distance[N-1] == INF else distance[N-1])
