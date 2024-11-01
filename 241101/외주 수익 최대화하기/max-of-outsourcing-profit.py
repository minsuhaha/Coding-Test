'''
n일의 휴가기간동안 가능한 외주 수익 최대값 구하기

t, p / 외주작업기한, 수익
* 동시에 여러개의 일 불가
'''
import sys
input = sys.stdin.readline

n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]

max_total = 0
for i in range(n):
    time = n
    total = 0
    idx = i
    while True:
        time -= (work[idx][0] + idx)
        if time < 0:
            break
        total += work[idx][1]
        idx += 1
        if idx == n:
            break
    max_total = max(max_total, total)
print(max_total)