import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    count += 1
                    queue.append((nx, ny))
    return count

res = []
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            res.append(bfs(i, j))
            cnt += 1

print(cnt)
for r in sorted(res):
    print(r)
