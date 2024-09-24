import sys
from collections import deque
input = sys.stdin.readline


def bfs(node):
    queue = deque([node])
    visited[node] = 1

    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if visited[next_node]:
                if visited[node] == visited[next_node]:
                    return False
            else:
                if visited[node] == 1:
                    visited[next_node] = -1
                else:
                    visited[next_node] = 1
                queue.append(next_node)
            
    return True

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    flag = True
    for node in range(1, V+1):
        if not visited[node]:
            if not bfs(node):
                flag = False
                break
    print('YES') if flag else print('NO')
