def solution(k, dungeons):
    def dfs(hp, cnt):
        nonlocal max_cnt
        max_cnt = max(max_cnt, cnt)
        
        for i in range(len(dungeons)):
            if not visited[i] and hp >= dungeons[i][0]:
                visited[i] = True
                dfs(hp-dungeons[i][1], cnt+1)
                visited[i] = False
    
    
    max_cnt = 0
    visited = [False] * len(dungeons)
    dfs(k, 0)
    return max_cnt
    
    