import sys
from collections import deque
sys.stdin.readline


def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return visited

n = int(input()) # 총 도시의 수
m = int(input()) # 계획 도시 수

city = []
for _ in range(n):
    city.append(list(map(int, input().split())))
plan = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            graph[i+1].append(j+1)

visited = [False] * (n+1)
bfs(plan[0])

flag = True
for p in plan:
    if not visited[p]:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
