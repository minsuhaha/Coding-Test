import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(fqueue, jqueue):
    minute = 0
    while jqueue:
        minute += 1
        while fqueue and fqueue[0][2] < minute:
            x, y, m = fqueue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > R-1 or ny < 0 or ny > C-1:
                    continue

                if graph[nx][ny] == '.':
                    graph[nx][ny] = 'F'
                    fqueue.append((nx, ny, m+1))

        while jqueue and jqueue[0][2] < minute:
            x, y, m = jqueue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > R-1 or ny < 0 or ny > C-1:
                    return minute
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '..'
                    jqueue.append((nx, ny, m+1))

    return 'IMPOSSIBLE'

fqueue, jqueue = deque(), deque()
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            fqueue.append((i, j, 0))
        if graph[i][j] == 'J':
            jqueue.append((i, j, 0))
            graph[i][j] = '..'

print(bfs(fqueue, jqueue))
