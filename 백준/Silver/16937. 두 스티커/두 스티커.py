import sys
input = sys.stdin.readline

# 1. 두 스티커 모두 회전 x
# 2. 첫번째 스티커 회전 o / 두번째 스티커 회전 x
# 3. 첫번째 스티커 회전 x / 두번째 스티커 회전 o
# 4. 두 스티커 모두 회전 o

h, w = map(int, input().split())
n = int(input())
sticker = [list(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(n-1):
    for j in range(i+1, n):
        r1, c1 = sticker[i]
        r2, c2 = sticker[j]

        if r1+r2 <= h and max(c1, c2) <= w or max(r1, r2) <= h and c1+c2 <= w:
            result = max(result, r1*c1 + r2*c2)
        elif r2+c1 <= h and max(c2,r1) <= w or max(c1, r2) <= h and r1+c2 <= w:
            result = max(result, r1*c1 + r2*c2)
        elif r1+c2 <= h and max(c1, r2) <= w or max(c2, r1) <= h and r2+c1 <= w:
            result = max(result, r1*c1 + r2*c2)
        elif c1+c2 <= h and max(r1, r2) <= w or max(c1, c2) <= h and r1+r2 <= w:
            result = max(result, r1*c1 + r2*c2)

print(result)