import sys
from itertools import combinations
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

hospital = []
people = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            people.append((i, j))
        elif graph[i][j] == 2:
            hospital.append((i, j))
        

answer = INF
for comb in combinations(hospital, m):
    dist_cnt = 0
    for x1, y1 in people:
        dist = INF
        for x2, y2 in comb:
            dist = min(dist, abs(x1-x2) + abs(y1-y2))
        dist_cnt += dist
    answer = min(answer, dist_cnt)


print(answer)