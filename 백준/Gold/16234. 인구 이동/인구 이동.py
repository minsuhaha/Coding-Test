import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    union = []
    union.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if L <= abs(graph[x][y]-graph[nx][ny]) <= R and not visited[nx][ny]:
                queue.append((nx, ny))
                union.append((nx, ny))
                visited[nx][ny] = True

    if len(union) <= 1:
        return 0
    res = sum(graph[x][y] for x, y in union) // len(union)
    for x, y in union:
        graph[x][y] = res
    return 1

day = 0
while True:
    cnt = 0
    visited = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += bfs(i, j)
    
    if cnt == 0:
        break

    day += 1

print(day)
