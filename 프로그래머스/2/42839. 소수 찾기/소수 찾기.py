def solution(numbers):
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    def dfs(res):
        if res and is_prime(int(res)):
            prime_set.add(res)
        
        for i in range(len(numbers)):
            if not res and numbers[i] == '0':
                continue
            if not visited[i]:
                visited[i] = True
                dfs(res+numbers[i])
                visited[i] = False
        
    
    visited = [False] * len(numbers)
    prime_set = set()
    dfs('')
    return len(prime_set)