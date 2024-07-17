import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if cheeze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif cheeze[nx][ny] == 1:
                    cheeze[nx][ny] = 0
                    visited[nx][ny] = True
                    cnt += 1 # 현재 녹인 치즈개수
    
    return cnt

r, c = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(r)]

hour = 0
left_cnt = 0
while True:
    visited = [[False]*c for _ in range(r)]
    res = bfs(0, 0)
    if not res:
        break
    hour += 1
    left_cnt = res
    
print(hour)
print(left_cnt)
