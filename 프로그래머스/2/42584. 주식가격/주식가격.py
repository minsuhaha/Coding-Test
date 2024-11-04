from collections import deque
def solution(prices):
    stack = []
    queue = deque()
    for idx, price in enumerate(prices):
        queue.append((idx, price))
    
    down = []
    while queue:
        idx, price = queue.popleft()
        
        while stack and stack[-1][1] > price:
            ans = stack.pop()
            down.append((ans[0] ,idx-ans[0]))           
        stack.append((idx, price))
    
    n = len(prices)
    answer = [0] * n
    for idx, price in stack:
        answer[idx] = (n-1)-idx
    
    for idx, rank in down:
        answer[idx] = rank
    
    return answer
    
    