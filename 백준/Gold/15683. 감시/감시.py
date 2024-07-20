import sys
import copy
input = sys.stdin.readline
INF = float('inf')

# 위 오른 아래 왼
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

direction = [
    [],
    [[0], [1], [2], [3]], # 1번 
    [[0, 2], [1, 3]], # 2번 
    [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번
    [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]], # 4번
    [[0, 1, 2, 3]] # 5번
]

def check(x, y, dir, cctv):
    for d in dir:
        nx, ny = x, y
        
        while True:
            nx += dx[d]
            ny += dy[d]

            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                break
            if cctv[nx][ny] == 6:
                break
            if cctv[nx][ny] == 0:
                cctv[nx][ny] = -1 # 감시가능구역 체크

def dfs(depth, cctv):
    global total_cnt
    if depth == len(cctv_info):
        cnt = 0
        for i in range(N):
            cnt += cctv[i].count(0)
        total_cnt = min(cnt, total_cnt)
        return
    
    cctv_copy = copy.deepcopy(cctv)
    x, y, cctv_type = cctv_info[depth]
    for dir in direction[cctv_type]:
        check(x, y, dir, cctv_copy)
        dfs(depth+1, cctv_copy)
        cctv_copy = copy.deepcopy(cctv)

N, M = map(int, input().split())
cctv = [list(map(int, input().split())) for _ in range(N)]
cctv_info = []
for i in range(N):
    for j in range(M):
        if 1 <= cctv[i][j] <= 5:
            cctv_info.append((i, j, cctv[i][j]))

total_cnt = INF
dfs(0, cctv)
print(total_cnt)
