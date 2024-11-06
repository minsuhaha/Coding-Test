def solution(k, dungeons):
    
    def dfs(hp, cnt):
        nonlocal max_cnt
        max_cnt = max(max_cnt, cnt)
        
        for idx, dungeon in enumerate(dungeons):
            if not visited[idx]:
                if hp >= dungeon[0]:
                    visited[idx] = True
                    dfs(hp-dungeon[1], cnt+1)
                    visited[idx] = False
        
    
    max_cnt = 0
    visited = [False] * (len(dungeons))
    dfs(k, 0)
    return max_cnt