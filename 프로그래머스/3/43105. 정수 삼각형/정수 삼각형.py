def solution(triangle):
    dp = [[0]*(len(triangle)+1) for _ in range(len(triangle)+1)]
    
    for i in range(1, len(triangle)+1):
        for j in range(1, i+1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i-1][j-1]
    
    return max(dp[len(triangle)])