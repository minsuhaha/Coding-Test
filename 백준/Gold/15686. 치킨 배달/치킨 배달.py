import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chicken, house = [], []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i,j))
        elif graph[i][j] == 1:
            house.append((i,j))

total_chicken_dist = INF
for comb in combinations(chicken, m):
    now_chicken_dist = 0
    for h in house:
        dist = INF
        for c in comb:
            dist = min(dist, abs(h[0]-c[0])+abs(h[1]-c[1]))
        now_chicken_dist += dist
    total_chicken_dist = min(total_chicken_dist, now_chicken_dist)
print(total_chicken_dist)
