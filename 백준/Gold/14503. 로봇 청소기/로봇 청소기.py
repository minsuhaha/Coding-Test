'''
문제
    1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        2.1 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        2.2 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
    3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우, 
        3.1 반시계 방향으로 90도 회전한다.
        3.2 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        3.3 1번으로 돌아간다.

*  d가 0인 경우 북쪽 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽을 바라보고 있는 것이다.

결론
- 로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy, sd):
    queue = deque([(sx, sy, sd)])
    visited[sx][sy] = True
    cnt = 1

    while queue:
        x, y, d = queue.popleft()

        flag = False
        for _ in range(4):
            d = (d+3) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    queue.append((nx, ny, d))
                    flag = True
                    break
        
        if not flag:
            if 0 <= x-dx[d] < n and 0 <= y-dy[d] < m and graph[x-dx[d]][y-dy[d]] != 1:
                queue.append((x - dx[d], y - dy[d], d))
            else:
                return cnt

n, m = map(int, input().split())
r, c, direction = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

print(bfs(r, c, direction))
