'''
문제
1. 체스판의 모든 칸은 빈 칸 또는 벽 중 하나이다. 
    - 빈칸 : '.' / 벽 : '#'
2. 욱제의 캐릭터는 가장 왼쪽 아랫 칸에 있고 가장 오른쪽 윗 칸으로 이동해야 한다.
    - (0, 7) -> (7, 0)
3. 1초마다 모든 벽이 아래에 있는 행으로 한 칸씩 내려가고, 가장 아래에 있어서 아래에 행이 없다면 벽이 사라지게 된다. 
    - 인접한 한 칸 또는 대각선 방향으로 인접한 한 칸으로 이동하거나, 현재 위치에 서 있을 수 있음 
    - 즉 총 9개의 케이스로 이동 가능
4. 1초 동안 욱제의 캐릭터가 먼저 이동하고, 그 다음 벽이 이동한다. 벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없다.

결론
욱제의 캐릭터가 가장 오른쪽 윗 칸으로 이동할 수 있는지 없는지 구해보자.
'''

dx = [0, 0, 1, 1, 1, 0, -1, -1, -1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def bfs():
    pqueue.append((0, 7, 0))
    time = 0
    while pqueue:
        visited = [[False]*8 for _ in range(8)]
        time += 1
        while pqueue and pqueue[0][2] < time:
            x, y, z = pqueue.popleft()
            
            if graph[y][x] == '#':
                continue
            
            if x == 7 and y == 0:
                return 1
            
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<8 and 0<=ny<8:
                    if graph[ny][nx] == '.' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        pqueue.append((nx, ny, z+1))
        move_wall()

    return 0                

def move_wall():
    # 1초마다 벽 아래로 한칸 씩 움직임
    global graph
    graph_copy = [['.']*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if graph[i][j] == '#':
                if i+1 < 8:
                    graph_copy[i+1][j] = '#'
    graph = graph_copy

import sys
from collections import deque
input = sys.stdin.readline
graph = [list(input().rstrip()) for _ in range(8)]

pqueue = deque()
print(bfs())
