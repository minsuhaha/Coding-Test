def solution(numbers, target):
    def dfs(idx, total):
        nonlocal cnt
        if idx == len(numbers):
            if total == target:
                cnt += 1
            return
        
        dfs(idx+1, total+numbers[idx])
        dfs(idx+1, total-numbers[idx])
        
    cnt = 0
    res = []
    dfs(0, 0)
    return cnt