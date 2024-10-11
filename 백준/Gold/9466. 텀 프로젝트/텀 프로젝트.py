import sys
from collections import deque
input = sys.stdin.readline


def bfs(node):
    queue = deque([node])
    visited[node] = True
    team = []

    while queue:
        node = queue.popleft()
        team.append(node)

        next_node = graph[node]
        if visited[next_node]:
            if next_node in team:
                return len(team[team.index(next_node):])
            return 0
        else:
            visited[next_node] = True
            queue.append(next_node)

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)

    cnt = n
    for i in range(1, n+1):
        if not visited[i]:
            cnt -= bfs(i)
    print(cnt)
    
