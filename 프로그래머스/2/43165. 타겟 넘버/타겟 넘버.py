def solution(numbers, target):
    answer = 0
    
    def dfs(idx, total):
        nonlocal answer
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        
        dfs(idx+1, total+numbers[idx]) # 양수
        dfs(idx+1, total-numbers[idx]) # 음수

    dfs(0, 0)
    return answer
                
        