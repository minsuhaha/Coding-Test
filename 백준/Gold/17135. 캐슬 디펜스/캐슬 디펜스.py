import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline


N, M, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1]
dy = [0, -1, 0]

def bfs(anch1, anch2, anch3):
    graph_copy = copy.deepcopy(graph)
    die_cnt = 0

    for _ in range(N):
        die_set = set()
    
        for m in (anch1, anch2, anch3):
            queue = deque([(N-1, m, 1)]) # 성보다 1줄 앞줄에서 탐색

            while queue:
                y, x, dist = queue.popleft()

                if graph_copy[y][x] == 1:
                    die_set.add((y, x))
                    break
                    
                for i in range(3):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0<=nx<M and 0<=ny<N and dist < D:
                        queue.append((ny, nx, dist+1))

        for y, x in die_set:
            graph_copy[y][x] = 0
            die_cnt += 1

        # 적 한칸아래로 이동
        for row in range(N-1, 0, -1):
            graph_copy[row] = graph_copy[row-1][:]
        graph_copy[0] = [0]*M

    return die_cnt

result = 0
for ancher in combinations(range(M), 3):
    result = max(result, bfs(ancher[0], ancher[1], ancher[2]))
print(result)
