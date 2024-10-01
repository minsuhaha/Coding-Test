import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, c):
    queue = deque([(sx, sy, c)])
    visited = [[False]*m for _ in range(n)]
    visited[sx][sy] = True

    while queue:
        x, y, cnt = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt+1))
            

    ans.append((cnt, graph[sx][sy]+graph[x][y])) 


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            bfs(i, j, 0)

ans.sort(key=lambda x : (-x[0], -x[1]))
print(ans[0][1])
