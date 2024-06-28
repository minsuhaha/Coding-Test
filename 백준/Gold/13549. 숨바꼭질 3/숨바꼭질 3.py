import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [0] * (100001)
visited = [False for _ in range(100001)]

def bfs(v):
    ans = 0
    queue = deque([v])
    visited[v] = True

    while queue:
        x = queue.popleft()
    
        # k값과 동일할때
        if x == k:
            ans = graph[x]
            break

        # 순간이동
        if (x*2) < 100001 and not visited[x*2]:
            graph[x*2] = graph[x]
            visited[x*2] = True
            queue.append(x*2)
        
        # 뒤로 한칸이동
        if (x-1) >= 0 and not visited[x-1]:
            graph[x-1] = graph[x] + 1
            visited[x-1] = True
            queue.append(x-1)

        # 앞으로 한칸이동
        if (x+1) < 100001 and not visited[x+1]:
            graph[x+1] = graph[x] + 1
            visited[x+1] = True
            queue.append(x+1)
    
    return ans

print(bfs(n))
