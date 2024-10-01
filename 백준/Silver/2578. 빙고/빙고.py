'''
문제
- 5X5 빙고판 존재
- 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 빙고 +1 -> 줄에 선을 긋는다
결론
- 선이 3개이상 그어지는 경우 게임 끝
'''

def bingo():
    cnt = 0
    # 세로줄
    for x in range(5):
        if all(visited[y][x] for y in range(5)):
            cnt += 1
    # 가로줄
    for y in range(5):
        if all(visited[y][x] for x in range(5)):
            cnt += 1
    
    # 대각선 왼
    if all(visited[i][i] for i in range(5)):
        cnt += 1
    # 대각선 오
    if all(visited[i][4-i] for i in range(5)):
        cnt += 1
    
    return cnt

import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
speak = [list(map(int, input().split())) for _ in range(5)]
visited = [[False]*5 for _ in range(5)]

graph_check = {}
for i in range(5):
    for j in range(5):
        graph_check[graph[i][j]] = (j, i)


time = 0
for i in range(5):
    for j in range(5):
        time += 1
        x, y = graph_check[speak[i][j]]
        visited[y][x] = True
        if bingo() >= 3:
            print(time)
            exit()
