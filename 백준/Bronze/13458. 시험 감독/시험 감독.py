import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# 기본적으로 모든 반에 총 감독이 1명은 필수
for i in range(n):
    A[i] -= B
cnt = n

# 부감독 수
for i in range(n):
    if A[i] > 0:
        if A[i] % C == 0:
            cnt += (A[i]//C)
        else:
            cnt += (A[i]//C) + 1
print(cnt)
