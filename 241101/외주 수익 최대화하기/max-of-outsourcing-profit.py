'''
n일의 휴가기간동안 가능한 외주 수익 최대값 구하기

t, p / 외주작업기한, 수익
* 동시에 여러개의 일 불가
'''
import sys
input = sys.stdin.readline

n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]

def dfs(idx, start, total):
    global max_total
    if start >= n or idx == n:
        max_total = max(max_total, total)
        return
    
    if start + work[idx][0] <= n:
        dfs(idx+1, start + work[idx][0], total+work[idx][1])

    elif start + work[idx][0] > n:
        dfs(idx+1, start, total)

max_total = 0 
for i in range(n):
    dfs(i, i, 0)

print(max_total)