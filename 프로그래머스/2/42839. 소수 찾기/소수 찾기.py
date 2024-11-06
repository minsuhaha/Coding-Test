def solution(numbers):
    def prime(number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
    def dfs(res):
        if 0 < len(res) <= len(numbers):
            if prime(int(res)):
                numbers_cnt.add(res)
        
        for i, number in enumerate(numbers):
            if visited[i]:
                continue
            if res == '' and number == '0':
                continue
            visited[i] = True
            dfs(res+number)
            visited[i] = False
                
            
    visited = [False] * len(numbers)
    numbers_cnt = set()
    dfs('')
    return len(numbers_cnt)