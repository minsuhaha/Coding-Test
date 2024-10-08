import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    W = int(input())

    dp = [0] * (N+1)

    queue = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = D[i]
    
    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            dp[next_node] = max(dp[next_node], dp[node] + D[next_node])
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                queue.append(next_node)
    print(dp[W])
