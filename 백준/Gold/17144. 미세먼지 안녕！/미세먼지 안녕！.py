import sys
from collections import deque

input = sys.stdin.readline

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

# 1. 미세먼지 확장
def spread():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    graph_copy = [[0]*c for _ in range(r)]
    queue = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                queue.append((i, j)) # 미세먼지 초기화
    
    while queue:
        x, y = queue.popleft()
        tmp = graph[x][y] // 5
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c and graph[nx][ny] != -1:
                graph_copy[nx][ny] += tmp
                graph_copy[x][y] -= tmp
    
    for i in range(r):
        for j in range(c):
            graph[i][j] += graph_copy[i][j]

# 2. 공기청정기 머리
def up_cleaner():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x, y = up, 0
    before = 0
    d = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]

        if nx == up and ny == 0:
            break

        if 0 > nx or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue

        graph[nx][ny], before = before, graph[nx][ny]
        x, y = nx, ny

# 3. 공기청정기 아래
def down_cleaner():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = down, 0
    before = 0
    d = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]

        if nx == down and ny == 0:
            break

        if 0 > nx or nx >= r or ny < 0 or ny >= c:
            d += 1
            continue

        graph[nx][ny], before = before, graph[nx][ny]
        x, y = nx, ny


# 공기청정기 좌표구하기
up, down = 0, 0
for i in range(r):
    if graph[i][0] == -1:
        up = i
        down = i + 1
        break

for _ in range(t):
    spread()
    up_cleaner()
    down_cleaner()

total = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            total += graph[i][j]
print(total)
