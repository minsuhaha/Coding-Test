import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 초기 토마토 있는 위치 queue에 넣어주기
queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((j, i))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
            continue
        if tomato[ny][nx] == 0:
            queue.append((nx, ny))
            tomato[ny][nx] = tomato[y][x] + 1
                
res = 1
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        if res < tomato[i][j]:
            res = tomato[i][j]
print(res-1)