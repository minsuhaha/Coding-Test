'''
- 각 칸에서 (동,서,남,북,상,하)으로 이동가능.
- # : 금(벽) - 이동불가
- . : 칸 - 이동가능

-> S -> E 가는 최단경로 구하기
'''

import sys
from collections import deque
input = sys.stdin.readline

# 동,서,남,북,상,하
move = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]

def bfs(z, x, y):
    queue = deque([(z, x, y)])
    visited[z][x][y] = 0

    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + move[i][0]
            ny = y + move[i][1]
            nz = z + move[i][2]

            if 0<=nx<R and 0<=ny<C and 0<=nz<L:
                if graph[nz][nx][ny] == 'E':
                    return visited[z][x][y] + 1

                if graph[nz][nx][ny] == '.' and visited[nz][nx][ny] == -1:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    queue.append((nz, nx, ny))
    return 0

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    
    graph = []
    for _ in range(L):
        lst = [list(input().rstrip()) for _ in range(R)]
        graph.append(lst)
        input().rstrip() # 빈줄 입력

    visited = [[[-1]*C for _ in range(R)] for _ in range(L)]    
    flag = True
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == 'S':
                    ans = bfs(i, j, k)
                    flag = False
                    break
            if not flag:
                break
        if not flag:
            break
    
    if ans:
        print(f'Escaped in {ans} minute(s).')
    else:
        print('Trapped!')
