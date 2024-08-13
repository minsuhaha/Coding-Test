import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(x):
    queue = deque([x])
    visited[x] = 1

    while queue:
        node = queue.popleft()
        
        if node == p2:
            return visited[node] - 1
        for next_node in graph[node]:
            if graph[next_node] and not visited[next_node]:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)
    return -1

print(bfs(p1))
