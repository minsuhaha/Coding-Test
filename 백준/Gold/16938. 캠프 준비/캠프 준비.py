'''
N : 문제개수
L <= 문제난이도합 <= R
X <= 가장어려운 문제난이도 - 가장쉬운 문제난이도
'''
import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
score = list(map(int, input().split()))




def dfs(idx, max_num, min_num, sum_num):
    global cnt
    if len(res) == N:
        if L <= sum_num <= R and X <= max_num-min_num:
            cnt += 1
        return
    elif len(res) >= 2:
        if L <= sum_num <= R and X <= max_num-min_num:
            cnt += 1
    
    for i in range(idx, N):
        res.append(score[i])
        dfs(i+1, max(max_num, score[i]), min(min_num, score[i]), sum_num+score[i])
        res.pop()
        
cnt = 0
res = []
dfs(0, 1, 10**6, 0)
print(cnt)
