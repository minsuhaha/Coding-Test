'''
n일의 휴가기간동안 가능한 외주 수익 최대값 구하기

t, p / 외주작업기한, 수익
* 동시에 여러개의 일 불가
'''
import sys
input = sys.stdin.readline

n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]


def dfs(day, total):
    global max_total
    if day >= n:
        max_total = max(max_total, total)
        return

    # 뛰어넘기
    dfs(day+1, total)

    if day + work[day][0] <= n:
        dfs(day+work[day][0], total+work[day][1])

max_total = 0
dfs(0, 0)
print(max_total)