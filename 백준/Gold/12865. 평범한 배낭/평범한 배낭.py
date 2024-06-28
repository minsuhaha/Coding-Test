import sys
input = sys.stdin.readline

# n : 물품 수, k : 버틸 수 있는 문게
n, k = map(int,input().split())
# bag에 들어있는 리스트 [무게, 가치]
bag = [[0,0]]
for i in range(n):
    bag.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < bag[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i][0]] + bag[i][1])  

print(dp[n][k])






