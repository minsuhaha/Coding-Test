import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

fqueue = deque() # 초기 불이 있는 위치
jqueue = deque() # 초기 지훈이가 있는 위치

def bfs(fqueue, jqueue):
    minute = 0 # 시간 초기화(분)

    while jqueue:
        minute += 1 # 1분씩 올라감

        while fqueue and fqueue[0][2] < minute:
            y, x, time = fqueue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > c-1 or ny < 0 or ny > r-1:
                    continue
                if graph[ny][nx] == '.':
                    graph[ny][nx] = 'F' # 불로 번짐표시
                    fqueue.append((ny, nx, time+1))

        while jqueue and jqueue[0][2] < minute:
            y, x, time = jqueue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > c-1 or ny < 0 or ny > r-1:
                    return minute
                
                if graph[ny][nx] == '.':
                    jqueue.append((ny, nx, time+1))
                    graph[ny][nx] = '..' # 지훈이 방문처리

    return 'IMPOSSIBLE'

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            fqueue.append((i, j, 0))
        elif graph[i][j] == 'J':
            jqueue.append((i, j, 0))
            graph[i][j] = '.' # 지훈이 방분처리        

res = bfs(fqueue, jqueue)
print(res)       