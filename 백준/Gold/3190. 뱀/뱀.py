'''
문제 
    1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다. -> 우선 벽이나 자리 몸에 부딪히지 않을 때 머리 이동 시킴
    2. 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝
    3. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음. -> 몸 길이 늘어남
    4. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. -> 몸길이는 변하지 않음.
* 뱀은 처음에 오른쪽 방향을 보고있음.

결론
- 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)] # 빈칸 초기화
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 2 # 사과 배치

l = int(input())
snake_dict = {}
for _ in range(l):
    x, c = input().rstrip().split()
    snake_dict[int(x)] = c

queue = deque([(0, 0)]) # 초기 뱀의 위치
graph[0][0] = 1 # 초기 뱀

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0
nx, ny = 0, 0
dir = 0
while queue:
    time += 1
    
    nx = nx + dx[dir]
    ny = ny + dy[dir]

    # graph 밖 범위거나, 자기 몸통과 만날 때
    if nx < 0 or nx >= n or ny < 0 or ny >=n or graph[nx][ny] == 1:
        break
    
    # 사과가 있는 칸
    if graph[nx][ny] == 2:
        graph[nx][ny] = 1
        queue.append((nx, ny)) # 뱀의 머리 위치
    
    # 사과가 없는 칸
    elif graph[nx][ny] == 0:
        x, y = queue.popleft()
        graph[x][y] = 0 # 뱀의 꼬리 한칸 댕기기
        graph[nx][ny] = 1
        queue.append((nx, ny)) # 뱀의 머리 위치


    if time in snake_dict:
        if snake_dict[time] == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4

print(time)
    