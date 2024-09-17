import sys
input = sys.stdin.readline

A, B, C, X, Y = map(int, input().split())

# 1. 개별로만 구입
# 2. 반반으로만 구입
# 3. 반반 + 개별 구입

# 1. 개별로만 구매
total1 = A*X + B*Y

# 2. 반반으로만 구입
total2 = 2 * C * max(X,Y)

# 3. 반반 + 개별 구입
total3 = min(total1, total2)
for i in range(1, max(X,Y)+1):
    total3 = min(total3, 2*C*i + A*max(X-i, 0) + B*max(Y-i,0))

print(total3)