import sys
from collections import deque
input = sys.stdin.readline


def bfs(num):
    queue = deque([num])
    visited[num] = True
    cycle = []

    while queue:
        node = queue.popleft()
        next_node = graph[node]

        cycle.append(node)
        
        if visited[next_node]:
            if next_node in cycle: # cycle안에 포함되어있지 않으면 이전 bfs에서 방문처리된거임
                return len(cycle[cycle.index(next_node):])
        else:
            visited[next_node] = True
            queue.append(next_node)
    
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    cnt = N
    for i in range(1, N+1):
        if not visited[i]:
            cnt -= bfs(i)

    print(cnt)
