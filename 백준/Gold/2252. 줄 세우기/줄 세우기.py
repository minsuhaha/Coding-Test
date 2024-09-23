import sys
from collections import deque
input = sys.stdin.readline

answer = []
def bfs():
    queue = deque()
    for i in range(1, n+1):
        if check[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        answer.append(node)

        for next_node in graph[node]:
            check[next_node] -= 1
            if check[next_node] == 0:
                queue.append(next_node)
    return answer

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
check = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    check[b] += 1

print(*bfs())
