import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited1 = [[False]*n for _ in range(n)]
visited2 = [[False]*n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

# 적녹색약 x
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs(i, j, visited1)
            cnt1 += 1


# 적녹색약 O
# graph 상에서 초록색 -> 빨간색으로 변경해주기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs(i, j, visited2)
            cnt2 += 1

print(f'{cnt1} {cnt2}')