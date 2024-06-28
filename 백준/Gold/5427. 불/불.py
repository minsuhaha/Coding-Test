import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(fqueue, squeue):
    cnt = 0 # 시간 초기화 (초)

    while squeue:
        cnt += 1

        # 불 먼저 이동시킴 (이제 불이 붙을 예정 인 곳도 상근이는 못가기 때문에 선후관계)
        while fqueue and fqueue[0][2] < cnt: # 현재 초를 넘어가지않도록 설정하기 위해
            y, x, time = fqueue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > w-1 or ny < 0 or ny > h-1:
                    continue
                
                if graph[ny][nx] == '.':
                    fqueue.append((ny, nx, time+1))
                    graph[ny][nx] = '*' # 불 방문표시

        # 상근이 이동
        while squeue and squeue[0][2] < cnt:
            y, x, time = squeue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > w-1 or ny < 0 or ny > h-1:
                    return cnt
                
                if graph[ny][nx] == '.':
                    squeue.append((ny, nx, time+1))
                    graph[ny][nx] = '..'  # 상근이 방문처리

    return 'IMPOSSIBLE'
    

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]

    fqueue = deque() # 불 이동 큐
    squeue = deque() # 상근이 이동 큐

    for i in range(h):
        for j in range(w):
            # 불 일 경우
            if graph[i][j] == '*':
                fqueue.append((i, j, 0))

            # 상근이의 현재 위치
            elif graph[i][j] == '@':
                squeue.append((i, j, 0))
                graph[i][j] = '.'

    res = bfs(fqueue, squeue)
    print(res)      
