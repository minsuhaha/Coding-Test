import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    queue = deque([(x, y)])    
    graph[x][y] = cnt

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = cnt
                    queue.append((nx, ny))                    

def bfs2(num):
    queue = deque()
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == num:
                queue.append((i, j, 0))

    while queue:
        x, y, d = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] != num and graph[nx][ny] > 1:
                    return d
                
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, d+1))
    return INF
                    
# 1. 섬끼리 묶기
cnt = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            bfs(i, j, cnt)

# 2. 섬끼리의 최소거리 구하기
ans = INF
for i in range(2, cnt+1):
    ans = min(ans, bfs2(i))
print(ans)
