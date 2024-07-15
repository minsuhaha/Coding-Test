import sys
from itertools import combinations
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 치킨 집, 일반 집 위치값 넣어주기
chicken, house = [], []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))

res = []
for comb in combinations(chicken, M):
    total = 0
    for h in house:
        cnt = INF
        for c in comb:
            cnt = min(cnt, abs(h[0]-c[0]) + abs(h[1]-c[1]))
        total += cnt
    res.append(total)

print(min(res))
