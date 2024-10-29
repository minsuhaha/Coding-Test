import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우


def high_cleaner():
    move = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 우상좌하
    x, y = up, 0
    d = 0
    prior = 0
    while True:
        nx = x + move[d][0]
        ny = y + move[d][1]

        if nx == up and ny == 0:
            break

        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            d += 1
            continue
        
        graph[nx][ny], prior = prior, graph[nx][ny]
        x, y = nx, ny


def low_cleaner():
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)] #우하좌상
    x, y = down, 0
    d = 0
    prior = 0
    while True:
        nx = x + move[d][0]
        ny = y + move[d][1]

        if nx == down and ny == 0:
            break

        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            d += 1
            continue
        
        graph[nx][ny], prior = prior, graph[nx][ny]
        x, y = nx, ny


# 시공의 돌풍 위치 위/아래 위치 구해주기
for i in range(n):
    if graph[i][0] == -1:
        up = i
        down = i + 1
        break


for _ in range(t):
    # 1. 먼지 확산
    graph_copy = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if graph[x][y] != -1: # 시공의 돌풍이 아닐 때
                for k in range(4):
                    nx = x + move[k][0]
                    ny = y + move[k][1]
                    if 0<=nx<n and 0<=ny<m and graph[nx][ny] != -1:
                        graph_copy[x][y] -= graph[x][y] // 5
                        graph_copy[nx][ny] += graph[x][y] // 5

    for i in range(n):
        for j in range(m):
            graph[i][j] += graph_copy[i][j]

    # 2. 돌풍의 청소
    high_cleaner()
    low_cleaner()

total = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            total += graph[i][j]
print(total)