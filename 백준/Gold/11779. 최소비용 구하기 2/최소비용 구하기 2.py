import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start_node):
    q = []
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0
    check_node[start_node] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, weight in graph[node]:
            cost = distance[node] + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                check_node[next_node] = node
                heapq.heappush(q, (distance[next_node], next_node))

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
check_node = defaultdict() # 경로 추적을 위한 dict
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
start_node, end_node = map(int, input().split())

dijkstra(start_node)
print(distance[end_node])

check = end_node
res = []
while check:
    res.append(check)
    check = check_node[check]
print(len(res))
print(*reversed(res))
