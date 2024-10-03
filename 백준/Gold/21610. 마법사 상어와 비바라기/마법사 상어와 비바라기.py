import sys, copy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 초기 구름 생성
queue = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])
for _ in range(m):
    d, s = map(int, input().split())
    cloud = deque()

    # 1. 구름이 d방향으로 s칸 이동
    while queue:
        x, y = queue.popleft()
        
        nx = (x + dx[d-1]*s) % n
        ny = (y + dy[d-1]*s) % n
        
        graph[nx][ny] += 1
        cloud.append((nx, ny))
        visited[nx][ny] = True # 구름 칸 체크
    
    
    # 2. 구름 대각선 방향 체크 후 구름 제거
    while cloud:
        x, y = cloud.popleft()
        for i in range(1, 8, 2):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] >= 1:
                    graph[x][y] += 1

    # 3. 구름 생성
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and not visited[i][j]:
                graph[i][j] -= 2
                queue.append((i, j))
            elif visited[i][j]:
                visited[i][j] = False

print(sum(map(sum, graph)))
