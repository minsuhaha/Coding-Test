import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    
    dp = [1]* (n+1)
    
    for i in range(2, 4):
        for j in range(i, n+1):
            dp[j] += dp[j-i]
    
    print(dp[n])