def solution(k, dungeons):
    
    def dfs(hp, cnt):
        nonlocal answer
        answer = max(answer, cnt)
    
        for i in range(len(dungeons)):
            if dungeons[i][0] <= hp and not visited[i]:
                visited[i] = True
                dfs(hp-dungeons[i][1], cnt+1)
                visited[i] = False
    
    answer = 0
    visited = [False] * len(dungeons)
    dfs(k, 0)
    return answer