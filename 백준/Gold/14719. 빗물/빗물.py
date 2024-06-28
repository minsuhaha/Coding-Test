import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))

cnt = 0
for i in range(1, len(block)-1):
    max_left = max(block[:i])
    max_right = max(block[i+1:])
    point = min(max_left, max_right) # 빗물 고이는 기준

    if point > block[i]:
        cnt += point - block[i]

print(cnt)
