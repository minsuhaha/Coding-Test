import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
graph_re = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y) # outdegree
    graph_re[y].append(x)  # indegree
    
s, e = map(int, input().split())

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    
# s -> e
visited1 = [False] * (n+1)
visited1[e] = True
bfs(s, graph, visited1)

# e -> s
visited2 = [False] * (n+1)
visited2[s] = True
bfs(e, graph, visited2)

# x -> s
visited3 = [False] * (n+1)
bfs(s, graph_re, visited3)

# x -> e
visited4 = [False] * (n+1)
bfs(e, graph_re, visited4)

cnt = 0
for i in range(1, n+1):
    if i == s or i == e:
        continue
    if visited1[i] and visited2[i] and visited3[i] and visited4[i]:
        cnt += 1
print(cnt)
