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


N = int(input())
M = int(input())
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())

dijkstra(start)
print(distance[end])
