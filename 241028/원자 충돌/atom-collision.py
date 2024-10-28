import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
move_graph = []
for _ in range(m):
    x, y, m, s, d = map(int, input().split())
    move_graph.append((x-1, y-1, m, s, d))

move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for _ in range(k):
    # 1. 자신의 방향으로 자신의 속력만큼 이동
    while move_graph:
        x, y, m, s, d = move_graph.pop()
        nx = (x + move[d][0]*s) % n
        ny = (y + move[d][1]*s) % n
        graph[nx][ny].append((m, s, d))

  
    for i in range(n):
        for j in range(n):
            # 3. 이동이 끝난 후, 하나의 칸에 1개의 원자가 있을경우
            if len(graph[i][j]) == 1:
                _m, _s, _d = graph[i][j].pop()
                move_graph.append((i, j, _m, _s, _d))
            
            # 2. 이동이 끝난 후, 하나의 칸에 2개 이상의 원자가 있는 경우
            elif len(graph[i][j]) >= 2:
                sum_m, sum_s, even_cnt, odd_cnt = 0, 0, 0, 0
                n_cnt = len(graph[i][j])
                while graph[i][j]:
                    _m, _s, _d = graph[i][j].pop()
                    sum_m += _m
                    sum_s += _s
                    
                    if _d % 2 == 0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1
                
                if even_cnt == n_cnt or odd_cnt == n_cnt:
                    move_d = (0, 2, 4, 6)
                else:
                    move_d = (1, 3, 5, 7)
                
                if sum_m // 5 != 0:
                    for x in range(4):
                        move_graph.append((i, j, sum_m//5, sum_s//n_cnt, move_d[x]))

print(sum(move[2] for move in move_graph))