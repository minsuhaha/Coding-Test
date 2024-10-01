import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, count):
    global max_cnt
    queue = deque([(sx, sy, count)])
    visited = [[False]*c for _ in range(r)]
    visited[sx][sy] = True

    while queue:
        x, y, cnt = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt+1))

    max_cnt = max(max_cnt, cnt)  


r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

max_cnt = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':
            bfs(i, j, 0)
print(max_cnt)
