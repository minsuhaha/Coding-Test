'''
문제
일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

0 : 빈 칸 
1 :벽
2 : 바이러스

결론
벽을 3개 세워서 바이러스가 모든 빈 칸으로 퍼지지않도록 막을 경우의 안전영역 칸 개수 구하기
'''
import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(comb):
    graph_copy = copy.deepcopy(graph)
    cnt = 0

    # 벽으로 변경
    for com in comb:
        graph_copy[com[0]][com[1]] = 1

    # 바이러스 초기 위치 queue에 넣어주기
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == 2:
                queue.append((i, j))
                
    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n:
                if graph_copy[ny][nx] == 0:
                    graph_copy[ny][nx] = 2
                    queue.append((ny, nx))
    
    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == 0:
                cnt += 1
    
    return cnt

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

blank = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i, j))

max_cnt = 0
for comb in combinations(blank, 3):
    max_cnt = max(max_cnt, bfs(comb))
print(max_cnt)
