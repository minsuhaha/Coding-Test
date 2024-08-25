import sys
from collections import deque

n = int(input())
graph = [0] + list(map(int, input().split()))
visited = [False] * (n+1)
s = int(input())

def bfs(x):
    queue = deque([x])
    visited[x] = True
    cnt = 1

    while queue:
        x = queue.popleft()
        
        # 왼쪽 이동
        if 0 < x - graph[x] < n+1 and not visited[x-graph[x]]:
            cnt += 1
            queue.append(x-graph[x])
            visited[x-graph[x]] = True
        # 오른쪽 이동
        if 0 < x + graph[x] < n+1 and not visited[x+graph[x]]:
            cnt += 1
            queue.append(x+graph[x])
            visited[x+graph[x]] = True
    return cnt

print(bfs(s))
