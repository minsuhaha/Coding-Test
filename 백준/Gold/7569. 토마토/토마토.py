import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]


dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((k, j, i))

while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or nx > m-1 or ny < 0 or ny > n-1 or nz < 0 or nz > h-1:
            continue
       
        if tomato[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
            visited[nz][ny][nx] = True
            tomato[nz][ny][nx] = tomato[z][y][x] + 1
            queue.append((nx, ny, nz))

result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, tomato[i][j][k])

print(result-1)
